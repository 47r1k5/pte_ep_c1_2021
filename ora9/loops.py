is_number=False
while not is_number:
    try:
        number=int(input("Kérek egy egész számot: "))
        is_number=True
    except:
        print("Ez nem egy szám.")

if number %2==0:
    print("páros")
else:
    print("páratalan")

i=1
while i<=5:
    print(i)
    i+=1

for j in [1,2,3,4,5]:
    print(j)

print()

for k in range(100):
    print(k, end=" ")

print()

for l in range(50,60):
    print(l)