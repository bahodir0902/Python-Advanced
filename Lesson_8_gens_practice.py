def gen_10_nums():
    for i in range(10):
        yield i

def gen_item_from_nested_list(lst: list[list] | tuple[tuple]):
    for i in lst:
        if isinstance(i, list | tuple):
            for j in i:
                yield j
        else:
            yield i


"""
Absolute Zero (Beginner)
Understanding Generators Basics:

Write a generator function that yields the first 10 natural numbers.
Create a generator that yields squares of numbers from 1 to 10.
Using yield:

Write a generator that yields the characters of a given string one by one.
Create a generator that yields items from a list, one by one, until it encounters the value "STOP".
Iterating Over Generators:

Write a generator that produces numbers from 1 to 5. Iterate over it using a for loop and print each number.
Warm-up (Intermediate)
Infinite Generators:

Write a generator that produces an infinite sequence of even numbers starting from 0.
Generator with Conditional Logic:

Write a generator that yields only odd numbers from a list.
Using yield and yield from:

Write a generator that yields all items of nested lists (e.g., [1, [2, 3], 4] -> 1, 2, 3, 4).
Fibonacci Sequence:

Implement a generator for the Fibonacci sequence up to a given number of terms.
Challenge (Advanced)
Prime Number Generator:

Custom Range Generator:

Implement a generator function that mimics Python’s range() function, supporting step and negative ranges.
Pipeline Generators:

Combine multiple generators to create a pipeline. For example:
A generator produces numbers from 1 to 100.
A second generator filters out multiples of 3.
A third generator squares the remaining numbers.
Memory Efficiency:

Generate the first 10 million numbers using a generator and demonstrate its memory efficiency compared to a list.
Insane (Hell Level)
File Processing with Generators:

Write a generator that reads a large text file line by line and yields only lines containing a specific keyword.
Parallel Generators:

Use two generators to produce numbers and their squares simultaneously (e.g., 1, 1, 2, 4, 3, 9).
Generator Comprehension:

Write a generator comprehension that calculates the sum of squares of numbers from 1 to 1,000,000.
Async Generators (Python 3.6+):

Write an asynchronous generator that yields numbers with a delay (e.g., async for x in generator()).
Simulate Infinite Streams:

Create a generator that mimics a live data stream (e.g., random sensor readings) and stops based on a user-defined condition.
Advanced Data Processing Pipeline:

Build a generator pipeline for processing a CSV file:
Read the file line by line.
Parse each line into a dictionary.
Filter rows based on a condition.
Yield only the required columns.
Recursive Generator:

Write a recursive generator to traverse a deeply nested dictionary and yield all key-value pairs.
Generator Debugging Tool:

Create a decorator that logs the values being yielded by a generator function.
Combinatorial Generator:

Write a generator that produces all possible combinations of a given list of items (e.g., ['A', 'B', 'C'] -> AB, AC, BC).
"""

