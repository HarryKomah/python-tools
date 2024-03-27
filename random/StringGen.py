import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_numbers(length):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))

def generate_random(list_string, length):
    return ''.join(random.choice(list_strings) for _ in range(length))


# Example usage:
random_string = generate_random_string(10)

random_str = generate_random(['a', 'b', 'c'], 2)

print(random_string)
print(random_str)

