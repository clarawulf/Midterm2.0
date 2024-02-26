import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Replace numbers greater than 80 with their corresponding negative value
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]

# Print the list
print(random_numbers)
