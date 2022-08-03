number_list = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33


def linear_search(search_list, target_value):
    for elm in range(len(search_list)):
        if search_list[elm] == target_value:
            return elm
    raise ValueError(f"{target_value} is not in the list.")


try:
  # Call the function below...
  result = linear_search(number_list, 100)
  print(result)

except ValueError as error_message:
  print("{0}".format(error_message))