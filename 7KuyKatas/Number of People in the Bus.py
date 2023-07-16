def number(bus_stops):
    result = 0
    for stop_res in bus_stops:
            result += stop_res[0]
            result -= stop_res[1]
    return result