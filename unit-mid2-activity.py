# Unit 2 Activity
# Chiune Honda
# April 10 2024

# Square root Exemplifier➗

import math

def calculate_square_root(num):
    return math.sqrt(num)


def main():
    print("Square roots of numbers from 1 to 1000:")
    for num in range(1, 1001):
        result = calculate_square_root(num)
        print("Square root of", num, "is:", result, "🤑")

if __name__ == "__main__":
    main()


