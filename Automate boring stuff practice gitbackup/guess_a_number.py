# guess a number game
# 1.generate a random number  2. permit trying for 6 times  3.give hint for guess values

import random
print('Hi, what is your name ?')
name = input()   # prep for the next print

print('Well, ' + name + '. I am thinking of a number between 1 and 20')
guessNum = random.randint(1, 20)  # generate random number

# use code to debug
print('DEBUG: secret number is ' + str(guessNum))

for i in range(1, 7):   # from 1 to 6
    print('Take a guess')
    userValue = input()

    if int(userValue) > guessNum:
        print('Your guess is too high')   # hint
    elif int(userValue) < guessNum:
        print('Your guess is too low')
    else:
        break;   # correct answer, stop the loop

if int(userValue) == guessNum:
    print('Good job, ' + name + '. You figure out my number in ' + str(i) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(guessNum) + '.')


