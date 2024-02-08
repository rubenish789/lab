import random
def guessNumber():
    x = input("Hello! What is your name?\n")
    num = random.randint(1,20)
    print(f"Well, {x}, I am thinking of a number between 1 and 20.")
    i = 0
    while True:
        i+=1
        print("Take a guess.")
        attempt = int(input())
        if attempt == num:
            print(f"Good job, {x}! You guessed my number in {i} guesses!")
            break
        elif(attempt > num):
            print("\nYour guess is too big")
            continue
        elif(attempt < num):
            print("\nYour guess is too low")
            continue
        
guessNumber()