from typing import Any
from .battlestrategy import BattleStrategy


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Any) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Any) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return hasattr(creature, "transform")

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}'\
                   for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revent())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any):
        return hasattr(creature, "heal")

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}' \
                for this defensive strategy")
        print(creature.heal())
        print(creature.attack())
