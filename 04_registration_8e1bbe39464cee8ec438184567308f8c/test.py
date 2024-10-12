import itertools
import string
import os
from subprocess import run

# Using system() method to
# execute shell comm


def generate_combinations():
    # Get all printable characters
    printable_characters = string.printable
    
    # Generate all 4-letter combinations
    combinations = itertools.product(printable_characters, repeat=4)
    print(combinations)
    # Convert combinations to a list of strings
    result = [''.join(combination) for combination in combinations]
    
    return result

# Example usage
if __name__ == "__main__":
    combinations = generate_combinations()
    print(f"Total combinations: {len(combinations)}")
    # Uncomment the next line to print all combinations (be cautious, as this will be a large outputi)
    for i in combinations:
        print("trying" ,i)
        result = run(['./04_chall'], text = True, input=i, capture_output=True)
        if 'bye' not in result.stdout:
            exit()
