###############################################################################
#
# Filename: lists_tuples_sets_and_dicts.py
#
# CS Assignment: Varies
# Text: The Practice of Computing with Python
#
# Version History
#
# Date:       Name:                ChangeNo:  Comment:
# 02/09/2016  Luke Kanuchok        00000000    Create Examples
#
###############################################################################
#
# Problem Description: Go through several data structures in python and
#                      demonstrate how the work, similarities and differences,
#                      and provide context for using them in CST-110.
#
###############################################################################
#
# Pseudocode Algorithm:
#
# Main Step 1 - Detail lists in python
# - What is a list?
# - How do I create a list?
# - What are some useful list methods?
# - What are some precautions when using lists?
#
# Main Step 2 - Detail tuples in python
# - What is a tuple?
# - How do I create a tuple?
# - What are some useful tuple methods?
# - What are some precautions when using tuples?
# - How are tuples different from lists?
#
# Main Step 3 - Detail sets in python
# - What is a set?
# - How do I create a set?
# - What are some useful set methods?
# - What are some precautions when using sets?
#
# Main Step 4 - Detail dicts in python
# - What is a dict?
# - How do I create a dict?
# - What are some useful dict methods?
# - What are some precautions when using dicts?
# - How are sets different from dicts?
#
###############################################################################
#
# Inputs: N/A
# Outputs: N/A
#
###############################################################################


# Main Step 1 - Detail lists in python

# - What is a list?
# A list is a type of value in python. It is a collection of values, which are
# allowed to be of multiple types. It is an ordered collection, with values
# being indexed starting at 0 up through n-1 (for a list with n elements). A
# list is mutable, which means that it can be changed. You can create new lists
# very easily.

# - How do I create a list?
# You can create a tuple in several ways.
# Using square brackets around a comma delimited collection of items is
# probably the most popular:
list1 = [1, 2, 4, 6, 88, "Hello"]

# Alternatively, you can use the typename as a function to convert another
# collection into a list (in this case, a tuple into a list):
list2 = list(('a', 'b', 'c'))

# SIDE NOTE: You can turn a string into a list
str_list = list("Testing")
print(str_list)    # Gives ['T', 'e', 's', 't', 'i', 'n', 'g']

# And turn a string back into a list (using a string method called join)
# help(str.join)
# S.join(iterable) -> str  
# Return a string which is the concatenation of the strings in the
# iterable.  The separator between elements is S.
print("-".join(str_list))   # Gives T-e-s-t-i-n-g (joined the characters with
                            #                      '-' between each item.
# End SIDE NOTE

# Finally, you can create a new list by combining two or more  other lists with
# concatenation.
list3 = list1 + list2 + ['4', '5', '6']

# - What are some useful list methods?
# You can 'append' elements to a list:
list1.append(55)
list2.append("Apple")

# You can use 'index' to find where in a list an element exists:
list1.index(4)    # gives 2 (0-based indexing!)
list2.index("a")  # gives 0 (0-based indexing!)

# You can 'insert' elements into a list:
# list.insert(index, object) -- insert object before index
list1.insert(1, "Goodbye")  # result: [1, "Goodbye", 2, 4, 6, 88, "Hello"]

# You can 'sort' a list. It must be a list where all of the elements are
# comparable (using "elem1 > elem2" has a meaning):
list2.sort()  # result: ['Apple', 'a', 'b', 'c']

# You can refer to an element in a list by using square brackets at the end of
# the list:
print(list2[1])   # prints 'a'

# You can store new values in a list (change the list) by referring to an
# element of a list on the left hand side of an assignment:
list1[0] = "Five"   # result: ['Five', 'Goodbye', 2, 4, 6, 88, 'Hello', 55]

# You can slice a list by including one or more colon seperated values in
# a lists reference. The first index is the first index to include, and the
# second value is the one _after_ the last index to include:
list1[4:]   # Gives [6, 88, 'Hello', 55]   (element 4 to the end)
list1[3:5]  # Gives [4, 6]  (Element 3 and 4, stop before element 5)
print(list1[:2])   # Gives ['Five', 'Goodbye']  (All elements before index 2)

# You can get the size/length of a collection using the ubiquitous 'len()':
print(len(list1))   # Gives 8: ['Five', 'Goodbye', 2, 4, 6, 88, 'Hello', 55]

# - What are some precautions when using lists?
# As they are mutable, they can be changed. This is both a pro and a con.


# Main Step 2 - Detail tuples in python

# - What is a tuple?
# A tuple is a type of value in python. It is a collection of values, which are
# allowed to be of multiple types. It is an ordered collection, with values
# being indexed starting at 0 up through n-1 (for a tuple with n elements). A
# tuple is immutable, which means that it cannot be changed. You can create new
# tuples very easily, but they are considered distinct from other tuples.

# - How do I create a tuple?
# You can create a tuple in several ways.
# Using parenthesis around a comma delimited collection of items is
# probably the most popular:
tuple1 = (1, 2, 4, 6, 88, "Hello")

# Alternatively, you can use the typename as a function:
tuple2 = tuple(['a', 'b', 'c', 4, 5])

# - What are some useful tuple methods?
# You can NOT 'append' elements to a tuple (NO CHANGING):
#tuple1.append(55)
#tuple2.append("Apple")

# You can use 'index' to find where in a tuple an element exists:
tuple1.index(4)    # gives 2 (0-based indexing!)
tuple2.index("a")  # gives 0 (0-based indexing!)

# You can NOT 'insert' elements into a tuple (NO CHANGING):
#tuple1.insert(1, "Goodbye")  # result: [1, "Goodbye", 2, 4, 6, 88, "Hello"]

# You can NOT 'sort' a tuple. (NO CHANGING):
#tuple2.sort()  # result: ['Apple', 'a', 'b', 'c']

# You can refer to an element in a tuple by using square brackets at the end of
# the tuple:
print(tuple2[1])   # prints 'b'

# You can NOT store new values in a tuple (change the tuple) (NO CHANGING):
#tuple1[0] = "Five"   # result: ['Five', 'Goodbye', 2, 4, 6, 88, 'Hello', 55]

# You can slice a tuple by including one or more colon seperated values in
# a tuples reference. The first index is the first index to include, and the
# second value is the one _after_ the last index to include:
tuple1[4:]   # Gives (6, 88, 'Hello', 55)   (element 4 to the end)
tuple1[3:5]  # Gives (4, 6)  (Element 3 and 4, stop before element 5)
tuple1[:2]   # Gives ('Five', 'Goodbye')  (All elements before index 2)
print(tuple1[4:])   # Gives (88, 'Hello')   (element 4 to the end)
print(tuple1[3:5])  # Gives (6, 88)  (Element 3 and 4, stop before element 5)
print(tuple1[:2])   # Gives (1, 2)  (All elements before index 2)

# You can get the size/length of a collection using the ubiquitous 'len()':
print(len(tuple1))   # Gives 6: (1, 2, 4, 6, 88, 'Hello')

# - What are some precautions when using tuples?
# They are more robust than lists, as they can not be changed.

# - How are tuples different from lists?
# They can be used as dict keys (see later in the document).
# Tuples are nearly exactly what you would get if you made lists immutable:
#>>> print([x for x in dir(list) if x not in dir(tuple)])
#['__delitem__', '__iadd__', '__imul__', '__reversed__', '__setitem__', 'append', 'clear', 'copy', 'extend', 'insert', 'pop', 'remove', 'reverse', 'sort']
#>>> print([x for x in dir(tuple) if x not in dir(list)])
#['__getnewargs__']
#>>> 
#

# Main Step 3 - Detail sets in python

# - What is a set?
# A set is a type of value in python. It is a collection of values, which are
# allowed to be of multiple types. It is an un-ordered collection, which means
# it cannot be indexed. It does have a size.

# - How do I create a set?
# The easy way to create a set is to use braces, without colons:
set1 = {'a', 'b', 'c', 1, 2, 3}
set2 = {'a', 'b', 3, '5', 'HELLO'}
set3 = {3, 1, 'b'}

# You can also make a set out of another collection using set():
x = set([1,2,3,4,5])  # Gives (order?) {1, 2, 3, 4, 5}
y = set("brown fox")  # Gives (order?) {'w', ' ', 'f', 'r', 'o', 'n', 'b', 'x'}

# Notice that if/when you print a set that they may or may not be printed in
# the order that you entered them into the set.
print(set1)

# - What are some useful set methods?
#>>> print([x for x in dir(set) if not x.startswith('__')])
#['add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
# 'intersection', 'intersection_update', 'isdisjoint', 'issubset',
# 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']

# add - Adds an element to the set
set2.add('5')    # Gives (order?) {'HELLO', 'a', 3, 'b', '5'}
# difference - Return the difference of two or more sets as a new set.
set1.difference(set2)   # Gives {1, 2, 'c'} (elements in set1 not in set2)

# discard - Remove an element from a set if it is a member.
set1.discard("Whatever")   # Gives original set1 (element not in original)

# intersection - Return the intersection of two sets as a new set.
set1.intersection(set2)     # Gives the common elements {3, 'b', 'a'} 

# issubset - Report whether another set contains this set.
set3.issubset(set1)    # Gives True (set3 is a subset of set1)

# pop - Remove and return an arbitrary set element. (Note: ARBITRARY!)
x = set("TESTING")
print(x)    # Gives {'S', 'I', 'E', 'N', 'G', 'T'}
x.pop()
print(x)    # Gives (this time!) {'I', 'E', 'N', 'G', 'T'} ('S' was popped)

# remove - Remove an element from a set; it must be a member.
set1.remove('a')    # Gives {1, 2, 3, 'c', 'b'}

# union - Return the union of sets as a new set.
set2.union(set3)   # Gives {1, 3, 'HELLO', 'b', '5', 'a'}

# You can get the size/length of a collection using the ubiquitous 'len()':
print(len(set2))   # Gives 5: {'b', 'HELLO', 3, 'a', '5'}

# - What are some precautions when using sets?
# Use 'discard' if the element may not be in the set, and 'remove' if it is
# known to be in the set.
# 'add', 'remove', 'pop', and 'discard' change a set.
# 'difference', 'intersection', 'union', etc. do not modify the sets involved,
# but return a new set that is based on the original sets.


# Main Step 4 - Detail dicts in python

# - What is a dict? (Short for dictionary!)
# A set is a type of value in python. It is a collection of values, which are
# allowed to be of multiple types. It is an un-ordered collection, which means
# it cannot be indexed. It does have a size. Each item in the collection has
# both a name (a key) and data (a value). You access the values similarly to
# accessing an element in a list or tuple.

# - How do I create a dict?
# The standard creation is balanced fairly evenly between creating an empty
# dict with 'dict()', and then populating the dict using something like
# list indexing:
dict1 = dict()
dict1['key1'] = 'some value'
dict1['second key'] = 345
dict1[(602, 639, 8000)] = 'A phone number'

# ...or creating a dict using a modified set notation:
dict2 = {'key1': 'value1', 'key2': 'value2', 'name': 'John Doe', 5: 'Secret'}

# To access an element in a dict
print(dict1['key1'])   # Gives 'some value'
print(dict2[5])        # Gives 'Secret'

# - What are some useful dict methods?
#>>> print([x for x in dir(dict) if not x.startswith('__')])
#['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
# 'setdefault', 'update', 'values']
#>>>

# get - D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
print(dict1.get("key1", 5))    # Gives "some value" ('key1' was in the dict)
print(dict1.get("key2", 10))   # Gives 10  ('key2' was not in the dict)

# items - A set-like object providing a view on D's items.
for k, v in dict1.items():
    print("Key: '{}', value: '{}'".format(k,v))

#Gives:
#Key: '(602, 639, 8000)', value: 'A phone number'
#Key: 'second key', value: '345'
#Key: 'key1', value: 'some value'

# keys - a set-like object providing a view on D's keys.
for k in dict1.keys():
    print("Key: '{}'".format(k))
# Gives
#Key: 'second key'
#Key: '(602, 639, 8000)'
#Key: 'key1'

# values - an object providing a view on D's values
for v in dict1.values():
    print("Value: '{}'".format(v))
# Gives
#Value: '345'
#Value: 'some value'
#Value: 'A phone number'


# - What are some precautions when using dicts?
# Make sure you know which are which: kays and values.

# - How are sets different from dicts?
# Sets have just values, dicts store values behind keys. Sets allow more
# operations (union, difference, intersection, etc.) combining elements across
# multiple sets. Usually you don't combine multiple dictionaries.

# Final thoughts: when in doubt read the python help.
# >>> help(dict)
# >>> help(dict.fromkeys)
# etc.
