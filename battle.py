# from ex0 import CreatureFactory, FlameFactory, AquaFactory
import ex0


def factory_check(factory: ex0.CreatureFactory) -> None:
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def base_fight(flame_factory: ex0.FlameFactory,
               aqua_factory: ex0.AquaFactory
               ) -> None:
    base_flame = flame_factory.create_base()
    base_aqua = aqua_factory.create_base()
    print(base_flame.describe())
    print(" vs.")
    print(base_aqua.describe())
    print(" fight!")
    print(base_flame.attack())
    print(base_aqua.attack())


def main() -> None:
    print("Testing factory")

    factory_flame = ex0.FlameFactory()
    factory_aqua = ex0.AquaFactory()

    factory_check(factory_flame)
    print("\nTesting factory")
    factory_check(factory_aqua)

    print()
    print("Testing battle")
    base_fight(factory_flame, factory_aqua)


if __name__ == "__main__":
    main()
