# uber_city1 = {"Erode", "Coimbatore", "Chennai"}
# uber_city2 = {"Bangalore", "Coimbatore", "Hyderabad"}

# print(uber_city1.union(uber_city2))  # Union of two sets
# print(uber_city1.intersection(uber_city2))  # Intersection of two sets
# print(uber_city1.difference(uber_city2))  # Difference of two sets

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Print the original set
my_set.remove(3)  # Remove an element from the set
print(my_set)  # Print the updated set
my_set.add(6)  # Add an element to the set
print(my_set)  # Print the updated set after adding an element
my_set.discard(8)  # Discard an element from the set (no error if the element is not present)
print(my_set)  # Print the updated set after discarding an element