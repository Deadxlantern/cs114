print(" Hello old world Master")
from time import sleep
sleep (1)

print ("Are you a Vampire?")
vampire = input()
vampup=vampire.upper()
sleep (1)
if vampup=='NO':
    print('Only blood suckers allowed, Begone bloodbag.')
else:
    print ("How old are you ancient one")
    age  = int(input())
    if age >= 2000:
        print ('You are a an immortal warrior step away from the machine')
    elif age <2000:
        print ('You are to young to be near this machine.')
