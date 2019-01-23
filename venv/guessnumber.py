x = [10,20,30,40,50,60]

p = 0
while True:
    i = int(input("enter guess value"))
    if i in x:
       print("guess number found")
       break
    else:
       p = p+1
       if p == 3:
           print("you have exceeded the guess")
           break
       print("guess number not found")

