class Dog:
    def __init__(self, name, happiness, toys):
        self.name = name
        self.happiness = happiness
        self.toys = toys

    def play(self, minutes):
        happy = minutes*2
        self.happiness += happy
        print(f"{self.name}, played fetch!")

    def show_happiness(self):
        print(f"{self.name} has ${self.happiness}")

Odie = Dog("Odie", 90, ["Bully Stick"])


print(Odie.__dict__)

x = input(f"How many minutes do you to spend playing with {Dog.name}? '(max 60)'")

Odie.play(x)
print(f"Odie has '{Odie.happiness}' happiness now.")

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