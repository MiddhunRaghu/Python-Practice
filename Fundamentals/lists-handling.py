# playlist = ["Naa Ready" , "Ramuloo Ramulaa" , "Butta Bomma" , "Srivalli" , "Samajavaragamana"]
# locations = ["Hyderabad" , "Bangalore" , "Chennai" , "Mumbai" , "Delhi"]
leaders = ["Josheph Vijay" , "Pawan Kalyan" , "Stalin" , "Rajinikanth" , "Narendra Modi"]

# print("Playlist: ", playlist)
# print("Locations: ", locations)
# print("Leaders: ", leaders)

# playlist.append("Thalapathi Kacheri")  # Add a new song to the playlist
# print("Updated Playlist: ", playlist)  # Print the updated playlist

# playlist.remove("Butta Bomma")  # Remove a song from the playlist
# print("Updated Playlist after removal: ", playlist)  # Print the updated playlist after removal

# playlist.reverse()  # Reverse the order of songs in the playlist
# print("Reversed Playlist: ", playlist)  # Print the reversed playlist

# playlist.pop()  # Remove the last song from the playlist
# print("Updated Playlist after popping the last song: ", playlist)  # Print the updated playlist

# print( "Samajavaragamana is in position" ,playlist.count("Samajavaragamana"))  # Print the number of songs in the playlist


# #List Slicing

# print("Top 3 songs in the playlist:" , playlist[0:3])  # Print the first three songs in the playlist

# print("Last 2 songs in the playlist:" , playlist[-2:])  # Print the last two songs in the playlist

# #List iteration

# for place in locations:
#     print("Location:", place)  # Print each location in the list

# #Check if an item exists in the list

# if "Mumbai" in locations:
#    print("Mumbai is in the list of locations.")  # Print a message if Mumbai is in the list
# else:
#     print("Mumbai is not in the list of locations.")  # Print a message if Mumbai is not in the list

# #update the list via index

# locations[1] = "Pune"  # Update the second location in the list
# print("Updated Locations: ", locations)  # Print the updated list of locations

#enumerate is used to get the index and value of each item in the list during iteration

for i, leader in enumerate(leaders):
    print(f"Leader {i}: {leader}")  # Print the index and name of each leader in the list