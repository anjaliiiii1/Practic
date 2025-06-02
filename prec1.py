a = int(input("Enter your 1st Number : "))
b = int(input("Enter your 2nd Number : "))
c = int(input("Enter your 3rd Number : "))

if a>b | a>c:
    print("the biggest number is : ", a)

elif b>a | b>c:
    print("the biggest number is : ", b)

else:
    print("the biggest number is : ", c)
