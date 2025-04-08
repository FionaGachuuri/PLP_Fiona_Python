#!/usr/bin/env python3
"""
A class to represent a person.
This class is used to create a person object with a username, email, id and age.
It includes methods to get the username, email, id and age of the person.
It also includes a method to get the string representation of the person object.
"""
class Person:
    """
    A class to represent a person.

    Attributes
    ----------
    username : str
        the username of the person
    email : str
        the email of the person
    id : int
        the id of the person
    age : int
        the age of the person
    """

    def __init__(self, username, email, id, age):
        self.username = username
        self.email = email
        self.id = id
        self.age = age

    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be a string")
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        if "@" not in value:
            raise ValueError("Email must contain '@'")
        if value.count("@") != 1:
            raise ValueError("Email must contain only one '@'")
        self._email = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be an integer")
        if value < 0:
            raise ValueError("ID must be a positive integer")
        self._id = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

    def __str__(self):
        return f"Person(username={self.username}, email={self.email}, id={self.id}, age={self.age})"


class Admin(Person):
    """
    A class to represent an admin.
    """
    
    def __init__(self, username, email, id, age, permissions=None):
        super().__init__(username, email, id, age)
        self.admin = True
        self.permissions = permissions or ["read", "write", "execute"]
    
    def get_permissions(self):
        return self.permissions
    
    def set_permissions(self, permissions):
        if not isinstance(permissions, list):
            raise TypeError("Permissions must be a list")
        for permission in permissions:
            if not isinstance(permission, str):
                raise TypeError("Permission must be a string")
        self.permissions = permissions

    def __str__(self):
        return f"Admin(username={self.username}, email={self.email}, id={self.id}, age={self.age}, permissions={self.permissions})"
        
if __name__ == "__main__":
    try:
        p = Admin("josekk", "josekk@gmail.com", 34456, 35)
        print(p)
    except TypeError as e:
        print(f"TypeError: {e}")