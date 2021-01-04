"""
Project:Creating the errors
Author:Devam


"""

user_input_0 = "Devam"
user_input_1 = input("Please Enter Your Name:")
if user_input_0 == user_input_1:
    print(f"Welcome, Mr.{user_input_1.title()} You Are Authorised")
else:
    raise Exception("Invalid Name,You Are Unauthorised!!")
print("Program Terminating..")

"""
user_input = input("enter the any number:")
if not type(user_input) is int:
    raise TypeError("Only integers are allowed")
"""
"""
user_input_1 = 1
while user_input_1 == 1:
    user_input = input("enter the name:")
    try:
        user_input_2 = int(user_input)
        user_number = user_input_2 ** 2
        print(user_number)
    except:
        raise ValueError("Invalid input,only integers are allowed..")
    user_input_1 = int(input("enter any number to end program and press 1 to continue program:"))
print("program terminated")
"""