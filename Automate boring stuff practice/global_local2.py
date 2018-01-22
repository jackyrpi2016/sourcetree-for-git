# global scope and local scope 2

def spam():
    eggs = 'hello'   # if this local variable is not here, print global variable eggs = 42
    print(eggs)

eggs = 42
spam()
print(eggs)  # print 42
