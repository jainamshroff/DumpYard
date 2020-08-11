# Map Filter And Induce

# Map Function
numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))

# for item in range(len(numbers)):
#     numbers[item] = int(numbers[item])

numbers[2] = numbers[2] + 1
#print(numbers[2])

# def sq(a):
#     return a * a



num = [2, 3, 4, 5, 6, 7, 8]
square = list(map(lambda x : x * x, num))

print(square)

def square(a):
    return a * a

def cube(a):
    return a * a * a

func = [square, cube]

for i in range(5):
    val = list(map(lambda x : x(i), func))
    print(val)

# ---------------------------Filter Function------------------------------------
# it makes a list where a given function returns true

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def greaterThanFive(num):
    return num > 5

greaterThanFiveList = list(filter(greaterThanFive, list1))
print(greaterThanFiveList)

# ---------------REDUCE--------------------

from functools import reduce

list2 = [1, 2, 3, 4]
num = reduce(lambda x, y : x * y, list2 )

# num = 0
# for i in list2:
#     num = num + i

print(num)