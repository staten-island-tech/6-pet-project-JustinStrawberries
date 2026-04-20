class Dog:
    def __init__(self, name, happiness, toys):
        self.name = name
        self.__happiness = happiness
        self.toys = toys

    def play(self, amount):
        self.__happiness += amount

    def show_happiness(self):
        print(f"{self.name} has ${self.__happiness}")

Odie = Dog("Odie", 90, ["Bully Stick"])


print(Odie.__dict__)

Odie.play(10)

print(Odie.__dict__)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # double underscore means "private"

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"{self.owner} has ${self.__balance}")



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
# print(Justin.dict) skibidi:
# 