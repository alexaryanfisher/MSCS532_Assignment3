"""
Assignment 3: Randomized Quicksort, Part 1

Randomized Quicksort implementation in Python.
This implementation uses a randomized quicksort algorithm to sort an array where the pivot is chosen randomly.

"""

import random
import time # For performance testing.

# Sorts the array using randomized quicksort.
def randomized_quicksort(arr):
     # Handle edge case: If the array is empty or has one element, it is already sorted.
    if len(arr) <= 1:
        return

    # Recursive  helper function for randomized quicksort.
    _recursive_randomized_quicksort(arr, 0, len(arr) - 1)

def _recursive_randomized_quicksort(arr, low, high):
    if low < high:
        # Partition the array and get pivot final position.
        pivot_index = _partition_random(arr, low, high)
        # Recursively sort subarray around the pivot.
        _recursive_randomized_quicksort(arr, low, pivot_index - 1)
        _recursive_randomized_quicksort(arr, pivot_index + 1, high)

def _partition_random(arr, low, high):
        #Choose a random pivot index between low and high.
        pivot_index_random = random.randint(low, high)
        # Swap the pivot with the last element.
        arr[pivot_index_random], arr[high] = arr[high], arr[pivot_index_random]
        return _partition(arr, low, high)

def _partition(arr, low, high):
     # Pivot element. ( Randomly chose and swapped with last element.)
     pivot = arr[high]
     # Index of smaller element.
     i = low - 1 

     #Iterate through the array from low to high - 1.
     for j in range(low, high):
         # If current element (j) is smaller than or equal to pivot.
         if arr[j] <= pivot:
             # Increment index of smaller element.
             i += 1
             # Swap the current element (j) with the element at index (i).
             arr[i], arr[j] = arr[j], arr[i]
    
     # Put the pivot element in its correct position.
     arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
     # Return the index of the pivot element.
     return i + 1

# Use and Edge Cases
print(" Use Cases for Randomized Quicksort")

# Use Case 1 : Repeated Elements
print("\nUse Case: Repeated Elements")
# Array with repeated elements.
arr1 = [3, 6, 5, 2, 6, 1]
print("Original array: ", arr1)
# Measure the time taken to sort the array.
# Start the timer.
start_time = time.perf_counter()
randomized_quicksort(arr1)
# End the timer.
end_time = time.perf_counter()
# Elapsed time in seconds.
elapsed_time = end_time - start_time
# Convert to milliseconds.
elapsed_time_ms = elapsed_time * 1000
print("Sorted array: ", arr1)
print(f"Execution Time: {elapsed_time_ms} ms")

# Use Case 2 : Empty Array
print("\nUse Case: Empty Array")
# Empty array.
arr2 = []
print("Original array: ", arr2)
start_time = time.perf_counter()
randomized_quicksort(arr2)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
elapsed_time_ms = elapsed_time * 1000
print("Sorted array: ", arr2)
print(f"Execution Time: {elapsed_time_ms} ms")

# Use Case 3 : Already Sorted Array
print("\nUse Case: Already Sorted Array")
# Already sorted array.
arr3 = [1, 2, 3, 4, 5, 6]
print("Original array: ", arr3)
start_time = time.perf_counter()
randomized_quicksort(arr3)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
elapsed_time_ms = elapsed_time * 1000
print("Sorted array: ", arr3)
print(f"Execution Time: {elapsed_time_ms} ms")

# Use Case 4 : Single Element Array
print("\nUse Case: Single Element Array")
# Array with a single element.
arr4 = [20]
print("Original array: ", arr4)
start_time = time.perf_counter()
randomized_quicksort(arr4)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
elapsed_time_ms = elapsed_time * 1000
print("Sorted array: ", arr4)
print(f"Execution Time: {elapsed_time_ms} ms")

# Use Case 5 : Randomly Generated Array
print("\nUse Case: Randomly Generated Array")
# Randomly generated array.
arr5 = [random.randint(1, 100) for _ in range(6)]
print("Original array: ", arr5)
start_time = time.perf_counter()
randomized_quicksort(arr5)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
elapsed_time_ms = elapsed_time * 1000
print("Sorted array: ", arr5)
print(f"Execution Time: {elapsed_time_ms} ms")

# Use Case 6 : Reverse Sorted Array
print("\nUse Case: Reverse Sorted Array")
# Reverse sorted array.
arr6 = [6, 5, 4, 3, 2, 1]
print("Original array: ", arr6)
start_time = time.perf_counter()
randomized_quicksort(arr6)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
elapsed_time_ms = elapsed_time * 1000
print("Sorted array: ", arr6)
print(f"Execution Time: {elapsed_time_ms} ms")

# Use Case 7 : Large Array (Performance Testing)
print("\nUse Case: Large Array (Performance Testing)")
# Large array with random integers.
arr7 = [random.randint(1, 1000) for _ in range(1000)]
print("Original array (Showing first 15 elements): ", arr7[:15], "...")
start_time = time.perf_counter()
randomized_quicksort(arr7)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
elapsed_time_ms = elapsed_time * 1000
print("Sorted array (Showing first 15 elements): ", arr7[:15], "...")
print(f"Execution Time: {elapsed_time_ms} ms")