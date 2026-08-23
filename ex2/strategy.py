from abc import ABC, abstractmethod
from ex0.creature import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...
    
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "Normal"
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            attack = creature.attack()
            print(attack)
        else:
            return
    
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "Aggressive"
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            transform = creature.transform()
            attack = creature.attack()
            revert = creature.revert()
        else:
            raise InvalidCreatureError("Invalid creature!")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "Defensive"
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            attack = creature.attack()
            heal = creature.heal()
        else:
            raise InvalidCreatureError("Invalid Creature!")

    def is_valid(self, creature: Creature) -> None:
        return isinstance(creature, HealCapability)



    