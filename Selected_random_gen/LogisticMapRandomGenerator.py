# Exercise 14.10
import time


def generate_random_numbers(n):
    r = 4
    res = []
    # Use the current time as the seed
    x = time.time() % 1  # We use modulo 1 to ensure the seed is in the range [0, 1), which is the valid range for the logistic map
    for i in range(n):
        x = r * x * (1 - x)
        res.append(x)
    return res


# Generate 5 random numbers
random_numbers = generate_random_numbers(5)
print(random_numbers)

# Generate 10 random numbers
random_numbers = generate_random_numbers(10)
print(random_numbers)


