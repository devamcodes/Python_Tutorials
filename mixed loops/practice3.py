"""
Project:
Author:Devam A

Discripition:i can use import function insted but just wanted to practice the use of lambda function but should try decorator if they can do the work

"""
"""name = input("PLEASE ENTER YOUR NAME:")
print(f"Hello, {name.title()}")
year = int(input("PLEASE ENTER YOUR AGE:"))
age = year * 12
print(f"YOUR AGE IS {age} MONTHS")
numbers = int(input("ENETR ANY NUMBER:"))
while(numbers != 0):
    f1 = input("ENTER FRIEND'S NAME")   
    friend = set()
    friend.add(f1)
    number = int(input("PLEASE ENTER 1 OR 0 NUMBER:"))
    numbers = number
    
f3 = input("ENTER NAME OF YOUR ONE FRIEND TO CHECK IF HE IS NEARBY")
nearby = set()
nearby.add(f3)
print(nearby.intersection(friend))
"""
number1 = int(input("ENTER ANY NUMBER:"))
number2 = int(input("ENTER ANY NUMBER:"))
PRODUCT = lambda number1,number2: number1*number2
SUBTRACTION = lambda number1,number2: number1-number2
ADDITION =lambda number1,number2: number1+number2
operations={
    "product":PRODUCT,
    "subtraction":SUBTRACTION,
    "addition":ADDITION
    }


user_input_option = ['PRODUCT', 'SUBTRACTION', 'ADDITION']
for a in range(len(user_input_option)):
    print(a,user_input_option[a])
user_input = input("ENTER PRODUCT,SUNBRTRACTION OR ADDITION:")
if user_input == "product":
        print (PRODUCT)
elif user_input == "subtraction":
       
        print(SUNBTRACTION)
elif user_input == "addition":
       
        print(ADDITION)
input("THANK YOU THE PROGRAM IS FINISHED ")



