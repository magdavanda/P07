from .capabilities import HealCapability, TransformCapability
from ex0.creature import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformation_check is False:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        self.transformation_check = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.transformation_check = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformation_check is False:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.transformation_check = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformation_check = False
        return "Morphagon stabilizes its form."
