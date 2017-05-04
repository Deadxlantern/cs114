"""Convert a volume in gallons to liters"""

 #1. Setup
liters_per_gallon = 3.785411784

 #2. input
print("How many gallons?")
gallons= float(input())

 #3. transform
liters= liters_per_gallon * gallons

 #4. output
print(str(gallons) + "gallons is " + str(liters) + "liters")
