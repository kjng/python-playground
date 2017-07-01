active = True
topping = ''
while active:
    topping = input('Enter a pizza topping: ')
    if topping == 'quit':
        active = False
    else:
        print("I'll add " + topping + " to your pizza!")
