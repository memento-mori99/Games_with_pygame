class MyBaseClass(object):
    def methodOne(self):
        print("MyBaseClass::methodOne()")


class MyChildClass(object):
    """ When a class derives from another class, remember to the base class's name
    in parentheses after your new class's name"""

    def methodOne(self):
        print("MyChildClass::methodOne()")


def callMethodOne(obj):
    obj.methodOne()


instance_1 = MyBaseClass()
instance_2 = MyChildClass()

callMethodOne(instance_1)
callMethodOne(instance_2)


# callMethodOne(5)
# The above will not work because "int" object does not contain a method called methodOne
# Python uses a technique called duck typing.


# this means that when Python sees a method call on an object, it assumes that the
# message can passed to it.
# The benefit of this technique is that inheritance is almost superseded by a
# technique called programming to the interface.

# Programming to the interface means that you don't need to worry about
# the internal workings of the object; you just need to know what methods are available.

# Programming to the interface
class Dog(object):
    def makeNoise(self):
        print("Woof !")


class Duck(object):
    def makeNoise(self):
        print("Quack !")


animals = [Dog(), Duck()]

for a in animals:
    a.makeNoise()
