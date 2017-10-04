# Python-Function-Guide
Basic python3 function guide
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

**Note:** complex object's real and imag is a float number. 

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