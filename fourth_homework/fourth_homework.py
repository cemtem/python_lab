import random


class HistoryDict:
    dictionary = {}
    history = []

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def set_value(self, key, value):
        if key not in self.history:
            self.history.append(key)
        if len(self.history) >= 11:
            del self.history[0]

        self.dictionary[key] = value

    def get_history(self):
        print(self.history)


class Bird:
    name = ''

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(self.name + ' bird can fly')

    def walk(self):
        print(self.name + ' bird can walk')

    def __str__(self):
        return self.name + " can fly, walk"


class FlyingBird(Bird):
    name = ''
    ration = ''

    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.name = name
        self.ration = ration

    def eat(self):
        print(self.name + ' bird eats ' + self.ration)

    def __str__(self):
        return self.name + " can fly, walk, eat"


class NonFlyingBird:
    name = ''
    ration = ''

    def __init__(self, name, ration='fish'):
        self.name = name
        self.ration = ration

    def walk(self):
        print(self.name + ' bird can walk')

    def eat(self):
        print(self.name + ' bird eats ' + self.ration)

    def swim(self):
        print(self.name + ' bird can swim')

    def __str__(self):
        return self.name + " can swim, walk, eat"


class SuperBird(Bird, NonFlyingBird):
    name = ''
    ration = ''

    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.name = name
        self.ration = ration

    def __str__(self):
        return self.name + " can fly, walk, swim, eat"


class Sun:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def inst(self):
        self.__init__()
        return self


class Matrix:
    rows = 0
    cols = 0
    matrix = []

    def __init__(self, *args):
        self.matrix = self.get_matrix(*args)

    def get_matrix(self, *args):
        if len(args) == 1:
            return args
        else:
            matrix = [[None for _ in range(args[0])] for _ in range(args[1])]
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    matrix[i][j] = random.randint(0, 100)
            return matrix

    def __str__(self):
        return str(self.matrix)

    def addition(self):
        pass

    def subtraction(self):
        pass

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def multiplication(self, matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                # iterate through rows of Y
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

    def __mul__(self, other):
        return self.multiplication(self, other)

    def multiplication_with_scalar_value(self):
        pass

    def transpose(self):
        pass

    def check_equal_or_not(self):
        pass

    def check_is_square(self):
        pass


class prop:

    def __init__(self,
                 fget=None,
                 fset=None,
                 fdel=None,
                 doc=None):

        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class Something:
    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        return self.x ** 2

    @attr.setter
    def attr(self, update):
        self.x = update


if __name__ == '__main__':
    # Task 5.1
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    d.get_history()

    # Task 5.2
    b = Bird("Any")
    b.walk()
    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    # p.fly()
    p.eat()
    c = FlyingBird("Canary")
    print(str(c))
    c.eat()
    s = SuperBird("Gull")
    print(str(s))
    s.eat()

    # Task 5.3
    p = Sun().inst()
    f = Sun().inst()
    print(p == f)

    # Task 5.4
    # a = Matrix(2, 2)
    # b = Matrix([[1, 2], [3, 4]])
    # print(a)
    # print(b)
    # c = a * b
    # print(c)

    # Task 5.5
    s = Something(10)
    print(s.attr)

    s.attr = 3
    print(s.attr)
