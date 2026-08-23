from . import creature
from abc import ABC, abstractmethod

class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> creature.Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> creature.Creature:
        ...


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        self.name = "Flameling"
    def create_base(self) -> creature.Creature:
        return creature.Flameling()
    
    def create_evolved(self) -> creature.Creature:
        return creature.Pyrodon()


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        self.name = "Aquabub"
    def create_base(self) -> creature.Creature:
        return creature.Aquabub()

    def create_evolved(self) -> creature.Creature:
        return creature.Torragon()

 