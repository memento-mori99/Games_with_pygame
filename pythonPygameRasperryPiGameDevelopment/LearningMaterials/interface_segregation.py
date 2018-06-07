class Duck():
    def Quack(self):
        print("Quack Duck !")


class Person():
    def Quack(self):
        print("Quack Person !")


def makeItQuack(duck):
    duck.Quack()


duck = Duck()
person = Person()

makeItQuack(duck)
makeItQuack(person)
