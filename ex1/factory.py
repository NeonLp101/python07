from ex0 import Creature, CreatureFactory
from ._creature import Sproutling, Bloomelle, Shiftling, Morphagon

class HealFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy")

class TransformFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")