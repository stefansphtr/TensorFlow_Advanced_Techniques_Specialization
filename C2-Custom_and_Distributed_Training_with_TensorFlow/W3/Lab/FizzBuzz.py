#!/usr/bin/env python

import tensorflow as tf

# Write fizzbuzz code

@tf.function
def fizzbuzz(max_num):
    counter = 0
    for num in range(max_num):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
    counter += 1
    return counter

# Create fizzbuzz with maximum number of 100
result = fizzbuzz(10)

print(f"The fizzbuzz function was called {result} times.")