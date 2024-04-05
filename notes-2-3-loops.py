# Loops and Iteration
# Author: Chiune
# April 5

# Print "something" 10 times

for _ in range(100000):
    print("balls")

# Print out every item in my grocery list
grocery_list = [
    "dishwaser tabs",
    "balls",
    "balls v2",
    "balls"
]
# Stip if we reach blueberry muffins

for item in grocery_list:
    print("------")
    print(f"* {item}")

    if item== "balls":
        break

# Count form 0 to 9
for i in range(1000) :
   print(i)
   
    # Modulo
if i % 2 == 0:
    print(f"{i} is an even number")

# Rewrtie the above for loop as a while loop
counter = 0

while counter < 1000:
    if counter % 2 == 0:
        print(f"{counter} is an even number")
else:
    print(counter)
    counter += 1

    # increment by 1 
    # counter = counter + 1 