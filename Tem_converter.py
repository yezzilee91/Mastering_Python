# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Temperature converter

print("This program converts Celsius(C) to Fahrenheit or Fahrenheit(F) to Celsius")


user_input0= input("Do you want to convert to C or F:")

if user_input0=="F":
    user_input1 = input("Please enter your temperature:")
    Fah= (float(user_input1)*(9/5))+32
    print("Fahrenheit is:", Fah)
elif user_input0=="C":
    user_input2 = input("Please input your temperature:")
    Ce= (float(user_input2)-32)*(5/9)
    print("Celcius is:", Ce)
    

