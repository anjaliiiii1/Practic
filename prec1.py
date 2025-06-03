import random

Secret_Num = random.randint(1,20)
user = int(input("Guess the secret number : "))

while user!= Secret_Num:

    if user > Secret_Num:
        print("Too High")
    else:
        print ("too low")

    user = int(input("try again : "))

print("Congratulations!")
    
