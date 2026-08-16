from ex0 import Creature
from ._capability import HealCapability, TransformCapability

class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"
    def heal(self) -> str:
        return "Sproutling heals herself"

class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals herself"

class Shiftling(Creature, TransformCapability):
    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."
    
    def transform(self) -> str:
        self.transformed = True
        return "Shiftling shifts into a sharper form!"
    
    def revert(self) -> str:
        self.transformed = False
        return "Shiftling returns to normal."

class Morphagon(Creature, TransformCapability):
    def attack(self) -> str:
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."
    
    def transform(self) -> str:
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"
    
    def revert(self) -> str:
        self.transformed = False
        return "Morphagon stabilizes its form."