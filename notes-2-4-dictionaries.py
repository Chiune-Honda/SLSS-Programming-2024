# Dictionaries
# 12 April 2024

# Big Ideas:
#    - dictionaries are a data strucuture
#    - dictionaries map keys to values


# Flashback to lists
person = ["John","23 years old", "4500 1023 2222 1111"]


person_dict = {
    "name": "John",
    "age": "23 years old",
    "credit card number": "4500 1023 2222 1111",
    "dog's name": "Joseph",
    "Favourite food": "Pizza"
}


# Get and print the person's name

print(person[0])
print(person[1])
print(person[2])
print(person_dict["name"])
print(person_dict["age"])
print(person_dict["credit card number"])
print(person_dict)["dog's name"]
print(person_dict)["Favourite food"]

# Print the last thing in the list
print(person[-1])
print(person[-2])
 
for value in person_dict:
    print(value)