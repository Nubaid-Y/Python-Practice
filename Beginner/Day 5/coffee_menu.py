class CoffeeMenu:
    def __init__(self):
        self.menu = {
        'espresso': 2.50,
        'latte': 2.75,
        'cappuccino': 3.20,
        'americano': 2.70
        }

    def getprice(self,item):
        return self.menu[item]

    def additem(self, item, price):
        self.menu[item] = price