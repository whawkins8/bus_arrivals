import requests
from RouteAndStop import RouteAndStop
from config import get_transloc_key

class Bus:
    def __init__(self, ID, loc, arrivals):
        self.ID = ID
        self.loc = loc
        self.arrivals = arrivals

class GetBuses:
    # wrap transloc api calls to get the buses on a route.

    def __init__(self, route_and_stop):
        self.buses = []

        self.url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"
        self.querystring = {"routes":route_and_stop.route, "agencies":route_and_stop.agency}
        self.headers = {'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
                        'x-rapidapi-key': get_transloc_key()}

        self.get_response()

    def get_response(self):
        try:
            self.response = requests.request("GET", self.url, headers=self.headers,
                                             params=self.querystring)
            self.response.raise_for_status()

        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            self.buses.clear()
            return self.parse_response()

    def parse_response(self):
        #TODO: handle exception if there is a KeyError here.
        data = self.response.json()['data'][self.querystring['agencies']]

        for bus in data:
            ID = bus['vehicle_id']
            loc = bus['location']
            arriv = bus['arrival_estimates']
            newbus = Bus(ID, loc, arriv)
            self.buses.append(newbus)

        return self.buses


if __name__ == '__main__':
    routeinfo = RouteAndStop("20", "4000034", "4101146")
    b = GetBuses(routeinfo)




