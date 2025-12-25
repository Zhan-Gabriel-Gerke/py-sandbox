class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attach_damage: int = 1

    def __init__(self, type_of_enemy, health_points, attach_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attach_damage = attach_damage

    def talk(self):
        print(f"I am an {self.__type_of_enemy}!")

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def special_attack(self):
        print("Enemy does not have a special attack")

    def attack(self):
        print("Zombie has attacks")
