# Python-Function-Guide
Basic python3 function guide
# Built-in functions
## chr
Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff. 
Usage: chr(i)
Note: chr() takes exactly one argument
---
Examples:
```Python
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
