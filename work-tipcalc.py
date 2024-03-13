# Tip Calc
# Author: Chiune Honda
# Feb 28 2024

def main():
    meal_price = dollars_to_float(input("How much was the meal? "))
    dollars = dollars_to_float(meal_price)
    tip_price = input("What percentagae would you like to tip? ").strip(" %$!/")  
    percent = percent_to_float(tip_price)  
    total_cost = dollars * (1 + percent / 100)
    print(f"Your total cost is ${round(total_cost, 2)}")

def dollars_to_float(d):
   number = float(d)
   return number

def percent_to_float(p):
   number = float(p)
   return number

main()
