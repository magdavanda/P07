from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy

def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    oppopents_count: int = len(opponents)
    print(f"{oppopents_count} opponents involved")
    print()
    print("* Battle *")

def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    creature1 = flame_factory.create_base()
    creature2 = healing_factory.create_base()
    opponents: list[tuple[CreatureFactory, BattleStrategy]] = [(creature1, normal_strategy), (creature2, defensive_strategy)]
    
    list_to_print: list[str] = []
    for creature, strategy in opponents:
        list_to_print.append(f"({creature.creature_name}+{strategy.name})")
    print("[ ", end="")
    print(", ".join(list_to_print), end="")
    print(" ]")

    battle(opponents)

    

if __name__ == "__main__":
    main()