### Task 5.1
Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

* <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>

Example:
```python
>>> c = Counter(start=42)
>>> c.increment()
>>> c.get()
43

>>> c = Counter()
>>> c.increment()
>>> c.get()
1
>>> c.increment()
>>> c.get()
2

>>> c = Counter(start=42, stop=43)
>>> c.increment()
>>> c.get()
43
>>> c.increment()
Maximal value is reached.
>>> c.get()
43
```

### Task 5.2
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. 
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

<em> Encryption:
Keyword is "Crypto"

* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
</em>

Example:
```python
>>> cipher = Cipher("crypto")
>>> cipher.encode("Hello world")
"Btggj vjmgp"

>>> cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
```

### Task 5.3
Implement custom Currency class with heirs of Euro, Dollar, Ruble.
Example of Usage:

```python
>>> e = Euro(5)​​
>>> e​​
5 €​​
>>> e.to(Dollar)​​
6 $​​
>>> sum([Euro(i) for i in range(5)])​​
10 €​​
>>> e > Euro(6)​​
False​​
>>> e + Dollar(10)​​  # 5€​​ + 10$
16 €​​
>>> Dollar(10) + e​​
13 $​​
>>> e.course = 2
>>> e.to(Dollar)​​
10 $
>>> Euro.course(Dollar)​
2​
>>> Euro.course(Ruble)​
60​
>>> e.currency
'Euro'
```

