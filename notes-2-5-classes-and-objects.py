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
        self.actual_cry = "Rooooooooooooar"


    def cry(self) -> str:
        """Represents the noise a Pokemon makes

        Returns:
            -As a string the sound a pokemon makes
            -e.g, "{name} says, "{actual_cry}"""
        return f'{self.name} says, "{self.actual_cry}!"'
    def consume(self, item: str) -> str:
        """Pokemon cosumes the item
        
        Params:
            - the item the pokemon consumes
            
        Retruns:
            - the response of the pokemon
            """
        if item.lower() == "berry":
            return f"{self.name} eats the berry and says, \"YUM\""
        elif item.lower() == "potion":
            return f"{self.name} feels much better after the potion!"
        else:
            return f"{self.name} batted away the {item}!"

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

    # Test Pokemon Cry
    print(pokemon_one.cry())
    print(pokemon_two.cry())

    # Test Pokemon consume
    print(pokemon_one.consume("berry"))
    print(pokemon_one.consume("potion"))
    print(pokemon_one.consume("Poision"))

if __name__ == "__main__":
    main()