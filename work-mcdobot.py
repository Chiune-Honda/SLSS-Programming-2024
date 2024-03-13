# McDoBot
# Author: Chiune
# Feb 21 2024

answer = input("Would like fries with your mean? (Yes/No) ").strip(" .,?!").lower()

if answer.strip().lower() == "yes":
    print("Alright, here's your meal with fries!")

elif answer.strip().lower() == "no":
    print("Ok, here's your fryless meal.")

else:
    print(f"{answer}? Sorry I don't understand that, please try again.")