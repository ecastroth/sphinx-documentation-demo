"""These are some docstrings for the File 2 insde the Package 1."""

from .subpackage1 import subfile2 as sp1f2

def someFunction1():
    """Some docstrings for a function inside the File 2, Package 1"""
    sp1f2.someFunction1()

def someFunction2():
    """Some docstrings for a function inside the File 2, Package 1"""
    sp1f2.someFunction2()
    pass

def someFunction3():
    """Some docstrings for a function inside the File 2, Package 1"""
    sp1f2.someFunction3()

def someFunction4():
    """Some docstrings for a function inside the File 2, Package 1"""
    sp1f2.someFunction4()

def someFunction5():
    """Some docstrings for a function inside the File 2, Package 1"""
    sp1f2.someFunction5()


class SomeClass1():
    """Some docstrings for the constructor of a class inside File 2, Package 1"""
    def __init__(self):
        self.some_class = sp1f2.SomeClass1()

    def someMethod1(self):
        """Some docstrings for a method inside a class from File 2, Package 1"""
        self.some_class.someMethod1()

    def someMethod2(self):
        """Some docstrings for a method inside a class from File 2, Package 1"""
        self.some_class.someMethod2()

    def someMethod3(self):
        """Some docstrings for a method inside a class from File 2, Package 1"""
        self.some_class.someMethod3()

    def someMethod4(self):
        """Some docstrings for a method inside a class from File 2, Package 1"""
        self.some_class.someMethod4()

    def someMethod5(self):
        """Some docstrings for a method inside a class from File 2, Package 1"""
        self.some_class.someMethod5()