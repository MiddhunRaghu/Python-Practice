Passenger_name="Middhun Raghunathan"

mobile_number="1234567890"
masked_number=mobile_number[:1]+"********"+mobile_number[-1:] #masking the mobile number except for the first and last digit
print("Passenger Name:", Passenger_name)
print("Mobile Number:", masked_number)
initials="".join([name[0].upper() for name in Passenger_name.split()]) #extracting the initials from the passenger name
print("Initials:", initials)

song = "karrupare vaarumaiya"
artist = "sai abayankar"
forrmatted = f"song: {song.title()} by {artist.title()}" #formatting the string using f-string
print(forrmatted)

location = "chennai"
print(location.replace("chennai", "Erode").title()) #replacing the string and formatting it to title case

message = "Your Uber booking id is , UBE202606. Driver will arrive in 5 minutes. Please be ready."

booking_id = message.split(",")[1].strip().split(".")[0] #splitting the string to extract the booking id
print("Booking ID:", booking_id)

promo_message = "Use code UBER50 to get 50% off on your next ride."

if "UBER50" in promo_message:
    print("Offer applied successfully!") #checking if the promo code is present in the message
else:
    print("Invalid promo code.")

feedback = "The driver was very friendly and the ride was smooth."
print("position is:", feedback.find("friendly")) #finding the position of the word "friendly" in the feedback message

print("Length of feedback:", len(feedback.split())) #finding the length of the feedback message
