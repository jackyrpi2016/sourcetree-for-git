# local variable leads to global variable's change
# may cause weird problems in the code

def eggs(cheese):
    cheese.append('hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) # local variable cheese will be destroyed when the def is finished
            # but local variable cheese has changed the origin value, spam and cheese are only references

            
