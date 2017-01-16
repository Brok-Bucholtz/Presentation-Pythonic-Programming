import numpy as np
from random import random


def add_random(x):
    return x + random()

# How do I find out what random is?
example_list = [1, 2, 3, 4, 5]
for example in example_list:
    if add_random(example) in example_list:
        example_list.remove(example)

print(example_list)


# Why is it false?
example_ndarray = np.array([[1, 2, 3, 0, 5], [6, 7, 8, 9, 10]])
print(np.alltrue(example_ndarray))
