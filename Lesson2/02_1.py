# list
from Lesson1.type_strings import coordinates
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mix = ["text", 56, 34.7, True, True]
empty = []

print(type(empty))
print("length of numbers:", len(numbers))
print("length of fruits:", len(fruits))

print(fruits[1])
print(fruits[::-1])
print(fruits[-1])

fruits[1] = 'orange'
print(fruits)

fruits.append('lemon')
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

fruits.remove("kiwi")
print(fruits)

last = fruits.pop()
print(last)
print(fruits)

numbers2 = [99, 1, 2, 34, 4, 5, 78, 7, 0, 9, 10]
print(sorted(numbers2))
print(sorted(numbers2, reverse=True))
print(min(numbers2), max(numbers2), sum(numbers2))
print("Is 34 in numbers2 --> ", 34 in numbers2)

numbers2.sort()
print(numbers2)

for fruit in fruits:
    print("I like ", fruit)