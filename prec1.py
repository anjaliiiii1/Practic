import random
import time

num = random.randint(1,20)
attampt = 0
max_attampt = 3
guesses = []

print("🎮 Welcome to the Guessing Game!")
time.sleep(1)
print("I am Thinking.. the number Between 1 to 20......")
time.sleep(1)

while max_attampt > attampt:
    guess = int(input("Guess the number : "))
    guesses.append(guess)
    attampt += 1

    if guess == num:
        print(f"🎉 Congratulations! You won in {attampt} tries.")
        break

    elif num > guess:
        print("Too Low.....")
        time.sleep(0.05)

    else :
        print("🔺 Too High!")
        time.sleep(0.05)

if guess != num:
    print("\n❌ Game Over!")

print("📋 Your guesses were:", guesses)
print("✅ The correct number was:", num)
