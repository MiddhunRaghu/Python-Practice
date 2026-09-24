# trip = {
#     "trip_id": "UB12345",
#     "pickup_location": "Erode",
#     "dropoff_location": ["Thindal" , "Perundurai" , "Chennai"],
#     "fare": 860.00,
#     "status": "Completed",
#     "driver_name": "Ravi Kumar"
# }

# print(trip["pickup_location"])  # Accessing a value using its key

# print(trip.get("Erode"))  # Accessing a value using the get() method if value is not present it will return None

# print(trip.keys())  # Getting all the keys in the dictionary
# print(trip.values())  # Getting all the values in the dictionary

# for key,value in trip.items():
#     print(f"{key}: {value}")  # Iterating through the dictionary and printing key-value pairs

# trip.update({"Car_model" : "Volkswagen Polo"})  # Updating the dictionary with a new key-value pair
# print(trip)  # Printing the updated dictionary

# trip.pop("fare")  # Removing a key-value pair from the dictionary using the pop() method
# print(trip)  # Printing the dictionary after removing the key-value pair


# print(trip["dropoff_location"])  # Accessing a value from the list inside the dictionary
# print(trip["dropoff_location"][1])  # Accessing the first element of the list inside the dictionary

# for location in trip["dropoff_location"]:
#     print(location)  # Iterating through the list inside the dictionary and printing each location


trips = {
    "UB001" : {"trip_id" : "UB001" , "pickup_location" : "Erode" , "drop_location" : "Thindal" , "Fare" : 120},
    "UB002" : {"trip_id" : "UB002" , "pickup_location" : "Thindal" , "drop_location" : "Perundurai" , "Fare" : 120},
    "UB003" : {"trip_id" : "UB003" , "pickup_location" : "Perundurai" , "drop_location" : "Erode" , "Fare" : 240}  

}

# print(trips["UB001"]["Fare"])

for trip_id,details in trips.items():
    print(trip_id)
    print(details["pickup_location"] , "->" ,details["drop_location"] )