class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass

    def move(self):
        pass

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def make_sound(self):
        return "Mammal sound"

    def give_birth(self):
        return "Giving birth to live young"

class Bird(Animal):
    def __init__(self, name, habitat, feather_color):
        super().__init__(name, habitat)
        self.feather_color = feather_color

    def make_sound(self):
        return "Bird song"

    def lay_eggs(self):
        return "Laying eggs"

class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def make_sound(self):
        return "Fish bubbles"

    def lay_eggs(self):
        return "Laying eggs in water"

mammal = Mammal(name="Lion", habitat="Grasslands", fur_color="Golden")
print(f"{mammal.name} in {mammal.habitat} has fur color {mammal.fur_color}. {mammal.make_sound()}. {mammal.give_birth()}.")
bird = Bird(name="Eagle", habitat="Mountains", feather_color="Brown")
print(f"{bird.name} in {bird.habitat} has feather color {bird.feather_color}. {bird.make_sound()}. {bird.lay_eggs()}.")
fish = Fish(name="Salmon", habitat="Rivers", scale_color="Silver")
print(f"{fish.name} in {fish.habitat} has scale color {fish.scale_color}. {fish.make_sound()}. {fish.lay_eggs()}.")