# Python Practice Session [Optional]

### Task 1

Add input validation via exceptions and file-import to the program from Task 3-optional.
Handle all exceptions and print user friendly output.

### Task 2

Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception `TypeError` should be raised. Method init sholud be able to take either 
`start,end,step` arguments, where `start` - first number of collection, `end` - last number of collection or some ordered iterable 
collection (see the example).
Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list.
Example:
```python
col1 = MyNumberCollection(0, 5, 2)
print(col1)
>>> [0, 2, 4, 5]
col2 = MyNumberCollection((1,2,3,4,5))
print(col2)
>>> [1, 2, 3, 4, 5]
col3 = MyNumberCollection((1,2,3,"4",5))
>>> TypeError: MyNumberCollection supports only numbers!
col1.append(7)
print(col1)
>>> [0, 2, 4, 5, 7]
col2.append("string")
>>> TypeError: 'string' - object is not a number!
print(col1 + col2)
>>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
print(col1)
>>> [0, 2, 4, 5, 7]
print(col2)
>>> [1, 2, 3, 4, 5]
print(col2[4])
>>> 25
for item in col1:
    print(item)
>>> 0 2 4 5 7
```
