from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import InvalidCreatureError

def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    oppopents_count: int = len(opponents)
    print("*** Tournament ***")
    print(f"{oppopents_count} opponents involved")
    print()

    for i in range(oppopents_count):
        for j in range(i + 1, oppopents_count):
            print("* Battle *")
            opponent1 = opponents[i]
            opponent2 = opponents[j]
            
            factory1, strategy1 = opponent1
            factory2, strategy2 = opponent2

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                strategy1.act(creature1)
            except InvalidCreatureError as e:
                print(f"Battle error, aborting tournament: {e} '{factory1.name}' for this {strategy1.name.lower()} strategy")
                return
        
            try:
                strategy2.act(creature2)
            except InvalidCreatureError as e:
                print(f"Battle error, aborting tournament: {e} '{factory2.name}' for this {strategy2.name.lower()} strategy")
                return
            print()


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")

    opponents: list[tuple[CreatureFactory, BattleStrategy]] = [(flame_factory, normal_strategy), (healing_factory, defensive_strategy)]
    list_to_print: list[str] = []
    for factory, strategy in opponents:
        list_to_print.append(f"({factory.name}+{strategy.name})")
    print("[ ", end="")
    print(", ".join(list_to_print), end="")
    print(" ]")
    battle(opponents)

    print("\nTournament 1 (error)")
    opponents = [(flame_factory, aggressive_strategy), (healing_factory, defensive_strategy)]
    list_to_print: list[str] = []
    for factory, strategy in opponents:
        list_to_print.append(f"({factory.name}+{strategy.name})")
    print("[ ", end="")
    print(", ".join(list_to_print), end="")
    print(" ]")
    battle(opponents)

    print("\nTournament 2 (multiple)")
    opponents = [(aqua_factory, normal_strategy), (healing_factory, defensive_strategy), (transform_factory, aggressive_strategy)]
    list_to_print: list[str] = []
    for factory, strategy in opponents:
        list_to_print.append(f"({factory.name}+{strategy.name})")
    print("[ ", end="")
    print(", ".join(list_to_print), end="")
    print(" ]")
    battle(opponents)


if __name__ == "__main__":
    main()