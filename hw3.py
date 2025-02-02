import random

class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
    
    def use(self):
        return self.attack_power
    
    def __str__(self):
        return self.name

class Monster:
    def __init__(self, name, health, attack_power, weapon1, weapon2):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapons = [weapon1, weapon2]
        self.current_weapon = weapon1
    
    def attack(self):
        damage = self.attack_power + self.current_weapon.use()
        print(f"{self.name} attacks with {self.current_weapon} causing {damage} damage!")
        return damage
    
    def switch_weapon(self):
        self.current_weapon = self.weapons[1] if self.current_weapon == self.weapons[0] else self.weapons[0]
        print(f"{self.name} switched to {self.current_weapon}.")
    
    def __str__(self):
        return f"Monster: {self.name}, HP: {self.health}, Attack Power: {self.attack_power}, Current Weapon: {self.current_weapon}"

class CorruptedHuman(Monster):
    def __init__(self, name, health, attack_power, weapon1, weapon2, corruption_level):
        super().__init__(name, health, attack_power, weapon1, weapon2)
        self.corruption_level = corruption_level
    
    def unleash_corruption(self):
        corruption_damage = self.attack_power * (1 + self.corruption_level / 100)
        print(f"{self.name} unleashes corruption, dealing {corruption_damage:.2f} damage!")
        return corruption_damage
    
    def __str__(self):
        return f"Corrupted Human: {self.name}, HP: {self.health}, Attack Power: {self.attack_power}, Corruption Level: {self.corruption_level}%, Current Weapon: {self.current_weapon}"

# สร้างอาวุธ
weapons_list = [
    Weapon("Rusty Sword", 5), Weapon("Shadow Dagger", 8),
    Weapon("Corrupt Claw", 10), Weapon("Blood Spear", 12)
]

# สร้างมอนสเตอร์ 20 ตัว
monsters = []
for i in range(20):
    name = f"Humanity {i+1}"
    health = random.randint(50, 100)
    attack_power = random.randint(10, 20)
    weapon1, weapon2 = random.sample(weapons_list, 2)
    
    if i % 3 == 0:
        corruption_level = random.randint(10, 50)
        monster = CorruptedHuman(name, health, attack_power, weapon1, weapon2, corruption_level)
    else:
        monster = Monster(name, health, attack_power, weapon1, weapon2)
    
    monsters.append(monster)

# ทดสอบการเรียกใช้ methods
for monster in monsters:
    print(monster)
    monster.attack()
    monster.switch_weapon()
    if isinstance(monster, CorruptedHuman):
        monster.unleash_corruption()
    print("-" * 40)