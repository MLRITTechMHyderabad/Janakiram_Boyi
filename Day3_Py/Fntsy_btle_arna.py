import random

class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed

    def attack(self, target):
        damage = max(1, self.attack_power - target.defense)
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! Health left: {self.health}")

    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage = 0

    def attack(self, target):
        if self.health < 30:
            print(f" {self.name} enters Berserk Mode! Attack power doubled!")
            self.attack_power *= 2  
        super().attack(target)


class Mage(Character):
    def __init__(self, name, health, attack_power, defense, speed, mana):
        super().__init__(name, health, attack_power, defense, speed)
        self.mana = mana

    def fireball(self, target):
        if self.mana >= 20:
            damage = self.attack_power + 10
            target.take_damage(damage)
            self.mana -= 20
            self.health -= 5  
            print(f" {self.name} casts Fireball! Deals {damage} damage but loses 5 health!")
        else:
            print(f" {self.name} has insufficient mana! Attacks normally.")
            self.attack(target)

class Archer(Character):
    def __init__(self, name, health, attack_power, defense, speed, critical_chance):
        super().__init__(name, health, attack_power, defense, speed)
        self.critical_chance = critical_chance

    def attack(self, target):
        if random.randint(1, 100) <= self.critical_chance:
            damage = max(1, self.attack_power * 2 - target.defense)
            print(f" {self.name} lands a Critical Hit! Deals {damage} damage!")
        else:
            damage = max(1, self.attack_power - target.defense)
            print(f" {self.name} shoots an arrow! Deals {damage} damage.")
        target.take_damage(damage)


def sort_by_speed(fighter1, fighter2):
    if fighter1.speed > fighter2.speed:
        return [fighter1, fighter2]
    else:
        return [fighter2, fighter1]


def battle(fighter1, fighter2):
    fighters = sort_by_speed(fighter1, fighter2)
    print(f" Battle Begins: {fighter1.name} vs {fighter2.name}!")

    while fighter1.is_alive() and fighter2.is_alive():
        attacker = fighters[0]
        defender = fighters[1]

        
        if isinstance(attacker, Mage):
            attacker.fireball(defender)
        else:
            attacker.attack(defender)

        
        if not defender.is_alive():
            print(f" {defender.name} is defeated! {attacker.name} wins!")
            break

        fighters.reverse() 


def create_character(character_type):
    print(f"Creating a {character_type}!")
    name = input("Enter the character's name: ")
    health = int(input("Enter the health points: "))
    attack_power = int(input("Enter the attack power: "))
    defense = int(input("Enter the defense: "))
    speed = int(input("Enter the speed: "))

    if character_type == "Warrior":
        return Warrior(name, health, attack_power, defense, speed)
    elif character_type == "Mage":
        mana = int(input("Enter the mana points: "))
        return Mage(name, health, attack_power, defense, speed, mana)
    elif character_type == "Archer":
        critical_chance = int(input("Enter the critical hit chance (as a percentage): "))
        return Archer(name, health, attack_power, defense, speed, critical_chance)

print("Welcome to the Fantasy Battle Arena!")
fighter1 = create_character("Warrior")
fighter2 = create_character("Mage")

battle(fighter1, fighter2)