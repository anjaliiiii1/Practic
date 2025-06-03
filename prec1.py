import random

Secret_Num = random.randint(1,20)

attempts = 0

un_attempts = 3

while attempts < un_attempts:

    user = int(input("Guess the secret number : "))
    attempts +=1
    if Secret_Num == user:
        print(f"Congratulations! you won at {attempts}tris.")
        break;
    
    elif user > Secret_Num:
        print("Too High")
    else:
        print ("too low")

print("Game Over The correct number is : ", Secret_Num)
    
