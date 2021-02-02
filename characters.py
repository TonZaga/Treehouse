import random

class Warrior:
    melee = True

    def bruteForce(self):
        if self.bruteForce:
            return bool(random.randint(0, 1))
        return False