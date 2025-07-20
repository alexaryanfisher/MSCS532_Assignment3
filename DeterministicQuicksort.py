"""
Assignment 3: Part 1 c: Comparison.

Deterministic Quicksort Implementation for Comparison with Randomized Quicksort
This implementation uses a deterministic quicksort algorithm ( first element as pivot) to sort an array and compares its performance with the randomized quicksort implementation.
This is useful for understanding the performance differences between deterministic and randomized approaches.

"""

import random
import time
import sys
from RandomizedQuicksort import randomized_quicksort
from RandomizedQuicksort import _partition



# Sort using deterministic quicksort, which is implemented in the same way as the randomized version but without randomization. Pivot selection is deterministic as first element, last element, or middle element.
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    _recursive_deterministic_quicksort(arr, 0, len(arr) - 1)

# Recursive helper function for deterministic quicksort.
def _recursive_deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = _partition_deterministic(arr, low, high)
        _recursive_deterministic_quicksort(arr, low, pivot_index - 1)
        _recursive_deterministic_quicksort(arr, pivot_index + 1, high)

def _partition_deterministic(arr, low, high):
    # Choose the pivot as the first element.
    pivot = arr[low]
    
    # Move the pivot to the end for partitioning.
    arr[low], arr[high] = arr[high], arr[low]

    # Calling  the standard partition function with the pivot at arr[high].
    return _partition(arr, low, high)

# Data Generation Functions
# Generate random large array.
def generate_random_array(size, max_value=10000):
    return [random.randint(1, max_value) for _ in range(size)]

# Generate sorted array.
def generate_sorted_array(size):
    return list(range(1, size + 1))

# Generate reverse sorted array.
def generate_reverse_sorted_array(size):    
    return list(range(size, 0, -1))

# Generate array with repeated elements for testing.
def generate_repeated_elements_array(size, unique_elements= 10):
    return [random.randint(1, unique_elements) for _ in range(size)]

# Performance Testing Function, Compare deterministic and randomized quicksort.
def comparsion(arr_type, size, unique_elements=None):
    if arr_type == "Random Array":
        orginal_arr = generate_random_array(size)
    elif arr_type == "Sorted Array":
        orginal_arr = generate_sorted_array(size)
    elif arr_type == "Reverse_sorted Array":
        orginal_arr = generate_reverse_sorted_array(size)
    elif arr_type == "Repeated_elements Array":
        orginal_arr = generate_repeated_elements_array(size, unique_elements)
    else:
        raise ValueError("Invalid array type specified.")

    # Deterministic Quicksort Testing
    # Copy the array to ensure both algorithms sort the same data.
    arr_deterministic = list(orginal_arr)

    # Measure time for deterministic quicksort.
    # Start time for deterministic quicksort.
    start_time_deterministic = time.perf_counter()
    deterministic_quicksort(arr_deterministic)
    end_time_deterministic = time.perf_counter()
    # End time for deterministic quicksort.
    end_time = time.perf_counter()
    # Elapsed time in seconds.
    elapsed_time_deterministic = end_time - start_time_deterministic
    # Convert to milliseconds.
    elapsed_time_deterministic_ms = elapsed_time_deterministic * 1000

    # Randomized Quicksort Testing
    # Copy the array to ensure both algorithms sort the same data.
    arr_randomized = list(orginal_arr)

    # Measure time for randomized quicksort.
    # Start time for randomized quicksort.
    start_time_randomized = time.perf_counter()
    randomized_quicksort(arr_deterministic)
    end_time_randomized = time.perf_counter()
    # End time for randomized quicksort.
    end_time = time.perf_counter()
    # Elapsed time in seconds.
    elapsed_time_randomized = end_time - start_time_randomized
    # Convert to milliseconds.
    elapsed_time_randomized_ms = elapsed_time_randomized * 1000

    print(f"Array Type: {arr_type}, Size: {size}")
    print(f"Randomized Quicksort Execution Time: {elapsed_time_randomized_ms} ms")
    print(f"Deterministic Quicksort Execution Time: {elapsed_time_deterministic_ms} ms")

# Main execution for performance testing.
if __name__ == "__main__":
    # Set recursion limit to handle large arrays.
    sys.setrecursionlimit(20000)

    # Test with different array types and sizes.
    sizes = [100, 1000, 5000, 10000, 15000]

    for size in sizes:
        # Print the size being tested.
        print(f"\nTesting with size: {size}")
        # Perform comparisons for different array types and noted sizes.
        comparsion("Random Array", size)
        comparsion("Sorted Array", size)
        comparsion("Reverse_sorted Array", size)
        comparsion("Repeated_elements Array", size, unique_elements=20)
        # Notify when comparison is done running.
        print(f"Comparison for size {size} completed.\n")