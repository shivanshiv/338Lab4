# ENSF 338: Lab 4 Exercise 3

'''
3.1) The strategy that is used to grow the arrays in the code is over-allocation. The following approach helps to minimize the number of memory allocations that are required as the list grows. Hence, this helps to improve performance during operations-- such as appending elements.

The function list_resize checks if the current allocated size is sufficient to accommodate the new size. If current allocated size ('allocated') is greater than 'new size', it updates the size without reallocating memory.
    if (allocated >= newsize && newsize >= (allocated >> 1)) {
        assert(self->ob_item != NULL || newsize == 0);
        Py_SET_SIZE(self, newsize);
        return 0;
    }
    
The code calculates a new allocation size for the array that is larger than the requested size. The growth pattern is designed to be sufficient in order to accommodate future growth:
    new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
    
The code also includes adjustment for any sort of over-allocation. If the new size is closer to the previously allocated size, then the allocation size is adjusted accordingly.
    if (newsize - Py_SIZE(self) > (Py_ssize_t)(new_allocated - newsize))
    new_allocated = ((size_t)newsize + 3) & ~(size_t)3;
    
After finding the new size, the code performs memory allocation for the array.
    items = (PyObject **)PyMem_Realloc(self->ob_item, num_allocated_bytes);

Growth Factor Calculation:
    The code that resizes the list can be found in the line:
        new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
    Essentially, newsize >> 3 adds 12.5% of the current size into the new size. 
    new_allocated can be simplified to:
        new_allocated = new_size + (new_size / 8) + 6
                    = new_size * (1 + 1/8) + 6
                    = new_size * (1.125) + 6
    For larger values of new_size, the impact of constant 6 becomes less significant. Therefore, expressed as a decimal, the growth factor can be indicated by the value 1.125.

'''


import sys
import timeit
import matplotlib.pyplot as plt

# 3.2) Test Code for List Growth
test_list = []
previous_capacity = 0

for i in range(64):
    test_list.append(i)
    current_capacity = sys.getsizeof(test_list)
    
    if current_capacity != previous_capacity:
        print(f"Capacity changed: {previous_capacity} bytes to {current_capacity} bytes after adding {i}")
        previous_capacity = current_capacity
        
        
# 3.3) Measuring Time to Grow the Array
def measure_append_time(lst, iterations=1000):
    return timeit.timeit(lambda: lst.append(None), number=iterations) / iterations

S = len(test_list)  
time_to_grow_S_to_S_plus_1 = measure_append_time(test_list.copy()) 
print(f"Average time to grow from size {S} to {S+1}: {time_to_grow_S_to_S_plus_1:.10f} secs.")

test_list = list(range(S - 1))
time_to_grow_S_minus_1_to_S = measure_append_time(test_list.copy())
print(f"Average time to grow from size {S-1} to {S}: {time_to_grow_S_minus_1_to_S:.10f} secs.")


# 3.4) Plotting Distribution
times_S_to_S_plus_1 = []
times_S_minus_1_to_S = []

for _ in range(1000):
    times_S_to_S_plus_1.append(measure_append_time(test_list.copy()))
    test_list = list(range(S - 1))
    times_S_minus_1_to_S.append(measure_append_time(test_list.copy()))


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(times_S_to_S_plus_1, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Distribution of Time to Grow from S to S+1')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(times_S_minus_1_to_S, bins=30, alpha=0.7, color='red', edgecolor='black')
plt.title('Distribution of Time to Grow from S-1 to S')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


'''
3.5) 
Differences in time measurements:
    Expanding a list from size S to S+1 often takes longer time than from S-1 to S, especially if S is the point where the list's capacity was last increased. 
    This happens because adding an element at S+1 typically requires allocating more memory. On the other hand, adding at S-1 might not trigger a resize.
    
Distribution shape:
    When we plot the time measurements, the S to S+1 operation (involves memory reallocation) shows a longer tail / skewed distribution. This means that some operations take significantly more time. 
    On the other hand, the S-1 to S operation (no memory reallocation) has a more consistent and compact distribution.

'''
