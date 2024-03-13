# Lists and Modules
# Author: Ubial 
# March 8

import random

def coin_flip():
    # Return heads or tails or other?
    # Heads is any number 0 to 0.499999999
    # Tails is any number from 0.5 to 0.9999999991
    # Other is any number greater than 0.99999991
    roll = random.random()

    if roll < 0.5:
        return 'Heads'
    elif roll < 0.9999991:
        return "tails" 
    else:
        return "other?"
    
    def main():
        # Repeat 100 times
        for _ in range(100):
            if coin_flip() == "heads":
    

main()