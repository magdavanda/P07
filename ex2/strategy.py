from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability

class InvalidCreatureError(Exception):
    def __init__(self, message: str = "Invalid Creature") -> None:
        self.message = message
        super().__init__(message)

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
            print(creature.attack())
        else:
            return
    
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "Aggressive"
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise InvalidCreatureError

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "Defensive"
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise InvalidCreatureError("Invalid Creature!")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)



    