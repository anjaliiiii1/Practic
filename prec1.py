import random
import time
Secret_Num = random.randint(1,20)

attempts = 0

un_attempts = 3

gusses = []

while attempts < un_attempts:

    user = int(input("Guess the secret number : "))
    gusses.append(user)
    attempts +=1
    if Secret_Num == user:
        print(f"Congratulations! you won at {attempts}tris.")
        break;
    
    elif user > Secret_Num:
        print("Too High")
        time.sleep(0.05)

    else:
        print ("too low")
print("Your guesses number were",user)
print("Game Over The correct number is : ", Secret_Num)

    
