# class Item():
#     # vat_rate = .2
#
#     def __init__(self, price):
#         self.price = price
#
#     def calcVat(self):
#         return self.price * self.vat_rate


class Item():
    def __init__(self, price):
        self.price = price  # Remember to declare like this

    def calcVat(self, rate):
        return rate.calcVat(self)


class UkVat():
    vat_rate = .2

    def calcVat(self, item):
        return item.price * self.vat_rate
    # We have a separate class to represent the VAT rate for each region
    # we are operating.


class OntarioVat():
    vat_rate = .13

    def calcVat(self, item):
        return item.price * self.vat_rate

    # This also satisfies the single-use principle; an item is an item,
    # it shouldn't need to know its VAT rate because that is separate from the
    # item's price.
    # Similarly, because it shouldn't need to know its VAT rate it shouldn't
    # need to no how to calculate the value.
    # This fits in quite nicely with interface segregation (duck typing).


if __name__ == "__main__":
    item = Item(2.99)

    uk = UkVat()
    ontario = OntarioVat()

    print(item.calcVat(uk))
    print(item.calcVat(ontario))
