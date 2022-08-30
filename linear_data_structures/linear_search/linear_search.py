"""  
1. Declare a function called linear_search() in Python with two parameters: 
search_list, as its first parameter, and target_value, as its second parameter.

2. In the function linear_search():
    > Create a for loop that iterates over the list with range() & len() methods.
    > Use the iterating variable to print each element in search_list

3. Within the for loop after printing the element:
    > Use an if statement that checks whether the element matches target_value.
        >> If so, return the index.

4. If you complete the loop and there is not a match, use ValueError() to raise 
an exception.
> Add a line outside the loop invoking raise ValueError() with "{target_value} 
not in list".
> Interpolate target_value into the string
"""

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