class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    @name.deleter
    def name(self):
        del self._name

    @age.deleter
    def age(self):
        del self._age


user = User
user.name = 'John'
user.age = 30
print(user.name)
print(user.age)
del user.name
del user.age
print(user.name)
print(user.age)
# The @classmethod decorator is used to define class methods.

# The @property decorator is used to define properties in a class.

