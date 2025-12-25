import Zombie, Ogre, Enemy, Hero, Weapon

def battle(e):
    e.talk()
    e.special_attack()


# zombie = Zombie.Zombie(10, 10)
# zombie.talk()
# zombie.spread_disease()
# print(zombie.get_type_of_enemy())

ogre = Ogre.Ogre(10, 10)
# ogre.talk()
# print(ogre.get_type_of_enemy())


def battle(e1: Enemy, e2:Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        e1.special_attack()
        e2.special_attack()
        e2.attack()
        e1.health_points -= e2.attach_damage
        e1.attack()
        e2.health_points -= e1.attach_damage

    if e1.health_points > 0:
        print("Enemy 1 wins!")
    else:
        print("Enemy 2 wins!")



def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        enemy.special_attack()
        enemy.attack()
        hero.health_points -= enemy.attach_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    if hero.health_points > 0:
        print("Hero wins!")
    else:
        print("Enemy 2 wins!")

zombie = Zombie.Zombie(10, 1)
hero = Hero.Hero(10, 1)
weapon = Weapon.Weapon("Sword", 5)
hero.weapon = weapon
hero.equipWeapon()
hero_battle(hero, zombie)