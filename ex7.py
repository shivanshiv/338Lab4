# ENSF 338 Lab 4 Exercise 7
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def get_size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def get_element_at_pos(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    # Original code
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
        if newhead is None:
            newhead = currNewNode
        else:
            prevNode.next = currNewNode
            prevNode = currNewNode
            self.head = newhead

    # Optimized version
    def optimized_reverse(self):
        prevNode = None
        currNode = self.head
        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode

# Timing Comparison for Both Methods
sizes = [1000, 2000, 3000, 4000]
reverse_times = []
optimized_reverse_times = []

for size in sizes:
    linked_list = LinkedList()
    for i in range(size):
        linked_list.append(i)

    time_reverse = timeit.timeit(linked_list.reverse, number=100)
    reverse_times.append(time_reverse)

    time_optimized_reverse = timeit.timeit(linked_list.optimized_reverse, number=100)
    optimized_reverse_times.append(time_optimized_reverse)

# Plotting Results
plt.figure(figsize=(10, 5))
plt.plot(sizes, reverse_times, label='Original Reverse', marker='o')
plt.plot(sizes, optimized_reverse_times, label='Optimized Reverse', marker='o')
plt.title('Execution Time of Reverse Methods')
plt.xlabel('List Size')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.grid()
plt.show()

