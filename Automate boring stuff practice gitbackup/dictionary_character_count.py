# count character
# input a string, count how many times a character has appeared in this string


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}  # use dictionary, 'character': count times

for character in message.upper():
    count.setdefault(character, 0)  # if character not exists, create character as the key, and value as 0
    count[character] = count[character] + 1  # increase the count by 1
    
print(count)
