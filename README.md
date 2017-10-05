# Python-Function-Guide
Basic python3 function guide
- [Built-in functions](#built-in functions)
    - [chr](#char)
# Awesome websites
- <http://www.diveintopython3.net/special-method-names.html>
# Built-in functions
## chr
Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff. 

**Usage:** chr(i)

**Note:** chr() takes exactly one argument.

**Examples:**
```python
>>> chr(65)
'A'

>>> chr(1)
'\x01'

>>> chr(0x30)
'0'

>>> chr(100000000)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: chr() arg not in range(0x110000)

```
## complex
complex(real[, imag]) -> complex number
    
Create a complex number from a real part and an optional imaginary part.
This is equivalent to (real + imag*1j) where imag defaults to 0.


**Usage:** complex(real[,imag])

**Note:** complex object's real and imag is a **float** number. 

**Examples:**
```python
>>> complex(1)
(1+0j)

>>> complex(1,2)
(1+2j)

>>> complex(real=1)
(1+0j)

>>> complex(imag=1)
1j

>>> type(complex())
<class 'complex'>
```
## dir
dir([object]) -> list of strings

If called without an argument, return the names in the current scope.
Else, return an alphabetized list of names comprising (some of) the attributes
of the given object, and of attributes reachable from it.
If the object supplies a method named __dir__, it will be used; otherwise
the default dir() logic is used and returns:
  for a module object: the module's attributes.
  for a class object:  its attributes, and recursively the attributes
    of its bases.
  for any other object: its attributes, its class's attributes, and
    recursively the attributes of its class's base classes.

**Usage:** dir([object])

**Note:** This function returns the attributes of the object.

**Examples:**
```python
>>> import sys
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_getframe', '_git', '_home', '_xoptions', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'set_asyncgen_hooks', 'set_coroutine_wrapper', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions', 'winver']

>>> def function():
...     print("hello")
...     
>>> dir(function)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> class Animal:
...     def sound(self):
...         return "miaomiaomiao"
...     
>>> dir(Animal)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'sound']
```
## divmode
Return the tuple (x//y, x%y).  Invariant: div*y + mod == x. 

**Usage:** divmode(x, y)

**Examples:**
```python
>>> divmod(5, 2)
(2, 1) # This is a tuple

>>> divmod(5.0, 2)
(2.0, 1.0)
```
## enumerate
enumerate(iterable[, start]) -> iterator for index, value of iterable

Return an enumerate object.  iterable must be another object that supports
iteration.  The enumerate object yields pairs containing a count (from
start, which defaults to zero) and a value yielded by the iterable argument.
enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

**Note:** The optional `start` parameter represents the number of the first item which default to zero.

**Examples:**
```python
>>> items = ['Cat', 'Dog', 'Rabbit']
... for item in enumerate(items):
...     print(item, type(item))
... 
(0, 'Cat') <class 'tuple'>
(1, 'Dog') <class 'tuple'>
(2, 'Rabbit') <class 'tuple'>
>>> for index, value in enumerate(items):
...     print(index, value)
...     
0 Cat
1 Dog
2 Rabbit
>>> for index, value in enumerate(items, 5):
...     print(index, value)
...         
5 Cat
6 Dog
7 Rabbit
```
## eval
Evaluate the given source in the context of globals and locals.

The source may be a string representing a Python expression
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it.

**Usage:** eval(expression[, globals[, locals]])

**Notes:** `globals` or `locals` optional parameter is a dictionary object.

**Examples:**
This example shows three different position int variables which are added together in eval() function as a string.
```python
>>> global_var = 1
... 
... def function():
...     local_var = 2
...     local_env = locals()
...     local_env.update({"additional_var":3})
...     result = eval("global_var + global_var + additional_var", globals(), local_env)
...     print(result)
... 
... function()
... 
5
```
## execfile
This function is removed from python3. The execfile can be replaced with exec, compile,read.

**Usage:** exec(compile("run.py"), "run.py", exec)

**Examples:**
```python
>>> exec(compile(open('helloworld.py').read(),'helloworld.py','exec'))
helloworld
```
## getattr
getattr(object, name[, default])
Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. 
For example, getattr(x, 'foobar') is equivalent to x.foobar. 
If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.

**Usage:** getattr(object, name[, default])

**Examples:**
```python
>>> class Animal():
...     name = "Animal"
... 
...     def sound(self):
...         return "miaomiao"
>>> getattr(Animal, 'name')
'Animal'
>>> getattr(Animal, 'sound') # Get the function address in the memory
<function Animal.sound at 0x0315C078>
>>> getattr(Animal, 'sound')(None) # You can run the function attribute with (...)
'miaomiao'
```
## abs
Return the absolute value of a number. The argument may be an **integer** or a **floating** point number. 
If the argument is a **complex** number, its magnitude is returned.

**Usage:** abs(x)

**Examples:**
```python
>>> abs(-10) # return type is integer if argument is integer
10
>>> abs(-10.0) # return type is float if argument is float
-10.0
>>> abs(complex(3,4)) # return type is float if argument is a complex number
5.0
```
## all
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

**Usage:** all(iterable)

**Note:** 
The function return True only if all items in iterable object must be True.Otherwise returns False.
False items: **{}, (), [], 0, False**

**Examples:**
```python
>>> items = [0, 0, 0]
>>> all(items)
False
>>> items = [1, 2, 3]
>>> all(items)
True
>>> items = [[], {}, ()]
>>> all(items)
False
```
## any
Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:
```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

**Usage:** any(iterable)

**Note:** The function returns True if any one item in iterable object is True.Otherwise returns False.

**Examples:**
```python
>>> items = [0, 0, 0]
>>> any(items)
False
>>> items = [0, 2, 0]
>>> any(items)
True
>>> items = [[1], {}, ()]
>>> any(items)
True
```
## repr
Return a **string** containing a **printable** representation of an object. 
For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. 
A class can control what this function returns for its **instances** by defining a __repr__() method.

**Usage:** repr(object)

**Note:** Difference between str and repr:(\_\_repr\_\_ is more important than \_\_str\_\_)

reference from <https://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python>
> The default implementation is useless (it’s hard to think of one which wouldn’t be, but yeah)
> - \_\_repr\_\_ goal is to be unambiguous
> - \_\_str\_\_ goal is to be readable
> - Container’s \_\_str\_\_ uses contained objects’ \_\_repr\_\_
> 
> if \_\_repr\_\_ is defined, and \_\_str\_\_ is not, the object will behave as though \_\_str\_\_=\_\_repr\_\_.
> 
> **Summary**:
>
> Implement \_\_repr\_\_ for any class you implement. This should be second nature. 
> Implement \_\_str\_\_ if you think it would be useful to have a string version which errs on the side of more readability in favor of more ambiguity

**Examples:**
```python
class Animal():
    name = "Animal"

    def sound(self):
        return "miaomiao"

    def __repr__(self):
        return 'This is my repr'

print(repr(Animal())) # 'This is my repr'
print(repr(Animal)) # '<class '__main__.Animal'>

>>> str(0.1)
'0.1'
>>> repr(0.1)
'0.1'
>>> hello = 'hello\n'
>>> str(hello)
'hello\n'
>>> repr(hello)
"'hello\\n'"
```
## reversed
reversed(seq)
Return a reverse **iterator**. 
seq must be an object which has a \_\_reversed\_\_() method or supports the sequence protocol (the \_\_len\_\_() method and the \_\_getitem\_\_() method with integer arguments starting at 0).

**Usage:** reversed(seq)

**Examples:**
```python
class Animal():
    """
    Create customize reversible class with sequence protocol.
    
    implement __len__() and __getitem__()
    """
    name = "Animal"
    values = [1, 2, 3, 4, 5]

    def sound(self):
        return "miaomiao"

    def __repr__(self):
        return 'This is my repr'
        
    def __len__(self):
        return len(self.values)
        
    def __getitem__(self, item):
        return self.values[item]
        

for item in reversed(Animal()):
    print(item) # 5,4,3,2,1
```