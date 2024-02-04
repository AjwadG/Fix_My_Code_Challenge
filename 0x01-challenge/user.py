#!/usr/bin/python3
"""
User class
"""


class User():
    """ User class """

    def __init__(self):
        """ initializetion of user instance """
        self.__email = None

    @property
    def email(self):
        """ Email atr getter"""
        return self.__email

    @email.setter
    def email(self, value):
        """ email atr setter """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
