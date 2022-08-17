# Python Practice - Session 7


### Task 7.1
Implement class-based context manager for opening and working with file, including handling exceptions. Do not use 'with open()'. Pass filename and mode via constructor.

### Task 7.2
Implement context manager for opening and working with file, including handling exceptions with @contextmanager decorator.

### Task 7.3
Implement decorator with context manager support for writing execution time to log-file. See contextlib module.

### Task 7.4
Implement decorator for suppressing exceptions. If exception not occure write log to console.

### Task 7.5
Implement function for check that number is even and at least 3. Throw different exceptions for these errors. Custom exceptions must be derived from custom base exceptions (not Base Exception classes).


### Task 7.6
Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it iterates through.
Example:
```python
lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
>>> 1 4 9 16 25

```

### Task 7.7
Implement a generator which will generate odd numbers endlessly.
Example:
```python
gen = endless_generator()
while True:
    print(next(gen))
>>> 1 3 5 7 ... 128736187263 128736187265 ...
```

### Task 7.8
Implement a generator which will geterate [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.
Example:
```python
gen = endless_fib_generator()
while True:
    print(next(gen))
>>> 1 1 2 3 5 8 13 ...
```

### Task 7.9
Implement a generator that receives other generators and generates elements from input generators  consistently
```python
def g1():
    yield 1
    yield 3

def g2():
    yield 2
    yield 4


for i in your_generator(g1, g2):
    print(i)
>>> 1 3 2 4
```

### Materials
* [Exceptions](https://realpython.com/python-exceptions/)
* [Contextlib](https://python-scripts.com/contextlib)
* [Context Managers](https://book.pythontips.com/en/latest/context_managers.html)
* [Python iterator](https://www.programiz.com/python-programming/iterator)
* [Iterators](https://anandology.com/python-practice-book/iterators.html)
* [Iterators and Generators](https://www.youtube.com/watch?v=jTYiNjvnHZY)
* [List comprehension and generator expressions](https://www.youtube.com/watch?v=3dt4OGnU5sM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=20)

