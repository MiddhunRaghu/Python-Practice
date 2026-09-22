# a = 5
# b = 5

# print (a + b)  # Addition

# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))

# print(x + y)  # Addition


import sys

full_name = " ".join(sys.argv[1:])

print("Hello", full_name)

email = full_name.lower().replace(" ", ".") + "@example.com"

print("Your email is:", email)  
