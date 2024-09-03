import random
print("Wrlcome to random Password Generator!")
randomchars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890+-*/@#$%^&"
nbrofpwds= int(input("Enter the number of password to be generated: "))
pwlen= int(input("Enter the lenght of password : "))
           
print("Here are your random password!")
for x in range(nbrofpwds):
    pwd=""
    for chars in range(pwlen):
        pwd=pwd+random.choice(randomchars)
print(pwd)