trip_summary= ("ubergo" , "Erode" , "Coimbatore" , 860.00 , "Completed") #creating a tuple to store the trip summary

print("Trip Summary:", trip_summary)

print("Trip Status:", trip_summary[0]) #accessing the first element of the tuple

trip_summary[1] = "Chennai"  # Attempting to modify the second element of the tuple (this will raise an error since tuples are immutable)
print("Updated Trip Summary:", trip_summary)  # Print the updated trip summary (this line will not be reached due to the error above)