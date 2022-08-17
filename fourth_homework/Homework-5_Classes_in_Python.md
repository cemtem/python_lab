# Python Practice - Session

#### Task 5.1
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.


Example:
```python
>>> d = HistoryDict({"foo": 42})
>>> d.set_value("bar", 43)
>>> d.get_history()

["bar"]
```

<em>After your own implementation of the class have a look at collections.deque https://docs.python.org/3/library/collections.html#collections.deque </em>

### Task 5.2
Create hierarchy out of birds. 
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value. 
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.

Example:
```python
>>> b = Bird("Any")
>>> b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
>>> p.fly()
AttributeError: 'Penguin' object has no attribute 'fly'
>>> p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
>>> str(c)
"Canary can walk and fly"
>>> c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
>>> str(s)
"Gull bird can walk, swim and fly"
>>> s.eat()
"It eats fish"
```

Have a look at __mro__ method of your last class.

### Task 5.3

A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. 
Implement singleton logic inside your custom class using a method to initialize class instance.

Example:

```python
>>> p = Sun.inst()
>>> f = Sun.inst()
>>> p is f
True
```

### Task 5.4
Implement a Matrix class which provides the following methods:
  * addition
  * subtraction
  * multiplication
  * multiplication with scalar value
  * transpose
  * check equal or not
  * check is square
  
Example:
```python
>>> a = Matrix(2, 2) # generate random matrix​
>>> b = Matrix([[1,2], [3, 4]]) # concreate matrix​
>>> c = a * b​
>>> c​
[[4, 5],​
[6, 7]]​
>>> c.is_squared()​
True​
```  
  
  
  
### Task 5.5
Implement custom descriptor aka ```property``` as a decorator
Example of Usage:

```python
class Something:​
    def __init__(self, x):​
        self.x = x​

    @prop​
    def attr(self):​
        return self.x ** 2​

    @attr.setter
    def attr_setter(self, update):
        return self.x = update
​
>>> s = Something(10)​
>>> s.attr​
100​
>>> s.attr​ = 3
>>> s.attr​
9
```


### Materials
* [Classes](https://docs.python.org/3/tutorial/classes.html)
* [OOP in python](https://realpython.com/python3-object-oriented-programming/)
* [Python OOP](https://proglib.io/p/python-oop/)
* [Magic methods](https://habr.com/ru/post/186608/)
* [Method resolution order](https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc)
* [Classm & Static methods](https://realpython.com/instance-class-and-static-methods-demystified/)

