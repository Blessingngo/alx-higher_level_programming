#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.
        Args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {b: getattr(self, b) for b in attrs if hasattr(self, b)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for b, v in json.items():
            setattr(self, b, v)
