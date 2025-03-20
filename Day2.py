#  Implement Bubble Sort from Scratch
def bubble_sort(arr):
    n = len(arr) 

    for i in range(n-1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                temp = []
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [1,9,5,7,6,8,3,4,2]
bubble_sort(arr)
print(arr)


# Implement Quick Sort from Scratch
def Quick_sort(arr):
    if len(arr) < 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return Quick_sort(left) + middle + Quick_sort(right)

arr = [1,5,9,7,6,3,4,8,2]
sorted_arr = Quick_sort(arr)
print(arr)
print(sorted_arr)



# WAF to search for a number in a sorted list
def binary_search(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) //2

        if arr[mid] == target:
            print("Found at index", mid)
            break
        elif arr[mid] < target:
            low = arr[mid]+1
        else: 
            high = arr[mid]-1

arr = [1,2,3,4,5,6,7,8,9]
target = 5
binary_search(arr, target)


# Implement a stack using a python list with Push, Pop & Peek operation.
class Stack():
    def __init__(self):
        self.values = []

    def push(self, x):
        self.values = [x] + self.values

    def pop(self):
        return self.values.pop(0)
    
    def peek(self):

            return self.values[-1]
        
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.values)
s.pop()
print(s.values)
print("Peek:", s.peek()) 