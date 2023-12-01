# Printing, commenting, debugging, string manipulation and variables

print('Hello world!!!!\n')
name = input('What is your name?\n')
print('Your name is ' + name)
age = input('What is your age?\n')


# Concat string

print("My name is " + name + ' and i am ' + str(age) + ' years old')


a = input('a: ')
b = input('b: ')

temp = a
a = b
b = temp

print('a:', str(a))
print('b: ', str(b))

nameitem = input('What is your name?\n')

namelen = len(nameitem)

print(namelen)


print('Welcome to the Brand Name Generator\n')

brandname = input('What is your name?\n')
brandpet = input('What is your pet name?\n')

print('Hi, Your brand name could be ' + str(brandname) + ' ' + str(brandpet))