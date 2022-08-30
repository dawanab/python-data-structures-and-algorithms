"""  
# For each element in the searchList
  > if element equal target value then
    >> Add its index to a list of occurrences
# if the list of occurrences is empty
  > raise ValueError
# otherwise
  > return the list occurrences

"""

def linear_search(search_list, target_value):
    matches = []
    for elm in range(len(search_list)):
        if search_list[elm] == target_value:
            matches.append(elm)
    if matches:
            return matches
    else:
        raise ValueError(f"{target_value} is not in the search_list.")



tour_locations = [ "New York City", "Los Angeles", "Bangkok",\
                   "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

print(linear_search(tour_locations, target_city))