import time
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def get_middle(self, start, end):
        slow = fast = start
        prev = None
        while fast != end and fast.next != end:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev, slow
    
    def binary_search(self, num):
        start, end = self.head, None
        while start != end:
            prev, middle = self.get_middle(start, end)
            if middle is None:
                return False
            if middle.value == num:
                return True
            elif middle.value < num:
                start = middle.next
            else:
                end = middle
        return False

class Array:
    def __init__(self, values):
        self.data = values
    
    def binary_search(self, num):
        low, high = 0, len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == num:
                return True
            elif self.data[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return False

# Complexity Analysis:
# Binary search on an array has O(log n) complexity since we can access elements in O(1) time.
# Binary search on a linked list takes O(n) to find the middle element and O(log n) iterations, leading to O(n) complexity overall.

def measure_time(search_structure, values, target):
    start_time = time.time()
    search_structure.binary_search(target)
    return (time.time() - start_time) * 1000  # Convert to ms

sizes = [1000, 2000, 4000, 8000]
linked_list_times = []
array_times = []

target = -1  # Worst case scenario (not in the list)

for size in sizes:
    values = list(range(size))
    
    linked_list = LinkedList()
    for v in values:
        linked_list.append(v)
    array = Array(values)
    
    linked_list_times.append(measure_time(linked_list, values, target))
    array_times.append(measure_time(array, values, target))

plt.plot(sizes, linked_list_times, label='Linked List', marker='o')
plt.plot(sizes, array_times, label='Array', marker='s')
plt.xlabel('Input Size')
plt.ylabel('Time (ms)')
plt.legend()
plt.title('Binary Search Performance: Linked List vs Array')
plt.show()
