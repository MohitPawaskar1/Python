'''
                     Recursive Function
                        │
         ┌──────────────┴──────────────┐
         │                             │
   Base Case                    Recursive Case
         │                             │
  Stops recursion            Calls itself with 
  and returns a value        a smaller problem
         │                             │
      Output                       Recursive Call  
                                        │
                        ┌───────────────┴───────────────┐
                        │                               │
                 Base Case                        Recursive Case
                        │                               │
                  Stops recursion                Calls itself again...

'''

# Factorial

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a  number: "))
print(f"The factorial of {n}: {factorial(n)}")