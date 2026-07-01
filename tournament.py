from typing import cast
from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import TransformCapability, HealCapability
from ex2.battlestrategy import BattleStrategy
from ex2.concreteclasses import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures = []

    # create creatures
    for factory, strategy in opponents:
        creatures.append((factory.create_base(), strategy))

    # all vs all
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):

            c1, s1 = creatures[i]
            c2, s2 = creatures[j]

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                if not s1.is_valid(c1) or not s2.is_valid(c2):
                    raise Exception("Invalid matchup")

                s1.act(c1)
                s2.act(c2)

            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":

    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    tournament = [
        (flame, normal),
        (heal, defensive),
        (transform, aggressive),
    ]

    battle(tournament)
