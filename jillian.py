# class Mage:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)

# Justin = Mage("Justin", 20, ["Gem"])
# Justin.buy({"title": "Wand", "atk": 2})
# print(Justin.__dict__)


class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Jillian = Hero("Jillian", 150, ["Potion"])

print (Jillian.__dict__)

Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__)