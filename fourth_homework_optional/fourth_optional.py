import string


class Counter:
    start = 0
    stop = 0
    current = 0

    def __init__(self, start=0, stop=0):
        self.counter = start
        self.stop = stop
        self.current = start

    def increment(self):
        if self.current < self.stop or self.stop == 0:
            self.current += 1
        else:
            # raise Exception('Maximal value is reached.')
            print('Maximal value is reached.')

    def get(self):
        return self.current


class Cipher:
    key_word = ''
    encode_alphabet = [letter for letter in string.ascii_lowercase]
    original_alphabet = [letter for letter in string.ascii_lowercase]

    def __init__(self, key_word):
        self.key_word = key_word
        for letter in reversed(key_word):
            del self.encode_alphabet[self.encode_alphabet.index(letter)]
            self.encode_alphabet.insert(0, letter)

    def encode(self, string):
        return self.__encoder__(string, True)

    def decode(self, string):
        return self.__encoder__(string, False)

    def __encoder__(self, string, encode):
        first_alph = self.original_alphabet if encode else self.encode_alphabet
        second_alph = self.encode_alphabet if encode else self.original_alphabet
        res = ''
        for letter in string:
            lower_letter = letter.lower()
            if lower_letter in first_alph:
                pos = first_alph.index(lower_letter)
                if letter.islower():
                    res += second_alph[pos]
                else:
                    res += second_alph[pos].capitalize()
            else:
                res += letter

        return res


class Currency:
    value = 0
    cur_char = ''
    cur_symbol = ''
    cur_name = ''
    courses = {'d': 1.0, 'e': 1.02, 'r': 0.016}

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value) + ' ' + str(self.cur_symbol)

    def __radd__(self, other):
        return Euro(self.value + other)

    def __add__(self, other):
        if issubclass(type(other), Currency):
            return self.value + other.to(type(self))
        else:
            return self.value + other.value

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    def currency(self):
        return self.cur_name

    def to(self, other_currency):
        if type(self) == other_currency:
            return self.value

        other_course = self.courses.get(other_currency.cur_char)
        cur_course = self.courses.get(self.cur_char)
        # self = other_currency(self.value / other_course * cur_course)
        return self.value / other_course * cur_course

    def course(self, other_currency):
        if type(self) == other_currency:
            return 1
        else:
            return self.courses[other_currency.cur_char] * self.courses[self.cur_char]


class Euro(Currency):
    cur_char = 'e'
    cur_symbol = '€'
    cur_name = 'Euro'

    def __init__(self, value):
        super().__init__(value)


class Dollar(Currency):
    cur_char = 'd'
    cur_symbol = '$'
    cur_name = 'Dollar'

    def __init__(self, value):
        super().__init__(value)


class Ruble(Currency):
    cur_char = 'r'
    cur_symbol = 'P'
    cur_name = 'Ruble'

    def __init__(self, value):
        super().__init__(value)


if __name__ == '__main__':
    # Task 5.1
    c = Counter(start=42)
    c.increment()
    print(c.get())

    c = Counter()
    c.increment()
    print(c.get())

    c.increment()
    print(c.get())

    c = Counter(start=42, stop=43)
    c.increment()
    print(c.get())

    c.increment()

    print(c.get())

    # Task 5.2
    cipher = Cipher('crypto')
    print(cipher.encode('Hello world'))
    print(cipher.decode("Fjedhc dn atidsn"))

    # Task 5.3
    e = Euro(5)
    print(e)

    print(e.to(Dollar))
    print(e.to(Ruble))
    print(sum([Euro(i) for i in range(5)]))
    print(e > Euro(6))
    print(e + Dollar(10))
    print(Dollar(10) + e)
    print(Euro(1).course(Dollar))
    print(Euro(1).course(Ruble))
    print(e.currency())
