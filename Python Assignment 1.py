# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 00:25:33 2019

@author: moham
"""
import sys
import datetime
from math import pi

#Assignment no: 1

#Qno1

print("......Qno1.........")
print("Twinkle,  twinkle Little Star")
print("      how i wonder what you are!")
print("            up upon the world so High")
print("            like a diamond in the sky")
print("Twinkle, twinkle little Star")

#Qno2
print("        ")
print(".......Qno2........")
print ('the version of pythion is:')
print(sys.version)

#Qno3

print("        ")
print(".......Qno3........")
now = datetime.datetime.now()
print("the Current Date And Time")
print(now.strftime("%Y-%m-%d, %H:%M:%S"))

#Qno4

print("        ")
print(".......Qno4........")
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

#Qno5

print("        ")
print(".......Qno5........")
First_Name=input("Enter the First Name : ")
Last_Name=input("Enter the Last Name : ")
print(Last_Name  +" "+  First_Name)

#Qno6

print("        ")
print(".......Qno6........")
First_Number=int(input("Enter the First Number : "))
Second_Number=int(input("Enter the Second Number : "))
print(First_Number+Second_Number)


