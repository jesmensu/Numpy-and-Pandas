from numpy import random

# Random means something that can not be predicted logically.
x = random.randint(100)     # Generate a random integer from 0 to 100
x = random.rand()           # Generate a random float from 0 to 1
x=random.randint(100, size=(5)) # Array of size 5 
x = random.randint(100, size=(3, 5))
x = random.rand(5)
x = random.choice([3, 5, 7, 9])   # Any value from the array
x = random.choice([3, 5, 7, 9], size=(3, 5))
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
x = random.permutation([1, 2, 3, 4, 5])