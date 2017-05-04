"""Convert miles to kilometers"""

#1. Setup
miles_per_kilometers = 1.60934

#2. input
print("How many miles?")
miles= float(input())

#3. transform
kilometers= miles * miles_per_kilometers

#4. output
print(str(miles) + "miles is " + str(kilometers) + "kilometers")
