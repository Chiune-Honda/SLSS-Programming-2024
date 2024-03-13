#
# Author: Chiune
# Feb 21 Feburary

# Ask the user what the weather is
user_reply = input("What is the weather like?")

# If th ey answer rainy, say
# bring an umbrella
if user_reply.strip().lower() == "rainy":
    print("Bring an umbrella!")
else:
    print("Bruh")