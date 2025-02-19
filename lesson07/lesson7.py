# Lesson 7
import random
dc_user = int(input("Enter the DC level: "))
dice  = random.randrange(1, 21)
print(f"Abilityt: {dice}")

if dc_user <= 20:
    if dice >= dc_user:
        print("You Win")

    else: 
        print("You Lose")
else:
    print("Invalid DC")


