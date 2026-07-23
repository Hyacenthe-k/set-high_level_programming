# Python - Everything is object

## Description
This project covers the fundamentals of Python's object model. It explores how Python handles memory allocation, mutable vs. immutable objects, variable assignment, reference counting, and how arguments are passed to functions.

## Learning Objectives
* What is an object?
* What is the difference between an dynamic type and a static type?
* What is the difference between a mutable and an immutable object?
* What is a reference?
* What is an assignment?
* What is an alias?
* How to know if two variables refer to the same object (`is` vs `==`)?
* How to display the memory address of an object (using `id()`)?
* How are arguments passed to functions (pass-by-value vs. pass-by-reference)?

## Requirements
* **Environment:** Ubuntu 20.04 LTS / Python 3.8.x
* **Style:** All Python code adheres to `pycodestyle` (version 2.8.*)
* **Executable:** All Python scripts must be executable (`chmod +x <file>`)
* **First Line:** All Python files start with `#!/usr/bin/python3`

---

## Files & Task Summary

### Mandatory Tasks (0 – 28)

| File | Description |
| :--- | :--- |
| `0-answer.txt` | Built-in function used to print the type of an object |
| `1-answer.txt` | Built-in function used to get the memory address of an object |
| `2-answer.txt` | Do `a` and `b` point to the same object? (`a = 89`, `b = 100`) |
| `3-answer.txt` | Do `a` and `b` point to the same object? (`a = 89`, `b = 89`) |
| `4-answer.txt` | Do `a` and `b` point to the same object? (`a = 89`, `b = a`) |
| `5-answer.txt` | Do `a` and `b` point to the same object? (`a = 89`, `b = a`, `b = 90`) |
| `6-answer.txt` | Result of `s1 == s2` (`s1 = "Best"`, `s2 = "Best"`) |
| `7-answer.txt` | Result of `s1 is s2` |
| `8-answer.txt` | Result of `s1 == s2` (`s1 = "Best School"`, `s2 = "Best School"`) |
| `9-answer.txt` | Result of `s1 is s2` (String interning) |
| `10-answer.txt` | Result of `l1 == l2` (`l1 = [1, 2, 3]`, `l2 = [1, 2, 3]`) |
| `11-answer.txt` | Result of `l1 is l2` |
| `12-answer.txt` | Result of `l1 is l2` (`l1 = [1, 2, 3]`, `l2 = l1`) |
| `13-answer.txt` | Result of `l1 is l2` after list modification |
| `14-answer.txt` | Output of code appending an element using in-place modification |
| `15-answer.txt` | Output of code appending an element using list concatenation |
| `16-answer.txt` | Output of integer parameter mutation inside a function |
| `17-answer.txt` | Output of list parameter mutation inside a function |
| `18-answer.txt` | Output of rebinding a list parameter inside a function |
| `19-copy_list.py` | Python function `copy_list(l)` that returns a copy of a list |
| `20-answer.txt` | Is `a` a tuple? (`a = ()`) |
| `21-answer.txt` | Is `a` a tuple? (`a = (1, 2)`) |
| `22-answer.txt` | Is `a` a tuple? (`a = (1)`) |
| `23-answer.txt` | Is `a` a tuple? (`a = (1,)`) |
| `24-answer.txt` | Result of `a is b` (`a = (1)`, `b = (1)`) |
| `25-answer.txt` | Result of `a is b` (`a = (1, 2)`, `b = (1, 2)`) |
| `26-answer.txt` | Result of `a is b` (`a = ()`, `b = ()`) |
| `27-answer.txt` | Will `id(a)` be the same after `a = a + [5]`? |
| `28-answer.txt` | Will `id(a)` be the same after `a += [5]`? |

---

### Advanced Tasks (29 – 34)

| File | Description |
| :--- | :--- |
| `100-magic_string.py` | Function that returns `"BestSchool"` repeated `n` times separated by commas |
| `101-locked_class.py` | Class `LockedClass` with no attributes, preventing dynamic attribute creation except `first_name` |
| `103-line1.txt` & `103-line2.txt` | CPython memory questions on integer object allocation |
| `104-line1.txt` to `104-line5.txt` | Analysis of memory identity with larger integers outside the small integer cache |
| `105-line1.txt` | CPython small integer caching mechanism limits |
| `106-line1.txt` to `106-line5.txt` | CPython string interning and reference counting mechanics |

---

## Author
* **Hyacenthe Karinda**
