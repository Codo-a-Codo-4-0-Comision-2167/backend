# Una clase que NO se puede instanciar..

from abc import ABC, abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def do_something(self):
        pass

    @staticmethod
    def do_something_else():
        print("Doing something else")

class ConcreteClass(AbstractClass):

        def __init__(self, value):
             self.value = value

        def do_something(self):
            print("Doing something...")

class OtherClass(AbstractClass):

        def __init__(self, value):
             self.value = value

        def do_something(self):
            print("Doing something...")


class AnotherClass(OtherClass, ConcreteClass):
    
    def __init__(self) -> None:
        super().__init__()
    
    def do_something(self):
            print("Doing something...")

myInstance = ConcreteClass(10)

mySecondInstance = OtherClass(20)

myThirdInstance = OtherClass(20)

myList = [myInstance, mySecondInstance, myThirdInstance, mySecondInstance, myInstance]

for instance in myList:
    instance.do_something()

print(myInstance.do_something())

print(AbstractClass.do_something_else())