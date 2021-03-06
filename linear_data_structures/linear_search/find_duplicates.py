# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", 
"London", "New York City", "Toronto"]
target_city = "New York City"

# Linear Search Algorithm
def linear_search(search_list, target_value):
    matches = []
    for elm in range(len(search_list)):
        if search_list[elm] == target_value:
            matches.append(elm)
            return matches
    raise ValueError(f"{target_value} is not in list.")

# Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)
