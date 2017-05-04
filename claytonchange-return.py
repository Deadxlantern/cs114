"""Convert Cents to change"""

#1. Setup
D= 1
q= .25
d= .1
n= .05
p= .01
#2. input
print ("How Much Change are you owed")
from time import sleep
sleep (1)
cents= float(input())
print ("change")

#3. transform
dollar = cents//D
cents=cents-dollar*D
quarters = cents//q
cents= cents-quarters*q
dimes = cents//d
cents= cents-dimes*d
nickles = cents//n
cents= round (cents-nickles*n,2)
pennys = cents//p
 #4. output
print("You will recieve " + str(dollar) + " dollars " + str(quarters) + " quarters " + str(dimes) + " dimes " + str(nickles) + " nickles " + str(pennys) + " pennys ")
