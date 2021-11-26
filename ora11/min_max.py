import random

def maximum_kereses(lista:list)->float:
    return 0

lista3 = []
for i in range(20):
    lista3.append(random.randint(1,100))

print(lista3)

max=lista3[0]
min=lista3[0]
for temp in lista3:
    if min>temp:
        min=temp
    if max<temp:
        max=temp

print(min, max)