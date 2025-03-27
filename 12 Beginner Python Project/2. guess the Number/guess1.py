import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guss a number between 1 and {x} : '))
        if guess < random_number:
            print('guess again. Too low.')
        elif guess > random_number:
            print('guess again. Too high.')
    
    print(f'You have guessed the number. The number is {random_number}')

guess (10)