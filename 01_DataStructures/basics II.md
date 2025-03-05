# Basics II Practice

### Strings
```
>>> print("Hello")
Hello
>>>>>> name = 'sanket agnihotri'
>>> print(name)
sanket agnihotri
>>> print(name[0:6])
sanket
>>> print(name[0:6:2])
sne
>>> print(name[-1:-10])

>>> print(name[-1:])
i
>>> print(name[-1:7])

>>> print(name[-10:-1])
 agnihotr
>>> print(name[-1:-10])

>>> for n in range(len(name), 0, -1):
...     print(n)
... 
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
>>> for n in range(len(name)-1, -1, -1):
...     print(name[n])
... 
i
r
t
o
h
i
n
g
a
 
t
e
k
n
a
s
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai"
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai

```
### List
```
shoes = ["nike", "adidas", "puma"]
>>> print(shoes)
['nike', 'adidas', 'puma']
>>> print("".join(shoes))
nikeadidaspuma
>>> print(" ".join(shoes))
nike adidas puma
>>> print(", ".join(shoes))
nike, adidas, puma

>>> sqaure = [x**2 for x in range(0,11)]
```

### Dictionaries
```
>>> d
{2: 'z', 3: 'c'}
>>> d_copy=d.copy()
>>> d
{2: 'z', 3: 'c'}
>>> d_copy
{2: 'z', 3: 'c'}
>>> d_copy.popitem()
(3, 'c')
>>> d_copy
{2: 'z'}
>>> d
{2: 'z', 3: 'c'}
>>> d=d_copy
>>> d
{2: 'z'}
>>> d_copy
{2: 'z'}
>>> d_copy.popitem()
(2, 'z')
>>> d
{}
d={
... "x": {1:"a", 2:"b", 3:"c"}, "y": {4:"d", 5:"e", 6:"f"}}
>>> d
{'x': {1: 'a', 2: 'b', 3: 'c'}, 'y': {4: 'd', 5: 'e', 6: 'f'}}
>>> d["x"]
{1: 'a', 2: 'b', 3: 'c'}
>>> d["x"][1]
'a'
>>> cube = {x:x**3 for x in range(11)}
>>> cube
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
>>> cube.clear()
>>> cube
{}
>>> z = ['a', 'b', 'c']
>>> d=dict.fromkeys(z,z)
>>> d
{'a': ['a', 'b', 'c'], 'b': ['a', 'b', 'c'], 'c': ['a', 'b', 'c']}
>>> default_value = 'ok'
>>> d=dict.fromkeys(z,default_value)
>>> d
{'a': 'ok', 'b': 'ok', 'c': 'ok'}
>>> d=dict.fromkeys(z,'e')
>>> d
{'a': 'e', 'b': 'e', 'c': 'e'}
```

### Tuples
```
>>> z=('a', 'b', 'c')
>>> z
('a', 'b', 'c')
>>> z[0]
'a'
>>> z[0]='e'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> len(z)
3
#Tuple unwrapping#
>>> z
('a', 'b', 'c')
>>> (a,b,c)=z
>>> a
'a'
>>> b
'b'
>>> c
'c'
>>> type(z)
<class 'tuple'>
```