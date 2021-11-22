#Written by Shivam Sanjay Kadam
#Date: 11/04/2021

import random
import sys


operation_log_list=[]      #list created to store operation performed, number of correct responses and number of incorrect responses


name=input("Enter Your Name ")

print("\nWelcome to our project ",name)
print("\nWhat type of number do you require to perform your operations?")
digit_type=int(input("\n  1-Single digit \t 2-Double digit \t 3-Triple digit "))
operation_count=int(input("\n Input number of times you would like to perform the operation "))


positive_reinforces_list=["Excellent", "Very Good", "Well Done", "Awesome"," Good Job", "Correct"]
supportive_reinforces_list=["Try Again", "OOPS", "Not Quite", "Look at it Again", "Sorry"]

def positive_reinforces():
    print(random.choice(positive_reinforces_list))

def supportive_reinforces():
    print(random.choice(supportive_reinforces_list))




def menu():
    print("\nPlease Select a option from Menu")
    print(" 1-Addition \n 2-Substraction \n 3-Multiplication \n 4-Division \n 5-Write a Report File \n 6-View Report File \n 7-Exit")   #Menu
    option=int(input())
    if option==1:
        addition()
    if option==2:
        substraction()
    if option==3:
        multiplication()
    if option==4:
        division() 
    if option==5:
        writeReportFile()
    if option==6:
        viewReportFile()       
    if option==7:
        close()


#Addition method
def addition():
    print("   ADDITION   ")
    positive_count=0                        #Count to keep record of correct responses
    supportive_count=0                      #Count to present the correct answer after second incorrect try by user
    operation_current_count=0               #Count to keep track of number of times operations performed 
    incorrect_response_count=0              #Count to keep record of incorrect responses
    while operation_current_count < operation_count:
        if digit_type==1:
            num1=random.randrange(0,9)      #Generating random single digit numbers
            num2=random.randrange(0,9)
        if digit_type==2:
            num1=random.randrange(10,99)    #Generating random double digit numbers
            num2=random.randrange(10,99)
        if digit_type==3:
            num1=random.randrange(100,999)  #Generating random triple digit numbers
            num2=random.randrange(100,999)
        print(num1,num2)
        user_answer=int(input("Enter the answer for addition "))
        if user_answer==num1+num2:
            operation_current_count+=1
            positive_count+=1
            supportive_count=0
            positive_reinforces()   #Calling positive_reinforces() method from kadam_support python module
        else:
            operation_current_count+=1
            supportive_count+=1
            incorrect_response_count+=1
            supportive_reinforces() #Calling supportive_reinforces() method from kadam_support python module
            if supportive_count==2:
                print("The correct answer is ",num1+num2)
                break
    operation_log_list.append(['Addition',positive_count,incorrect_response_count])            
    menu()

#Substraction method
def substraction():
    print("   SUBSTRACTION   ")
    positive_count=0
    supportive_count=0
    operation_current_count=0
    incorrect_response_count=0
    while operation_current_count < operation_count:
        if digit_type==1:
            num3=random.randrange(0,9)
            num4=random.randrange(0,9)
        if digit_type==2:
            num3=random.randrange(10,99)
            num4=random.randrange(10,99)
        if digit_type==3:
            num3=random.randrange(100,999)
            num4=random.randrange(100,999)
        print(num3,num4)
        if(num3==num4):
            input("both numbers are the same and the difference is 0 and Press key to continue")
        else:
            if (num4 > num3):
                temp_num = num3
                num3 = num4
                num4 = temp_num
            user_answer=int(input("Enter the answer for substraction "))
            if user_answer==num3-num4:
                operation_current_count+=1
                positive_count+=1
                supportive_count=0
                positive_reinforces()
            else:
                supportive_count+=1
                incorrect_response_count+=1
                operation_current_count+=1
                supportive_reinforces()
                if supportive_count==2:
                    print("The correct answer is ",num3-num4)
                    break
    operation_log_list.append(['Substraction',positive_count,incorrect_response_count])            
    menu()


#Multiplication Method
def multiplication():
    print("   MULTIPLICATION   ")
    positive_count=0
    supportive_count=0
    operation_current_count=0
    incorrect_response_count=0
    while operation_current_count < operation_count:
        if digit_type==1:
            num5=random.randrange(0,9)
            num6=random.randrange(0,9)
        if digit_type==2:
            num5=random.randrange(10,99)
            num6=random.randrange(10,99)
        if digit_type==3:
            num5=random.randrange(100,999)
            num6=random.randrange(100,999)
        print(num5,num6)
        user_answer=int(input("Enter the answer for multiplication "))
        if user_answer==num5*num6:
            operation_current_count+=1
            positive_count+=1
            supportive_count=0
            positive_reinforces()
        else:
            operation_current_count+=1
            supportive_count+=1
            incorrect_response_count+=1
            supportive_reinforces()
            if supportive_count==2:
                print("The correct answer is ",num5*num6)
                break
    operation_log_list.append(['Multiplication',positive_count,incorrect_response_count])
    menu()


#Division Method
def division():
    print("   DIVISION   ")
    positive_count=0
    supportive_count=0
    operation_current_count=0
    incorrect_response_count=0
    while operation_current_count < operation_count:
        if digit_type==1:
            num7=random.randrange(0,9)
            num8=random.randrange(0,9)
        if digit_type==2:
            num7=random.randrange(10,99)
            num8=random.randrange(10,99)
        if digit_type==3:
            num7=random.randrange(100,999)
            num8=random.randrange(100,999)   

        print(num7,num8)
        if(num7==num8):
            input("both numbers are the same and the division is 1 and Press key to continue")
        else:
            if  num8==0:
                print("Division by zero is not possible")
                input("Enter a key to continue ")
            else:
                user_answer=int(input("Enter the answer for division "))
                if  user_answer==num7//num8:
                    operation_current_count+=1
                    positive_count+=1
                    supportive_count=0
                    positive_reinforces()
                else:
                    supportive_count+=1
                    operation_current_count+=1
                    incorrect_response_count+=1
                    supportive_reinforces()
                    if supportive_count==2:
                        print("The correct answer is ",num7//num8)
                        break
    operation_log_list.append(['Division',positive_count,incorrect_response_count])
    menu()

#Write Report File
def writeReportFile():
    try:
        print("Your name will be used as file name")
        reportFile=open(name+'.txt','w')
        reportFile.write(str(operation_log_list))
        reportFile.close()
    except OSError as err:
        print("OS Error: {0}".format(err))
    menu()

#View Report File
def viewReportFile():
    try:
        reportFile=open(name+'.txt','r')
        data=reportFile.read()
        print(data)
        reportFile.close()
    except OSError as err:
        print("OS Error: {0}",format(err))
    menu()




#Exit method    
def close():
    print("Thank You")

 
menu()


