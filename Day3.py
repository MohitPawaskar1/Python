# Write a generotr function to generate Fibonacci numbers up tp n.
def fibonacci_serires(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b

print(list(fibonacci_serires(12)))


# Implement a decorator that logs function execution time

import time
import logging

logging.basicConfig(level=logging.INFO)

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"{func.__name__} executed in {execution_time: .6f} seconds ")
        return result
    return wrapper

@log_execution_time
def slow_function():
    time.sleep(2)
    return "Done!"

print(slow_function())

# Read a large file line by line without loading it into memory

def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line

for line in read_large_file("Day1.py"):
    print(line.strip())

