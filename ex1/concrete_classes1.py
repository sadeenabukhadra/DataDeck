from ex0.creature import Creature
from .capabilities import HealCapability
from ex0.factory import CreatureFactory

class ConcreteClasses(Creature,HealCapability):
    def __init__(self)->self:
        Creature.__init__("Sproutling" , "Grass")
    def 