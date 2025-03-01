**ENSF 338: Lab 4 Exercise 7**

1. When you look at the outer loop, it iterates from 'self.get_size - 1' to '0'. This means that it will run 'n' times, where 'n' is the size of the linked list. Then, the method 'self.get_element_at_pos(i)' is called inside the loop. Since it is a singly linked list, this has a time complexity O(n)-- as may need to traverse the list to find the element. Creating a new node for a linked list (currNewNode = Node(currNode.data)) has a complexity O(1). Similarly, the linking operation (prevNode.next = currNewNode) also has complexity O(1). Adding all these complexities together: 
        
        O(n) (from for loop) * O(n) (from self.get_element_at_pos(i)) + O(1) + O(1)
        = O(n^2)

2. Instead of creating new nodes, we reverse the links between the existing nodes. This reduces any sort of memory usage-- avoiding the creation of new node objects. Additionally, the optimized implementation only requires a single pass through the list. This results in a time complexity of O(n)-- hence being more efficient than the previous implementation.
