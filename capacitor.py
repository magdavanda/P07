# from ex1 import HealingCreatureFactory, TransformCreatureFactory
import ex1


def main() -> None:
    print("Testing Creature with healing capability")

    healing_factory = ex1.HealingCreatureFactory()
    print(" base:")
    healing_base = healing_factory.create_base()
    print(healing_base.describe())
    print(healing_base.attack())
    print(healing_base.heal())

    print(" evolved:")
    healing_evolved = healing_factory.create_evolved()
    print(healing_evolved.describe())
    print(healing_evolved.attack())
    print(healing_evolved.heal())

    print()
    print("Testing Creature with transform capability")
    print(" base:")
    transform_factory = ex1.TransformCreatureFactory()
    transform_base = transform_factory.create_base()
    print(transform_base.describe())
    print(transform_base.attack())
    print(transform_base.transform())
    print(transform_base.attack())
    print(transform_base.revert())

    print(" evolved:")
    transform_evolved = transform_factory.create_evolved()
    print(transform_evolved.describe())
    print(transform_evolved.attack())
    print(transform_evolved.transform())
    print(transform_evolved.attack())
    print(transform_evolved.revert())


if __name__ == "__main__":
    main()
