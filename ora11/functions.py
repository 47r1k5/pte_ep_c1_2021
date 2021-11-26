# print(chr(80),chr(121),chr(116),chr(104),chr(111),chr(110), sep="")
# print(ord("P"))
# print(ord("a"))
# print(ord("A"))
# print(ord(chr(80)))
# print(float("3.5"))
# print(type(float("3.5")))
# print(int(12))
# print(int("12", base=16))
# print(hex(18))
# print(bin(18))
# print(oct(18))
# number = 23.325236
# print(number)
# print(round(number,2))
# print(round(number,0))
#
#
# kmh=float(input())
# print(kmh*3.6)
#
import random
#
# lista= []
# paros= []
# paratlan= []
#
# for i in range(100):
#     lista.append(random.randint(1,100))
# print(lista)
#
# paros = list()
# paratlan =list()
#
# for elem in lista:
#     if elem % 2 == 0:
#         paros.append(elem)
#     else:
#         paratlan.append(elem)
#
# for elem in paros:
#     print(elem)
#
# for elem in paratlan:
#     print(elem)
#
import math
#
# a=int(input())
# b=int(input())
# c=int(input())
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# kerulet = a + b + c
# d = (a + b + c) / 2
# e = d * (d - a) * (d - b) * (d - c)
# print("Kerület", kerulet)
# print("Terület", math.sqrt(e))

# lista2 = []
# while len(lista2)==0 or lista2!="":
#     lista2.append(input())
# lista2.remove("")
# print(lista2)

# lista3 = []
# for i in range(20):
#     lista3.append(random.randint(1,100))
#
# print(lista3)
#
# max=lista3[0]
# min=lista3[0]
# for temp in lista3:
#     if min>temp:
#         min=temp
#     if max<temp:
#         max=temp
#
# print(min, max)

# def AskUserName():
#     userName = input("Adja meg a nevét! ")
#     HelloUser(userName)
#
# def HelloUser(userName):
#     print("Szia "+str(userName))
#
# AskUserName()

# from datetime import datetime
#
# def TimeNow():
#     print(datetime.now())
#
# TimeNow()


priceWithoutTax=int(input("Adja meg egy termék nettó árát! "))


def get_tax(priceWithoutTax:int, tax=0.27)->float:
    return priceWithoutTax*tax


def price_with_tax(priceWithoutTax:int):
    return priceWithoutTax + get_tax(priceWithoutTax)

print(get_tax(priceWithoutTax))
print(price_with_tax(priceWithoutTax))