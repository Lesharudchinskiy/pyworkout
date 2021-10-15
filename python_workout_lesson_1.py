import random


def guessing_game():
    rand_num = random.randint(1, 100)

    while True:
        user_num = input('Print your number here:')
        if user_num.isdigit():

            if int(user_num) > rand_num:
                print('Too high, try again')

            if int(user_num) < rand_num:
                print('Too low, try again')
            if int(user_num) == rand_num:
                print(f'Just right the number was: {rand_num}')
                break
        else:
            print(f'Your input "{user_num}" - is not digital, please you ONLY digits')


guessing_game()
