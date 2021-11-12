"""number=35
if number>100:
    print("A szám nagyobb, mint 100.")
else:
    print("A szám nem nagyobb, mint 100.")

if number % 2 ==0:
    print("páros")
else:
    print("nem páros")

number1=3
number2=9
if number1%number2==0:
    print("osztható")
else:
    print("nem osztható")

try:
    print(type(float(input("Kérek egy valós számot"))))
except ValueError:
    print("Hibás bemenet")

print(type(str(7)))
print(type(str(-91.34)))
"""
import random

szam=input()
szam=int(szam)
if type(szam)==int:
    print(szam*3)
else:
    print("nem szám")

