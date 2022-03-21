import random


def guessNumber():
    while True:
        guess = input('Try one more time> ')

        if guess.isdecimal():
            return int(guess)

        print('Please enter a number between 1 and 100.')


print()
secretNumber = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

for i in range(10):
    print(f'You have {10-i} guesses left. Take a guess')

    guess = guessNumber()
    if guess == secretNumber:
        break

    if guess < secretNumber:
        print(f'Your guess - {guess} is too low')
    if guess > secretNumber:
        print(f'Your guess - {guess} is too high')

if guess == secretNumber:
    print('Yeah! You guessed my number! ', secretNumber)
else:
    print('Game over. The number I was thingking of was ', secretNumber)
