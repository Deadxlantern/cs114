""" Wall To paint ratio"""
from time import sleep
 #1. Setup
gallon_per_sqft = 400

 #2. input
print("What is the width of the wall?")
width = float(input())
sleep (1)
print("What is the height of the Wall?")
height = float(input())
sleep (1)
print("How much does the gallon cost")
price = float(input())
print("How many layers do you want")
layers = float(input())
 #3. transform

sqft= width*height
coats = sqft/gallon_per_sqft
costs= coats*price*layers
 #4. output
print(" It would cost" ,costs ,'dollar to paint the wall')
