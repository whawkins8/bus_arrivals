# Functions for generating an alert when
# a bus is arriving in less than the input time.

import datetime
from GetArrivals import GetArrivals
from RouteAndStop import RouteAndStop
from GetBuses import GetBuses

def time_alert(RouteAndStop, alert_time):
    arrival_query = GetArrivals(RouteAndStop)
    arrival_time = arrival_query.arrival

    if arrival_time == -1:
        #TODO: maybe raise an exception.
        return False

    current_time = datetime.datetime.now()
    # here we need to handle converting minutes to seconds.
    alert_timedelta = datetime.timedelta(minutes=alert_time)
    if (arrival_time - current_time <= alert_timedelta):
        return True

    else:
        return False

def stop_alert(RouteAndStop, stop_id):
    buses = GetBuses(RouteAndStop).buses

    next_stops = []
    for bus in buses:
        # here we only add the next two stops to the list.
        # if we want to alert earlier, we can later add more stops
        # to be checked.
        next_stops.append(bus.arrivals[0]['stop_id'])
        next_stops.append(bus.arrivals[1]['stop_id'])

    if stop_id in next_stops:
        return True
    else:
        return False



if __name__ == '__main__':
    route_info = RouteAndStop('20', '4000034', '4101146')
    print(time_alert(route_info, 5))
    print(stop_alert(route_info, '4101146'))
