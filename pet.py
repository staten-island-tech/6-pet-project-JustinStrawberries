class Pet:
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
    
    def show_stats(self):
        return(f"{self.name} | Happiness: {self.happiness} | Energy: {self.energy}")
    
    
def get_minutes_for_play(pet):
    while True:
        user_input = input(f"How many minutes do you to spend playing with {pet.name}? (max 60): ")

        try:
            x = int(user_input)

            if 0 < x <= 60:
                print (f"You played with {pet.name} for {x} minutes!")
                return x
            else:
                print('Enter a number from 1-60!')
        except ValueError:
            print('Not a viable input')

def get_hours_for_rest(pet):
    while True:
        user_input = input(f"How many hours do you want {pet.name} to rest for? (max 12): ")

        try:
            x = int(user_input)

            if 0 < x <= 12:
                return x
            else:
                print('Enter a number from 1-12!')
        except ValueError:
            print('Not a viable input')



Odie = Pet("Odie", 90, ["Bully Stick"], 10)
Fluffy = Pet("Fluffy", 20, ["Red Collar"], 20)
Mr_Meows = Pet("Mr. Meows", 45, [""])
Ms_Meows = Pet("Ms. Meows", 70, ["Fish"])


pet = Odie

print(Odie.__dict__)

while True:
    print(f"\nWhat do you want to do with {pet.name}?")
    print("1. Play")
    print("2. Rest")
    print("3. Show Stats")
    print("4. Quit")

    choice = input("Enter a Choice: ")

    if choice == "1":
        user_input = get_minutes_for_play(pet)
        pet.play(user_input)

    if choice == "2":
        user_input = get_hours_for_rest(pet)
        pet.rest(user_input)

    if choice == "3":
        print(pet.show_stats())
        print()
        input("Press enter to return to menu")
        
        

    # if choice == "4":








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

