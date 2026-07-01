from typing import cast
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    base = factory.create_base()
    evolved = factory.create_evolved()

    heal_base = cast(HealCapability, base)
    heal_evolved = cast(HealCapability, evolved)

    print("base:")
    print(base.describe())
    print(base.attack())
    print(heal_base.heal())

    print("\nevolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(heal_evolved.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")

    base = factory.create_base()
    evolved = factory.create_evolved()

    transform_base = cast(TransformCapability, base)
    transform_evolved = cast(TransformCapability, evolved)

    print("base:")
    print(base.describe())
    print(base.attack())
    print(transform_base.transform())
    print(base.attack())
    print(transform_base.revert())

    print("\nevolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(transform_evolved.transform())
    print(evolved.attack())
    print(transform_evolved.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(healing_factory)
    test_transform(transform_factory)
