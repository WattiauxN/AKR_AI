from dumper import Dumper

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        self._name = name

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self._age = age
    
    def fonct(self):
        return 0

class MyClass1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."

    def farewell(self):
        return f"Goodbye from {self.name}."

    def __str__(self):
        return f"MyClass(name={self.name})"

    def __private_method(self):
        return "This is a private method."

class MyClass2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__private_attr = "This is private"

    def greet(self):
        return f"Hello, my name is {self.name}."

    def __str__(self):
        return f"MyClass(name={self.name}, age={self.age})"

person = Person(30,30)
dumper = Dumper()


print(dumper.print_dump(person))
print(dumper.dump(person))
print(dumper.get_instance_method(person))
# print(Dumper.dump_methods(MyClass2))
# print(Dumper.dump_methods(MyClass1))
# print(Dumper.dump_methods(Person))
print(dumper.dump_methods(MyClass2))
print(dumper.dump_methods(MyClass1))
print(dumper.dump_methods(Person))
print(dumper.dump_attributes(person))