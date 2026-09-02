from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidCreatureError(Exception):
    def __init__(self, message: str = "Invalid Creature") -> None:
        self.message = message
        super().__init__(message)


class BattleStrategy(ABC):
    name: str

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "Normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            return


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "Aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise InvalidCreatureError


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.name = "Defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())
        else:
            raise InvalidCreatureError
