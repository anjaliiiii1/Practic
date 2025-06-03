import random

Secret_Num = random.randint(1,20)
user = int(input("Guess the secret number : "))

while user!= Secret_Num:
    user = int(input("try a : "))

print("Congratulations!")
    
