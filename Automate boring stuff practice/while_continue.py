# while loop with continue

spam = 0

while spam < 5:
    spam = spam + 1
    if spam == 3:     
        continue    # skips statments after this
    print('Spam is ' + str(spam))
