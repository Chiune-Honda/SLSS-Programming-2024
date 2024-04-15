# Classes and Objects

# Big IDeas:
#     -Classes aloow us to couple data and functins together
class Pokemon: # alawys name classes with capital 
    def __init__(self):
        """Constrctor: contains all properties
        of a Pokemon. It also contains the default stage of the properties.
        """
        self.name = ""
        self.id = 0
        self.weight= 0 
        self.type = "Normal"

def main ():
    # Create two Pokemon

    # Create something 'Pikachu'-like
    pokemon_one = Pokemon()
   
   # Access the properties inside pokemon_one

    # Change the value of the properties
    pokemon_one.name = "Pikachu"
    pokemon_one.type = "Electric"
    pokemon_one.id = 25
    # Print the name of pokemon_one
    print(pokemon_one.name)
    print(pokemon_one.type)
    print(pokemon_one.id)


# Create something 'Squirtle'-like

# TODO: Create something 'Squirtle'-like
    #  - Create a new Pokemon object
    #      - Store this in variable pokemon_two
    #  - Squirtle's Pokedex id is 4
    #  - Squirtle's type is Water
    # To test, print out all of squirtle's properties

    pokemon_two = Pokemon()
    pokemon_two.name = "Squritle"
    pokemon_two.type = "Water"
    pokemon_two.id = 4
    print(pokemon_two.name)
    print(pokemon_two.type)
    print(pokemon_two.id)

if __name__ == "__main__":
    main()