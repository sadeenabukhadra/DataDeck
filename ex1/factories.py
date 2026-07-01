from ex0.factory import CreatureFactory
from .heal_family import Sproutling, Bloomelle
from .transform_family import Shiftling, Morphagon
from ex0.creature import Creature


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
