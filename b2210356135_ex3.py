import random
number = random.randint(0,100)
while True:
    guess = int(input("Guess now! :"))
    if(guess < number):
        print("Increase your number")
    elif(guess > number):
        print("Decrease your number")
    else:
        print("You guessed it!\n",number)
        break