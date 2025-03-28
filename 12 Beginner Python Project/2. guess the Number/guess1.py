import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guss a number between 1 and {x} : '))
#         if guess < random_number:
#             print('guess again. Too low.')
#         elif guess > random_number:
#             print('guess again. Too high.')
    
#     print(f'You have guessed the number. The number is {random_number}')




def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)??').lower()
        if feedback == 'h':
            high = guess
        elif feedback == 'l':
            low = guess
        print(f'low : {low} / high : {high} / guess : {guess}')

    print(f'guess number is {guess}')


computer_guess (10)