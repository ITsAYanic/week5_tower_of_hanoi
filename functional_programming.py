class Pillars:
    def __init__(self, number_of_plates: int = 3):
        self.pillar1 = []
        while number_of_plates > 0:
            self.pillar1.append(number_of_plates)
            number_of_plates -= 1
    
    pillar2 = []
    pillar3 = []

    def __repr__(self):
        return f"""Pillars:
        pillar1 = {self.pillar1}
        pillar2 = {self.pillar2}
        pillar3 = {self.pillar3}
        """


towers_of_hanoi = Pillars(4)
print(towers_of_hanoi)