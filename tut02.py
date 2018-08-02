'''
Discuss lists and some basic methods to manipulate lists
'''

# How do you declare lists?
# Empty lists?

fruits = ["bananas", "oranges", "grapes", "cherries"]
print(fruits)


'''
Unlike C, lists can store mixture of any data types
'''
random_list = [1, True, "hi!", fruits, 42, ["332", "433"]]
print(random_list)

del random_list[2]
random_list.remove("hi!")


'''
Append
'''
fruits.append('Strawberries')
print(fruits)

fruits[len(fruits):] = ['blackberries']
print(fruits)

veges = ['potatoes', 'tomatoes', 'eggplants']

fruits.extend(veges)
print(fruits)

fresh_foods = fruits + veges
print(fresh_foods)



'''
Insert: what if you want to add to any index?
'''
list.insert(i,x)
fruits.insert(0, "lychees") 


list.clear()
fruits.clear() # same as del fruits[:]



'''
SORT

Sometimes you want to keep your original order of items
E.g. in your main function, you sort by name, and
in another function called by your main function, it
uses the list sorted by their mark
'''


# list.sort
fruits.sort() # sort() changes the original list
print(fruits)

fruits2 = sorted(fruits)


'''
Reverse
'''
fruits.reverse()
print(fruits)

rev_fruits = list(reversed(fruits))
rev_fruits = fruits[::-1]
print(rev_fruits[0])





'''
List comprehensions
'''

# 'something' could depend on 'item'
# new_list = [something for item in item_list]

numbers = [-5, 3, 42, 10, 1]

nums1 = [x for x in numbers]
nums2 = [x + 5 for x in numbers]
nums3 = [x**2 for x in numbers]
nums4 = [x for x in numbers if x > 5]

print(nums1)
print(nums2)
print(nums3)
print(nums4)


message = "BIG" if max(numbers) > 10 else "SMALL"
print(message)





'''
Q1. Given a list of numbers, find the median of the numbers
You may assume that the input list contains at least one number.

'''

def median(numbers):
    if len(numbers) == 0:
        return None

    sorted_numbers = sorted(numbers)

    # indices of higher and lower medians
    hi = len(numbers) // 2
    lo = (len(numbers) - 1) // 2

    # This approach works regardless of whether there are
    # two 'middle' values (even number of elements in the list)
    # or there is just one (odd number of elements in the list)
    median = (numbers[lo] + numbers[hi]) / 2

    return median

# numbers = [2, 4, -23, 2, 95, 21]
# print(median(numbers))






'''
Another useful data type built into Python is the dictionary. Unlike a list, string or tuple whose elements can
be indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type;
strings and numbers can always be keys.
'''


'''
It allows us to index elements not just by integers, but any
reasonable data type

index = key (unique per element)
element = value

immutable - so cannot store a list
'''

phone = {'sam': 97896000, 'john':95842384, 'tom':97268907}
phone['adam'] = 12341234
print(phone)

print('sam' in phone)
print(phone['sam'])


for key in phone:
    print('name:', key)

for value in phone.values():
    print('number:', value)

for key, value in phone.items():
    print('name:', key, 'number:', value)
    # print(f'name: {key}, number: {value}')





'''
Common list methods:
list(d.keys()) on a dictionary returns all the keys in the dictionary
use the 'in' keyword to check if a particular key exists
dict() can be used to build a dictionary from a sequence of key-value pairs
use items() to loop through the dictionary
'''


'''
You are given a dictionary of fruits names and their prices ($)

Add a new entry: 'golden apple', with a price of $42 per unit

Implement a function that does the following:
 1. For each fruit in store, ask the user how many units
 of the fruit the user would like to purchase (in any order)
 2. After the user has entered the units for every fruit,
 calculates the total price the user has to pay and
 prints this value out
'''


def fruit_shop(fruit_prices):
    total = 0

    print('------------------------')
    for fruit, price in fruit_prices.items():
        count = int(input(f'How many units of {fruit}?: '))
        if count < 0:
            print('You cannot purchase negative units!')
            return

        print(f'Added {count} units of {fruit} to your basket (${count * price})')

    print('------------------------')
    
    total += price * count
    print(f'It would be {total} dollars in total')


fruit_prices = {'bananas': 10, 'rock melons': 4, 'blueberries': 23}
fruit_prices['golden apple'] = 42
fruit_shop(fruit_prices)






# Python program to find the factorial of a number provided by the user.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# To test
# number = int(input("Input a number to compute the factorial: "))
# print(factorial(number))

memo = {0: 1}
def factorial2(n):
    if n in memo:
        return memo[n]
    
    memo[n] = n * factorial2(n - 1)
    return memo[n]


# for i in range(1000):
#     print(factorial2(i))
