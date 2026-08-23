from ex0 import CreatureFactory
from ex0 import creature
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        return Sproutling()
    
    def create_evolved(self) -> creature.Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        return Shiftling()
    
    def create_evolved(self) -> creature.Creature:
        return Morphagon()