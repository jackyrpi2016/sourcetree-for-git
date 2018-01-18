# change global variabe in local scope

# global scope and local scope 2

def spam():
    global eggs   # first define a global
    eggs = 'hello'  # then change it
    print(eggs)

eggs = 42
spam()
print(eggs)

hello
hello
