#!/usr/bin/python3
"""Defines the Base class, the foundation of every model in this project."""
import json
import csv


class Base:
    """Manages the id attribute for all subclasses to avoid duplication."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base, auto-assigning an id when none is given."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file."""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from the class JSON file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                dicts = cls.from_json_string(file.read())
        except IOError:
            return []
        return [cls.create(**d) for d in dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of objects to a CSV file named <Class>.csv."""
        filename = "{}.csv".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                d = obj.to_dictionary()
                writer.writerow([d[field] for field in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of instances from the class CSV file."""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    values = {k: int(v) for k, v in zip(fields, row)}
                    instances.append(cls.create(**values))
        except IOError:
            return []
        return instances
