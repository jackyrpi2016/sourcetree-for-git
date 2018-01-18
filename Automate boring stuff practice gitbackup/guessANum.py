# guess a number between 0 and 100

import random
num = random.randint(0, 100)
print(num)

for count in range(10):
    
    print('please guess a number')
    number = int(input())

    if number > num:
        print('please guess a smaller number')
    elif number < num:
        print('please guess a bigger number')
    else:
        print('You are right!')
        break
    
print('The correct number is: ' + str(num))

