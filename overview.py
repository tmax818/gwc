## Variables

# myvar = "python"
# print(myvar)

# myvar = 42
# print(myvar)

## Strings

mystr = "This is my string! It's cool!"
mystr2 = 'This is my string! It\'s cool!'

# print(mystr)
# print(mystr2)


## Datatypes

# strings = "some characters 123, @#%$@#$, True or False"
# print(type(strings))

# integers = 42
# print(type(integers))

# floats = 3.14
# print(type(floats))

# booleans = True or False 
# print(type(booleans))

# no_type = None
# print(type(no_type))


## Conditionals

# if True:
#     print("This is true")

# if False:
#     print("The if is true")
# else:
#     print("No the else is true!!!")

# if False:
#     print("first")
# elif False: 
#     print('second')
# elif False:
#     print('third')
# elif False:
#     print('fourth')
# else:
#     print("last")


## loops while, for and range

# i = 1
# while i <= 10:
#     print('hi there')
#     i += 1

# for x in range(1, 6):
#     print(x ** 2)

## lists len() and in

mylist = [1, 2, 3, 42, True, "a string", 3.14, [4, 5, 6]]

grocery_list = ['bananas', 'apples', 'ice cream', 'milk']

print(grocery_list[2])
grocery_list[0] = 'chips'

print(grocery_list)

#first_item = mylist[0]
# print(first_item)

# mylist[0] = 0 
# first_item = mylist[0]
# print(first_item)
# print(mylist)


mylist_length = len(mylist)

print(mylist_length)
print(len([1, 2, 3, 42, True, "a string", 3.14, [4, 5, 6]]))

item_check = 2 in mylist

print(item_check)

# if item_check:
#     print("Yep, it's in there!")

## functions print() input() range()

def my_print_func():
    print("Sup, Bro")

my_print_func()


def square(num):
    return num ** 2

print(square(4))

def add(a, b):
    return a + b 

print(add(10, 20))