#  File: GuessingGame.py

#  Description: Guess the correct number

#  Student Name: Courtney Thomas

#  Student UT EID:

#  Course Name: CS 303E

#  Unique Number: 1

#  Date Created: 4/10/2016

#  Date Last Modified: 4/10/2016

def average(lo, hi):
    return (lo + hi) // 2

def main():
    while True:
        print('Guessing Game', end='\n\n')
        print('Think of a number between 1 and 100 inclusive.', end='\n');
        print('And I will guess what it is in 7 tries or less.', end='\n\n')

        while True:
            ready = input('Are you ready? (y/n):')
            if (ready == 'n'):
                print(end='\n')
                print('Bye')
                exit(1)
            if ready == 'y':
                break
        break

    print(end='\n')
    lo = 1
    hi = 100
    guess_count = 1
    guess = 50
    while guess_count < 8:
        guess = average(lo, hi)
        print('Guess', guess_count,' :  The number you thought was', guess, end='\n')
        hint = eval(input('Enter 1 if my guess was high, -1 if low, and 0 if correct:'))
        print(end='\n')
        if hint == 1:
            hi = guess
            guess_count = guess_count + 1
            continue
        if hint == -1:
            lo = guess
            guess_count = guess_count + 1
            continue
        if hint == 0:
            print('Thank you for playing the Guessing Game.')
            exit(1)

    print('Either you guessed a number out of range or you had an incorrect entry.')              
    exit(1)
          
main()
