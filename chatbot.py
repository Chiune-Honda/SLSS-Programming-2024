# Chatbot
# Author: Chiune
# March 8

# 1. Greets the user
print("Hello there!")

# 2. Asks them, "how are you?" or something like it
print("How are you doing?")
user_feeling = input.strip( ".,?! ").lower()

# 3. Responds with a general statement
if user_feeling == "good" or user_feeling == "great":
    print("That's awesome!")
elif user_feeling == "bad" or user_feeling == "not too good":
    print( "I'm sorry that you're feeling that way.")

# 4. Says goodbye
    
print("Well thank you for your time!")

