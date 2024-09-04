import abc
import math

class Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def m1(self):
        return

    @staticmethod
    @abc.abstractmethod
    def m2():
        return

    @classmethod
    @abc.abstractmethod
    def m3(cls):
        return


class MyClass(Base):
    def m1(self):
        print('m1')

    def m2(self):
        print('m2')

    def m3(self):
        print('m3')

m = MyClass()
m.m1()
m.m2()
m.m3()


