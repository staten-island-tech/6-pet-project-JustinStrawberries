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

    def rest(self, hours):
        energizing = hours*10
        self.energy += energizing
        print(f"{self.name}, slept for {hours} hours!")
        return False
    
    
def get_minutes_for_play(pet):
    while True:
        user_input = input(f"How many minutes do you to spend playing with {pet.name}? (max 60): ")

        try:
            x = int(user_input)

            if 0 < x <= 60:
                return x
            else:
                print('Enter a number from 1-60!')
        except ValueError:
            print('Not a viable input')
    
# pet.play(x)
# print(f"Odie has {pet.happiness} happiness now.")
# print(f"Odie has {pet.energy} energy now.")

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
        print(f"{self.name} has {self.happiness} happiness")



Odie = Dog("Odie", 90, ["Bully Stick"], 10)
Fluffy = Dog("Fluffy", 20, ["Red Collar"], 20)
Mr_Meows = Cat("Mr. Meows", 45, [""])
Ms_Meows = Cat("Ms. Meows", 70, ["Fish"])


pet = Odie

print(Odie.__dict__)

while True:
    print(f"\nWhat do you want to do with {pet.name}?")
    print("1. Play")
    print("2. Rest")
    print("3. Show happiness")
    print("4. Quit")

    choice = input("Enter a Choice")

    if choice == "1":
        minutes = get_minutes_for_play(pet)





def get_minutes_for_play(pet):
    while True:
        user_input = input(f"How many minutes do you to spend playing with {pet.name}? (max 60): ")

        try:
            x = int(user_input)

            if 0 < x <= 60:
                return x
            else:
                print('Enter a number from 1-60!')
        except ValueError:
            print('Not a viable input')
    
pet.play(x)
print(f"Odie has {Odie.happiness} happiness now.")
print(f"Odie has {Odie.energy} energy now.")

