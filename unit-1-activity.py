# Unit 1 Activity
# Author: Chiune Honda
# March 4 2024

# Define function and make function remove unnecessary text and create lower case for the user's input

def better_input(prompt):
    return input(prompt).strip(" .,?!").lower()

print()

print("Hello mysterious user....")
print()

print("My name is TAC, it does not matter who you are, what your name is. You are here to learn extremely valuable information from me.")
print()


# If user wants to know their input will be stripped so their answer will be a lower case yes or no with zero extra punctation

yes_no = better_input(f"But first, would you like to know the phrase that my name was abbreviated from? (Yes/No) " )
print()
if yes_no == "no":
    print( "Alright then.")
if yes_no == "yes":
    print("Alright, good to hear, the phrase behind TAC is, Time Asleep Calculator 😴")


# Make sure to get rid of decimals if the user gives them

print()
sleep = float(better_input("Hmmmmmmmm, and on average, how many hours do you sleep a night? "))
print()

# Take the hours they sleep and use mathematics to find the percentage, then round to 2 decimals

sleep_age = (sleep / 24 * 100)
print(f"ALrighty, so, with your current sleep habits, you will spend %{round(sleep_age, 2)} of your precious life asleep.")

print()
print("Although that sounds scary, as the ultimate sleep calculator, I suggest to never minimize sleep, sleep is ridcoulously important for our physical and mental health.")
print()
print("Thanks for you time!")
print()