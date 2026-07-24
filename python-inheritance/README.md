# Python - Inheritance

## Description
This project covers the fundamentals of Object-Oriented Programming (OOP) in Python, focusing on **Inheritance**, superclasses, subclasses, method overriding, built-in function inspection (`dir()`, `type()`, `isinstance()`, `issubclass()`), and special methods/attribute management.

---

## Learning Objectives
* What is a superclass, base class, or parent class?
* What is a subclass?
* How to list available attributes and methods of a class or instance.
* When can an instance have new attributes?
* How to inherit a class from another class.
* How to define a class with multiple base classes.
* What is the default class every class inherits from?
* How to override a method or attribute inherited from the parent class.
* Which attributes or methods are available by heritage to subclasses?
* What is the purpose of `super()`?

---

## Requirements
* All files are interpreted/compiled on **Ubuntu 20.04 LTS** using **python3** (version 3.8.5).
* All code adheres to the **PEP 8** style guide.
* All files must be executable.
* All modules, classes, and functions must have proper docstrings.

---

## File Descriptions

| File | Description |
| --- | --- |
| `0-lookup.py` | Returns a list of available attributes and methods of an object. |
| `1-my_list.py` | A class `MyList` that inherits from `list` with a method `print_sorted()`. |
| `2-is_same_class.py` | Returns `True` if an object is *exactly* an instance of a specified class. |
| `3-is_kind_of_class.py` | Returns `True` if an object is an instance of, or inherited from, a specified class. |
| `4-inherits_from.py` | Returns `True` if an object is an instance of a class that inherited (directly or indirectly) from a specified class. |
| `5-base_geometry.py` | Defines an empty class `BaseGeometry`. |
| `6-base_geometry.py` | Expands `BaseGeometry` with an unimplemented `area()` method. |
| `7-base_geometry.py` | Adds `integer_validator(self, name, value)` to `BaseGeometry`. |
| `8-rectangle.py` | Class `Rectangle` that inherits from `BaseGeometry`. |
| `9-rectangle.py` | Complete `Rectangle` class with `area()` implementation and `__str__` representation. |
| `10-square.py` | Class `Square` that inherits from `Rectangle`. |
| `11-square.py` | Complete `Square` class with `__str__` representation. |
| `100-my_int.py` | Class `MyInt` inheriting from `int` with inverted `==` and `!=` operators. |
| `101-add_attribute.py` | Function that adds a new attribute to an object if possible. |
