x = [10,20,30,40]

i = 0
s = 0
while i < len(x):
    s=s+x[i]
    i=i+1
print(s)
j=0
while j <= 5:
    print('welcome',j)
    if j == 3:
        break
    j = j+1
else:
    print("j is greater than 5")

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

if b < a :
    print("b is less than a")
else:
    print("b is greater than a")


q = 0
r = 0

while q <= 100:
    r = r+q
    q = q+1
print(r)


l = 0
m = 0
while l <= 100:
    if m == 100:
        break
    m = m + l

    l = l + 1
print(m)