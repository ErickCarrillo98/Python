'''Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
Example: countdown(5) should return [5,4,3,2,1,0] '''

def countdown(num):
    new_list = []
    for i in range(num, -1, -1):
        new_list.append(i)
    return new_list
print(countdown(5))




#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(list):
    print(list[0])
    return(list[1])
y = print_and_return([1,2])
print(y)



#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def new(alist):
    sum = alist[0] + len(alist)
    return(sum)

y = new([1,2,3,4,5])
print(y)

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def values_greater_than_second(main_list):
    if len(main_list) < 2:
        return False
    list_two = []
    for i in range(len(main_list)):
        if main_list[i] > main_list[1]:
            list_two.append(main_list[i])
    print(len(list_two))
    return list_two

return_action = values_greater_than_second([5,2,3,2,1,4])
print(return_action)



#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def that_value(size, num2):
    create_list = []
    for i in range(size):
        create_list.append(num2)
    return create_list

print(that_value(4,7))
print(that_value(6,2))
