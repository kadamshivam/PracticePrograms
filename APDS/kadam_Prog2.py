#Written by Shivam Sanjay Kadam
#Date: 09/17/2021

import random
name=input("Enter Your Name ")
print("Welcome to our project ",name)


def menu():
    print("Please Select a option from Menu")
    print(" 1-Addition \n 2-Substraction \n 3-Exit")
    option=int(input())
    if option==1:
        addition()
    if option==2:
        substraction()
    if option==3:
        close()

#Addition method
def addition():
    num1=random.random()
    num2=random.random()
    print(num1,num2)
    user_answer=input("Enter the answer for addition ")
    if user_answer==num1+num2:
        input("Well done Press key to continue")
    else:
        print("Sorry the correct answer is",num1+num2)
        input("Press key to continue")
    menu()

#Substraction method
def substraction():
    num3=random.random()
    num4=random.random()
    print(num3,num4)
    if(num3==num4):
        input("both numbers are the same and the difference is 0 and Press key to continue")
    else:
        if (num4 > num3):
            temp_num = num3
            num3 = num4
            num4 = temp_num
        user_answer=input("Enter the answer for substraction ")
        if user_answer==num3-num4:
            input("Well done and Press key to continue")
        else:
            print("Sorry the correct answer is",num3-num4)
            input("Press key to continue")
    menu()

#Exit method    
def close():
    print("Thank you")

menu()


