>>> type(42)
<class 'int'>
>>> int('32')
32
>>> int('Hello')
ValueError: invalid literal for int(): Hello
>>> int(3.99999)
3
>>> int(-2.3)
-2
>>> float(32)
32.0
>>> float('3.14159')
3.14159
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
>>> import math
>>> math
<module 'math' (built-in)>
>>> ratio = signal_power / noise_power
>>> decibels = 10 * math.log10(ratio)
>>> radians = 0.7
>>> height = math.sin(radians)
>>> degrees = 45
>>> radians = degrees / 180.0 * math.pi
>>> math.sin(radians)
0.707106781187
>>> math.sqrt(2) / 2.0
0.707106781187
x = math.sin(degrees / 360.0 * 2 * math.pi)
x = math.exp(math.log(x+1))
>>> minutes = hours * 60 # correto
>>> hours * 60 = minutes # errado!
SyntaxError: can't assign to operator
def print_lyrics():
print("I'm a lumberjack, and I'm okay.")
print("I sleep all night and I work all day.")
>>> def print_lyrics():
... print("I'm a lumberjack, and I'm okay.")
... print(“I sleep all night and I work all day.”)
...
>>> print(print_lyrics)
<function print_lyrics at 0xb7e99e9c>
>>> type(print_lyrics)
<class 'function'>
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
def repeat_lyrics():
print_lyrics()
print_lyrics()
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
def print_lyrics():
print("I'm a lumberjack, and I'm okay.")
print("I sleep all night and I work all day.")
def repeat_lyrics():
print_lyrics()
print_lyrics()
repeat_lyrics()
def print_twice(bruce):
print(bruce)
print(bruce)
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(42)
42
42
>>> print_twice(math.pi)
3.14159265359
3.14159265359
>>> print_twice('Spam '*4)
Spam Spam Spam Spam
Spam Spam Spam Spam
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.
def cat_twice(part1, part2):
cat = part1 + part2
print_twice(cat)
>>> line1 = 'Bing tiddle '
>>> line2 = 'tiddle bang.'
>>> cat_twice(line1, line2)
Bing tiddle tiddle bang.
Bing tiddle tiddle bang.
>>> print(cat)
NameError: name 'cat' is not defined
Traceback (innermost last):
File "test.py", line 13, in __main__
cat_twice(line1, line2)
File "test.py", line 5, in cat_twice
print_twice(cat)
File "test.py", line 9, in print_twice
print(cat)
NameError: name 'cat' is not defined
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
>>> math.sqrt(5)
2.2360679774997898
>>> result = print_twice('Bing')
Bing
Bing

>>> print(result)
None
>>> print(type(None))
<class 'NoneType'>
>>> right_justify('monty')
def do_twice(f):
f()
f()
def print_spam():

print('spam')
do_twice(print_spam)
print('+', '-')
