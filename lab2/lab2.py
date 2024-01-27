#1
print(10 > 9)
#True

#2
print(10 == 9)
#False

#3
print(10 < 9)
#False

#4
print(bool("abc"))
#True

#5
print(bool(0))
#False

#6
print(10 * 5)

#7
print(10 / 2)

#8
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#9
if(5 != 10):
    print("5 and 10 is not equal")

#10
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

#11
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#12
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#13
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#14
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#15
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#16
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#17
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#18
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#19
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#20
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#21
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#22
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#23
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:  
    print("Yes, apple is a fruit!")

#24
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#25
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#26
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#27
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#28
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#29
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#30
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#31
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#32
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#33
a = 50
b = 10
if a > b:
    print("Hello World")

#34
a = 50
b = 10
if a != b:
    print("Hello World")

#35
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")

#36
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

c = 5
d = 1

#37
if a == b and c == d:
    print("Hello")

#38
if a == b or c == d:
    print("Hello")

#39
if 5 > 2:
    print("YES")

#40
a = 2
b = 5
print("YES") if a == b else print("NO")

#41
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

#42
i = 1
while i < 6:
    print(i)
    i += 1

#43
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

#44
i = 0
while i < 6:
    i += 1
    if i == 3:    
        continue

    print(i)

#45
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#46
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#47
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue

    print(x)

#48
for x in range(6):
    print(x)

#49
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
    