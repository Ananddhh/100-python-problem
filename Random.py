import random

Num = random.randint(1,6)

print(Num)

# Example: Generate a code with a prefix and a random number
import string

def generate_custom_code(prefix, length=4):
    random_number = ''.join(random.choices(string.digits, k=length))
    return prefix + random_number

# Generate a custom code
custom_code = generate_custom_code("ABC")
print(custom_code)

