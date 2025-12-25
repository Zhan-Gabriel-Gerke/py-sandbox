import Enemy, random

class Ogre(Enemy.Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre", health_points=health_points, attach_damage=attack_damage)

    def talk(self):
        print("Ogre is slamming hands all around.")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attach_damage += 4
            print("Ogre attack has increased by 4!")

    def attack(self):
        print("Ogre attacks!")