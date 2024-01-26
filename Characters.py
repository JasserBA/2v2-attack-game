import random

class Character:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health

    def calculate_attack(self):
        return self.strength
    
    def attack(self):
        return self.attack
    
    def hit(self, points):
        if ((self.health-points) > 0):
            self.health -= points
            return True
        else :
            return False

    def isAlive(self):
        return self.health > 0 
    
    def print_info(self):
        print(f"Name: {self.name}, Strength: {self.strength}, Health: {self.health}")


class Character1(Character):
    def __init__(self, name, strength, health):
        super().__init__(name, strength, health)
    def calculate_attack(self):
        return self.strength + random.randint(2, 10)

class Character2(Character):
    def __init__(self, name, strength, health):
        super().__init__(name, strength, health)
    def calculate_attack(self):
        return self.strength + random.randint(4, 10)

class Character3(Character):
    def __init__(self, name, strength, health):
        super().__init__(name, strength, health)
    def calculate_attack(self):
        return self.strength + random.randint(6, 10)
    


