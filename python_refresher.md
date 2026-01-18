
# Built int data types

Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

- Text Type:	str
- Numeric Types:	int, float, complex
- Sequence Types:	list (array), tuple, range
- Mapping Type:	dict (objects)
- Set Types:	set, frozenset
- Boolean Type:	bool
- Binary Types:	bytes, bytearray, memoryview
- None Type:	NoneType


## Lists (array)
```
# example
mylist = ["apple", "banana", "cherry"]
```
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets

List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

## Tuples
``` 
# example
mytuple = ("apple", "banana", "cherry")
```
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.


## Sets
```
# example
myset = {"apple", "banana", "cherry"}
```

Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.



## Dictionaries (objects)

```
# example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# get value 
x = thisdict["model"]
# gives "Mustang"

# to get value before it exists like when making a new set, use the get() method returns the value of the item with the specified key.
# dictionary.get(keyname, value)
counts = {}
counts[color] = counts.get(color, 0) + 1

# get keys
x = thisdict.keys()

# add item
thisdict["color"] = "white"

# change/update item
thisdict["year"] = 2018
thisdict.update({"year": 2020})
```

Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. 
In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values.

## IF...Else
a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("None")


## For Loops
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

## While Loops
i = 1
while i < 6:
  print(i)
  i += 1


# Ranges
Python range
The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

This set of numbers has its own data type called range.

Note: Immutable means that it cannot be modified after it is created.
Creating ranges
The range() function can be called with 1, 2, or 3 arguments, using this syntax:
```
range(start, stop, step)

# in for loop
for x in range(len(word) - 1, -1, -1):
        rev = rev + word[x]
        # rev += word[x]
        print('rev, x', word, rev, x) -> from word like 'good' prints 'doog'
    return rev
```



## Functions
Creating a Function
In Python, a function is defined using the def keyword, followed by a function name and parentheses:

ExampleGet your own Python Server
```
def my_function():
  print("Hello from a function")
```