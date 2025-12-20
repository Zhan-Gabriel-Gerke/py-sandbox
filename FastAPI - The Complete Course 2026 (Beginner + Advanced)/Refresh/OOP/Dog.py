import Animal

class Dog(Animal.Animal):
    can_shed: bool
    domestic_name: str

    def talk(self):
        print("Bark")

    def eat(self):
        print("Chews on bone!")