#!/usr/bin/python3
"""
Defines the Base class for managing unique identifiers.
"""
import json
import csv


class Base:
    """Base class for all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="", encoding="utf-8") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [
                    {k: int(v) for k, v in d.items()}
                    for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all Rectangles and Squares using Turtle graphics."""
        import turtle

        screen = turtle.Screen()
        screen.title("Almost a Circle")

        pen = turtle.Turtle()
        pen.speed(0)

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()

            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()

            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()
