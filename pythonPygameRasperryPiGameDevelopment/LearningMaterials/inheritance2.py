import os


class Foo(object):
    x = 0

    def __init__(self):
        print("Foo Constructor !")
        self.x = 10

    def printNumber(self):
        print(self.x)

        class Bar(Foo):
            def __init__(self):
                super(Bar, self).__init__()
                # What's going on here ?
                # The super method allows us to reference the base class;
                # however the base class needs to know 2 things :
                # the derived class type and the instance

                # You must always your base class's constructor
                # b4 you write any other code in your derived class's constructor.

                print("Bar Constructor !")

        b = Bar()
        b.printNumber()


f = Foo()
f.printNumber()
