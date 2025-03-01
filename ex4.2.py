import numpy as np
import matplotlib.pyplot as plt
import timeit

# 3)
# Inefficient Implementation: Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1

# Efficient Implementation: Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

'''
4) Linear Search Worst Case Complexity: O(n)
    - This occurs when the target is not present in the array, or when it is at the last position.
    
   Binary Search Worst Case Complexity: O(log n)
    - This occurs when the search space is halved at each step. This leads to logarithmic time complexity.
'''

# 5)

# 5.1) Timing the execution
n = 1000
sorted_array = np.arange(n) 
target = n + 1  

def measure_linear_search():
    return timeit.timeit(lambda: linear_search(sorted_array, target), number=1)

def measure_binary_search():
    return timeit.timeit(lambda: binary_search(sorted_array, target), number=1)

linear_search_times = []
binary_search_times = []

num_measurements = 100
for _ in range(num_measurements):
    linear_search_times.append(measure_linear_search())
    binary_search_times.append(measure_binary_search())

# 5.2) Plotting distribution
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(linear_search_times, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Distribution of Linear Search Times')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(binary_search_times, bins=30, alpha=0.7, color='red', edgecolor='black')
plt.title('Distribution of Binary Search Times')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()