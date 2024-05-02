import random

Num = random.randint(1,6)

print(Num)

# Example: Generate a code with a prefix and a random number
def generate_custom_code(prefix, length=4):
    random_number = ''.join(random.choices(string.digits, k=length))
    return prefix + random_number

# Generate a custom code
custom_code = generate_custom_code("ABC")
print(custom_code)


import random
import string

def generate_alphanumeric_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# Generate an alphanumeric code
alphanumeric_code = generate_alphanumeric_code()
print(alphanumeric_code)
