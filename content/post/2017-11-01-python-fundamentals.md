---
title: "Python Fundamentals"
slug: "python-fundamentals"
date: "2017-11-01"
tags: ["basic-python"]
---

This post will cover the absolutely basics of Python language

## Types, Statements

Unlike others, there's no need to declare variables in Python

```ipython
## No Need to declare Python variables
answer = 42
name = "Python"

print(answer)
print(name)

## Integers and Floats can operate with each other
answer = 42
pi = 3.14159

print(answer + pi)
```

## String

We can use single, double and tripple quotes to create strings

```ipython
'Hello World' == "Hello World" == """Hello World"""
```

There are a number of useful string methods

```ipython
### There are a bunch of useful string methods

### Capitalize the first letter
print("hello".capitalize())

### Convert all string characters to uppercase
print("hello".upper())

### Replace a letter
print("hello".replace("e","3"))

### Check if string contrains only alphabet
print("hello".isalpha() == True)

### Check if string contains only numbers
print("123".isdigit() == True)

### Split string to a list
print("some, csv, values".split(","))

### String Format Function
print("{a} and {b} are changing the world now"
      .format(a = "Machine Learning", b="Artificial Intelligence"))
```

## List

```ipython
student_names = ["Mark", "Katarina", "Tim"]

## Add an item to a list
## Same as the push method in javascript
student_names.append("Isaac")

## Check if an element is in a list
print("Tim" in student_names)

## List comprehension
print([element for element in student_names if len(element) <= 4])

score = ["A", "B", "C"]
## dictionary comprehension
results_dict = {a:b for (a,b) in zip(student_names, score)}
print(results_dict)

## set comprehension, seldom used
## can use [::-1] to reverse a list
results_set = {(a,b) for (a,b) in zip(student_names, score[::-1])}
print(results_set)
```

```ipython
student_names = ["Mark", "Katarina", "Tim"]
## Add an item to a list
## Same as the push method in javascript
["Mark", "Katarina", "Tim"].append("Isaac")

[stu.upper() for stu in student_names]

student_names[1:]
student_names[:-1]
del student_names[2]
```

## Loop

```ipython
## Python way
for var in collection:
    # Do something
```

```javascript
for(var i = 0; i < collection.length; i++) {
    // do something
}
```

## Break and Continue

Sometimes we don't want the loop to run to the end

```ipython
student_names = ["James", "Mark", "Ben", "Iza", "Frank"]

for name in student_names:
    print("Searched name is: "+ name)
    if name == "Iza":
        print("Find him")
        break
```

Continue

```ipython
student_names = ["James", "Mark", "Ben", "Iza", "Frank"]

for name in student_names:
    if name == "Ben":
        print("Found Ben!")
        continue
    print("Current student is: "+name)    
```

## While loops

I rarely use while loops in Python

```ipython
x = 0

while x <= 10:
    print("X is ",x)
    x += 1
```
