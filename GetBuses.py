import requests


class Bus:
    def __init__(self, ID, arrivals):
        self.ID = ID
        self.arrivals = arrivals

class GetBuses:
    # wrap transloc api calls to get the buses on a route.

    def __init__(self, route_and_stop):
        self.buses = []

        self.url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"
        self.querystring = {"routes":route_and_stop.route, "agencies":route_and_stop.agency}
        self.headers = {'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
                        'x-rapidapi-key': apikey}

        self.get_buses()

    def get_response(self):
        try:
            response = requests.request("GET", url, headers=self.headers, params=self.querystring)
            response.raise_for_status()

        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            self.parse_response()

    def parse_response(self):
        data = self.response.json()['data']["20"]

        for bus in data:
            ID = data['vehicle_id']
            loc = data['location']
            




