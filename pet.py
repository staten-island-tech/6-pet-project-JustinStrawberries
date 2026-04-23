class Dog:
    def __init__(self, name, happiness, toys, energy):
        self.name = name
        self.happiness = happiness
        self.toys = toys
        self.energy = energy

    def play(self, minutes):
        happy = minutes*2
        energy_used = minutes//2
        if self.energy >= energy_used:
            self.energy -= energy_used
            self.happiness += happy
            if self.happiness > 100:
                self.happiness = 100
                print(f"{self.name}, played fetch for {minutes} minutes!")
            return False
        else:
            print(f"Your pet's energy is too low to play for {minutes} minutes")
            return True


    def show_happiness(self):
        print(f"{self.name} has ${self.happiness}")

class Cat:
    def __init__(self, name, happiness, toys):
        self.name = name
        self.happiness = happiness
        self.toys = toys

    def play(self, minutes):
        happy = minutes*2
        self.happiness += happy
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name}, played chased a laser!")

    def show_happiness(self):
        print(f"{self.name} has ${self.happiness}")


Odie = Dog("Odie", 90, ["Bully Stick"], 10)
Fluffy = Dog("Fluffy", 20, ["Red Collar"], 20)
Mr_Meows = Cat("Mr. Meows", 45, [""])
Ms_Meows = Cat("Ms. Meows", 70, ["Fish"])


pet = Odie

print(Odie.__dict__)

while True:
    user_input = input(f"How many minutes do you to spend playing with {pet.name}? (max 60)")

    try:
        x = int(user_input)

        if 0 < x <= 60:
            break
        else:
            print('Enter a number from 1-60!')
    except ValueError:
        print('Not a viable input')
    

pet.play(x)
print(f"Odie has '{Odie.happiness}' happiness now.")
print(f"Odie has '{Odie.energy}' energy now.")



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