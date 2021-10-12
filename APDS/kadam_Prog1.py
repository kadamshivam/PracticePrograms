#Program to calculate Body mass index
#Written by Shivam Sanjay Kadam
#Date: 08/30/2021
#Input Variable: heigth weight
#Output Variable: BMI
weight=float(input("Enter weight in pounds"))
height=float(input("Enter height in inches"))
BMI=weight/(height**2)*703
print("Calculated BMI is",BMI)
if BMI<18 or BMI>25:
    print("Clinical Issues")
else:
    if BMI < (18+25)/2:
        print("Healthy body")
    if BMI > (18+25)/2:
        print("Unhealthy body")