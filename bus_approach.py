import requests
import json
import datetime
import dateutil.parser
from config import get_transloc_key

## GoRaleigh -> agency "20"
## Route 4 -> route = "4000034"
## stop -> stop = "4101146"

class RouteAndStop:
    # class for holding agency, route, and stop information.
    # agency, route, and stop should be strings.
    def __init__(self, agency, route, stop):
        self.agency = agency
        self.route = route
        self.stop = stop


class GetArrivals:
    # wrap API calls for retrieving arrival times.
    # Attributes:
    #   self.url - API url
    #   self.headers - API headers
    #   self.response - response from GET
    #   self.arrival - datetime object with arrival time. Set to -1 if API does not return a time.
    # Methods:
    #   __init__ - builds API query from input RouteAndStop, calls get_response().
    #   get_response - does a GET on the API, calls parse_response() to parse the json.
    #   parse_response - parses the json and extracts the time of arrival, and sets self.arrival.

    def __init__(self, route_and_stop):
        self.url = "https://transloc-api-1-2.p.rapidapi.com/arrival-estimates.json"
        self.querystring = {"routes":route_and_stop.route, "stops":route_and_stop.stop,
                        "agencies":route_and_stop.agency}
        self.headers = {'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com", 'x-rapidapi-key': get_transloc_key()}

        self.get_response()

    def get_response(self):
        try:
            self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
            self.response.raise_for_status()

        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return self.parse_response()

    def parse_response(self):
        response_data = self.response.json()

        num_arrivals = len(response_data['data'])
        if num_arrivals < 1:
            self.arrival = -1
            return self.arrival

        arriv_time = response_data['data'][0]['arrivals'][0]['arrival_at']
        self.arrival = dateutil.parser.parse(arriv_time)
        return self.arrival

    def __str__(self):
        return(str(self.arrival))

r = RouteAndStop("20", "4000034", "4101146")
arriv = GetArrivals(r)


