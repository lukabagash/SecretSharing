import random
import time

def generate_random_integers(n, lower_bound=1, upper_bound=100000):
    """
    Generate a list of n random integers between lower_bound and upper_bound.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

def measure_runtime(func, repetitions=2):
    """
    Measure the runtime of a function.
    """
    def wrapper(*args, **kwargs):
        total_time = 0
        for _ in range(repetitions):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time += (end_time - start_time)
        average_runtime = total_time / repetitions
        return result, average_runtime
    return wrapper


def save_to_file(data, filename):
    """
    Save a list of integers to a file.
    """
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")

