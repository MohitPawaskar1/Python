# WAP to reverse a string without using inbuilt function

string = "BGMI"
reverse_string = string[::-1]
print(reverse_string)

def reversed_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

s = "BGMI"
print(reversed_string(s))



# WAP implement a class Employee with attributes like name, salary, methods to compute annual salary

class Employee():
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12


e1 = Employee("Mohit", 200000)
print(e1.annual_salary())
print(f"The Employee {e1.name}, His monthly INHand Salary is RS.{e1.salary} and His annual Income is Rs.{e1.annual_salary()}")


# find the second largest number in a list without using max() twice

def sec_lar(lst):
    unique_list = list(set(lst))
    unique_list.sort(reverse=True)
    return unique_list[1] if len(unique_list) > 1 else None

lst = [10,20,30,40,10,50]
print(sec_lar(lst))