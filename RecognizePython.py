num1 = 42 #variable decleration
num2 = 2.3 #variable decleration
boolean = True #boolean
string = 'Hello World' #variable decleration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Variable decleration, array or object?, strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable decleration, array, object, strings, number, boolean
fruit = ('blueberry', 'strawberry', 'banana') #variable decleration, strings
print(type(fruit)) #console, access value
print(pizza_toppings[1]) #console, access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #console, access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #change value
print(fruit[2]) #console, access value

if num1 > 45: #conditional, if
    print("It's greater") #console
else: # conditonal, else
    print("It's lower") #console

if len(string) < 5: #conditional, if
    print("It's a short word!") #console
elif len(string) > 15:  #conditional, else if
    print("It's a long word!") #console
else: #conditional, else
    print("Just right!") #console

for x in range(5): #function, parameter
    print(x) #console
for x in range(2,5): #function, parameters
    print(x) #console
for x in range(2,10,3): #function, parameters
    print(x) #console
x = 0 #variable decleration, number
while(x < 5): #conditional, while loop, start
    print(x) #console
    x += 1 #increment

pizza_toppings.pop() #function
pizza_toppings.pop(1)#function, argument

print(person) #console
person.pop('eye_color') #delete value
print(person) #console

for topping in pizza_toppings: #for loop, variable
    if topping == 'Pepperoni': #if
        continue #continue 
    print('After 1st if statement') #console
    if topping == 'Olives': #if
        break #break

def print_hello_ten_times(): #function
    for num in range(10): #for loop, function, parameter
        print('Hello') #console

print_hello_ten_times() #function

def print_hello_x_times(x): #function, parameter
    for num in range(x): #for loop, 
        print('Hello') #console

print_hello_x_times(4) #function, argument

def print_hello_x_or_ten_times(x = 10): #function, parameters
    for num in range(x): #for loop, function
        print('Hello') #console

print_hello_x_or_ten_times() #function
print_hello_x_or_ten_times(4) #function, argument


"""
Bonus section
"""

# print(num3) ---Console num3
# num3 = 72   ---Decleration of variable, Number
# fruit[0] = 'cranberry' ---CHANGE VALUE
# print(person['favorite_team']) ---Console, access value
# print(pizza_toppings[7]) ---Console, access value, position 7
#   print(boolean) ---Console, true or false
# fruit.append('raspberry') ---Add value, string
# fruit.pop(1) ---Delete value, position 1