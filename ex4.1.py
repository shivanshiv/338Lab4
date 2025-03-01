# ENSF 338: Lab 4 Exercise 4

'''
1) 
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2
Best Case Complexity (O(n)): this occurs when none of the elements in the li are greater than 5. This means that if statement would not execute.
The outer loop runs 'n' times (n being the length of li), but the inner loop does not execute-- therefore making best case time complexity O(n).

Worst Case Complexity (O(n^2)): this occurs when all the elements in li are grater than 5. For each element, the inner loop will execute 'n' times.
The outer loop runs 'n' times, and for each iteration of the outer loop, the inner loop also runs 'n' times. This makes the worst case time complexity O(n^2).

Average Case Complexity (O(n^2)): this occurs if we assume that half of the elements are greater than 5. On average, we would still have a significant number of 
inner loop executions. The outer loop runs 'n' times, and for some iterations of the outer loop, the inner loop also runs 'n' times.
'''

# 2) The average, best, and worst case complexities are not the same. Here is a modified version of the code where the complexities are all equal:

def processdata(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2

'''
The inner loop runs for every element in the list, regardless of the value li[i].
This means that the inner loop will always execute 'n' times for each 'n' elements in the outer loop.
'''