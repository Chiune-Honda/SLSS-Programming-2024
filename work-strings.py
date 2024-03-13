
# Author: Chiune Honda
# Date: Feburary 14th 2024

name = "Chiune"
location = "SLSS"

# Question 1
# Greets the user and asks them how their day is going so far

print()
print("DISCLAIMER: Please remember to answer all questions using a capial for the first letter")
print()
print("Hello, user!")
print()
print("I'm going to ask you a question...")
print()
print("How is your day going so far?")
print()

input()

# Answers with "Wow, thanks for sharing" then asks for the user's name and welcomes them

print("Wow, thanks for sharing!")
print()

print("So, what's your name?")
print()

user_name = input()
print()
print(f"It's really nice to meet you {user_name}!")
print()

# Question 2

print("For my second question, what's your favourite sport to play or watch?")
print()

sport = input()

print()
if sport == "Soccer":
    print("That's awesome, soccer is my favourite as well")


else:
    print(f"Hmm, {sport} is a good choice, but me, I love soccer")


# Question 3

print()
print("Alright, last question, who's your favourite artist?")
print()

musician = input()

print()
if musician == "Drake":
    print("How do you spell CANADA!!?? D, R, A, K, E")


else:
    print(f"Great choice! I love {musician} as well, but for me Drake has to be there.")

print()
print(f"Alright, nice talking to you, {user_name}, good bye!")
print()