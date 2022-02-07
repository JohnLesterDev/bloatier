# Bloatier - A String Bloater/Debloater Algorithm

Description: My custom __format__ __algorithm__ with _loosy_ RAM allocation
and _terribly_ _huge_ time and space complexity that __bloats__ and __debloats__
string and string-like types.

---

## Sample

> Using bloat/debloat for basic stage format:

```python
# Importing the package
import bloatier

string_ = "A"  # Our string to be bloated
bloated_string = bloatier.bloat(string_)  # Bloated string

# Print the bloated string
print("Bloated String:\n", bloated_string)

# Print the debloated string
print("Debloated String = ", bloatier.debloat(bloated_string))
```

> Result:

```
Bloated String:
O0000000000000000000000000000000000000000000000000000000000
000000000000000000000O0000000000000000000000000000000000000
00000000000O00000000000000000000000000000000000000000000000
0O000000000000000000000000000000000000000000000000O00000000
0000000000000000000000000000000000000000O000000000000000000
000000000000000000000000000000O0000000000000000000000000000
00000000000000000000O00000000000000000000000000000000000000
0000000000O000000000000000000000000000000000000000000000000
O000000000000000000000000000000000000000000000000O000000000
000000000000000000000000000000000000000O0000000000000000000
00000000000000000000000000000O00000000000000000000000000000
0000000000000000000O000000000000000000000000000000000000000
000000000O000000000000000000000000000000000000000000000000O
000000000000000000000000000000000000000000000000O0000000000
00000000000000000000000000000000000000O00000000000000000000
0000000000000000000000000000O000000000000000000000000000000
000000000000000000O0000000000000000000000000000000000000000
00000000O000000000000000000000000000000000000000000000000O0
00000000000000000000000000000000000000000000000O00000000000
0000000000000000000000000000000000000O000000000000000000000
000000000000000000000000000O0000000000000000000000000000000
00000000000000000O00000000000000000000000000000000000000000
0000000O000000000000000000000000000000000000000000000000O00
0000000000000000000000000000000000000000000000O000000000000
000000000000000000000000000000000000O0000000000000000000000
00000000000000000000000000O00000000000000000000000000000000
0000000000000000O000000000000000000000000000000000000000000
000000O000000000000000000000000000000000000000000000000O000
000000000000000000000000000000000000000000000O0000000000000
00000000000000000000000000000000000O00000000000000000000000
0000000000000000000000000O000000000000000000000000000000000
000000000000000O0000000000000000000000000000000000000000000
00000O00000000000000000000000000000000000000000000000000000
00000000000000000000000000O00000000000000000000000000000000
0000000000000000O000000000000000000000000000000000000000000
000000O000000000000000000000000000000000000000000000000O000
000000000000000000000000000000000000000000000O0000000000000
00000000000000000000000000000000000O00000000000000000000000
0000000000000000000000000O000000000000000000000000000000000
000000000000000O0000000000000000000000000000000000000000000
00000O000000000000000000000000000000000000000000000000O0000
00000000000000000000000000000000000000000000O00000000000000
0000000000000000000000000000000000O000000000000000000000000
000000000000000000000000O0000000000000000000000000000000000
00000000000000O00000000000000000000000000000000000000000000
0000O000000000000000000000000000000000000000000000000O00000
0000000000000000000000000000000000000000000O000000000000000
000000000000000000000000000000000O0000000000000000000000000
00000000000000000000000O00000000000000000000000000000000000
0000000000000O000000000000000000000000000000000000000000000
000O000000000000000000000000000000000000000000000000O000000
000000000000000000000000000000000000000000O0000000000000000
00000000000000000000000000000000O00000000000000000000000000
0000000000000000000000O000000000000000000000000000000000000
000000000000O0000000000000000000000000000000000000000000000
00O000000000000000000000000000000000000000000000000O0000000
00000000000000000000000000000000000000000O00000000000000000
0000000000000000000000000000000O000000000000000000000000000
000000000000000000000O0000000000000000000000000000000000000
00000000000O00000000000000000000000000000000000000000000000
0O000000000000000000000000000000000000000000000000O00000000
0000000000000000000000000000000000000000O000000000000000000
000000000000000000000000000000O0000000000000000000000000000
00000000000000000000O00000000000000000000000000000000000000
0000000000O000000000000000000000000000000000000000000000000
O000000000000000000000000000000000000000000000000O000000000
000000000000000000000000000000000000000O0000000000000000000
00000000000000000000000000000O00000000000000000000000000000
0000000000000000000O000000000000000000000000000000000000000
000000000O000000000000000000000000000000000000000000000000O
000000000000000000000000000000000000000000000000O0000000000
00000000000000000000000000000000000000O00000000000000000000
0000000000000000000000000000O000000000000000000000000000000
000000000000000000O0000000000000000000000000000000000000000
000000000000000000000000000000000000000O0000000000000000000
00000000000000000000000000000O00000000000000000000000000000
0000000000000000000O000000000000000000000000000000000000000
000000000O000000000000000000000000000000000000000000000000O
000000000000000000000000000000000000000000000000O0000000000
00000000000000000000000000000000000000O00000000000000000000
0000000000000000000000000000O000000000000000000000000000000
000000000000000000O0000000000000000000000000000000000000000
00000000O000000000000000000000000000000000000000000000000O0
00000000000000000000000000000000000000000000000O00000000000
0000000000000000000000000000000000000O000000000000000000000
000000000000000000000000000O0000000000000000000000000000000
00000000000000000O00000000000000000000000000000000000000000
0000000O000000000000000000000000000000000000000000000000O00
0000000000000000000000000000000000000000000000O000000000000
000000000000000000000000000000000000O0000000000000000000000
00000000000000000000000000O00000000000000000000000000000000
0000000000000000O000000000000000000000000000000000000000000
000000O000000000000000000000000000000000000000000000000O000
000000000000000000000000000000000000000000000O0000000000000
00000000000000000000000000000000000O00000000000000000000000
0000000000000000000000000O000000000000000000000000000000000
000000000000000O0000000000000000000000000000000000000000000
00000O000000000000000000000000000000000000000000000000O0000
00000000000000000000000000000000000000000000O00000000000000
0000000000000000000000000000000000O000000000000000000000000
000000000000000000000000O0000000000000000000000000000000000
00000000000000O00000000000000000000000000000000000000000000
0000O000000000000000000000000000000000000000000000000O00000
0000000000000000000000000000000000000000000O000000000000000
000000000000000000000000000000000O0000000000000000000000000
00000000000000000000000O00000000000000000000000000000000000
0000000000000O000000000000000000000000000000000000000000000
000O000000000000000000000000000000000000000000000000O000000
000000000000000000000000000000000000000000O0000000000000000
00000000000000000000000000000000O00000000000000000000000000
0000000000000000000000O000000000000000000000000000000000000
000000000000O0000000000000000000000000000000000000000000000
00O000000000000000000000000000000000000000000000000O0000000
00000000000000000000000000000000000000000O00000000000000000
0000000000000000000000000000000O000000000000000000000000000
000000000000000000000O0000000000000000000000000000000000000
00000000000O000000000000000000000000000000000000000000000000
Debloated String = A
```

> Note: You can also use bloats/debloats for multi-stage format. (if you have enough RAM :>)

---

The string being used by the algorithm and the outputs are all stored
in a dictionary "__obtain__" and can be acquired by using the __acquired__ function.

There is a main __bloatier__ class and __5__ local functions related to the main class.

- __bloatier__ class
    - _bloat_ method
    - _bloats_ method
    - _debloat_ method
    - _debloats_ method
    - _acquire_ method
- _bloat_ function
- _bloats_ function
- _debloat_ function
- _debloats_ function
- _acquire_ function

---
