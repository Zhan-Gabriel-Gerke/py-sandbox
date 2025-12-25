import random

import Enemy
class Zombie(Enemy.Enemy):
    def __init__(self, health_point, attack_damage):
        super().__init__(type_of_enemy="Zombie", health_points=health_point, attach_damage=attack_damage)

    def talk(self):
        print("*Grumbling..")

    def spread_disease(self):
        print("The zombie is trying to spread disease")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 2
            print("Zombie regenerated 2 HP!")