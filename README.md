# DataDeck

A strategic card game featuring collectible creatures and turn-based battles, designed using **Abstract Factory**, **Capabilities**, and **Strategy design patterns**.  
The goal is to build a flexible and extensible system where object creation, abilities, and battle logic are fully decoupled.

---

#  Contents

- [EX0 — Creature Factory](#ex0--creature-factory)
- [EX1 — Capabilities System](#ex1--capabilities-system)
- [EX2 — Abstract Strategy Tournament](#ex2--abstract-strategy-tournament)

---

#  EX0 — Creature Factory

Implements the **Abstract Factory Design Pattern** to create families of creatures.

Each factory is responsible for creating:
- A base creature
- An evolved creature

The goal is to separate object creation from usage.

---

## Design Pattern

### Abstract Factory Pattern
- Factories create related objects
- Creatures are grouped into families
- Client interacts only with factories

---

##  Creature Base Class

### Creature (Abstract)

**Attributes:**
- name: str
- creature_type: str

**Methods:**
- attack() → str (abstract)
- describe() → str (concrete)

---

##  Creature Families

###  Fire Family
- Flameling (base)
- Pyrodon (evolved)

###  Water Family
- Aquabub (base)
- Torragon (evolved)

---

##  Factories

### CreatureFactory (Abstract)
- create_base()
- create_evolved()

### FlameFactory
- Flameling
- Pyrodon

### AquaFactory
- Aquabub
- Torragon

---

##  Restrictions

- Concrete creatures must NOT be exposed outside the package
- Only factories are accessible externally

---

##  Usage

`battle.py`:
1. Create factories
2. Generate creatures
3. Call describe() and attack()
4. Simulate battle

---

##  Structure


ex0/
├── init.py
├── creature.py
├── factory.py
├── flame_factory.py
├── aqua_factory.py

battle.py


---

# EX1 — Capabilities System

Extends EX0 by introducing **capabilities** using multiple inheritance.

Abilities are separated from creatures to improve flexibility.

---

##  Main Idea

> "Behavior is independent from the creature"

---

## Capabilities

### HealCapability

         heal(target=None) -> str

TransformCapability
        
         transform() -> str
         revert() -> str

Includes state:

        self.transformed: bool
 
Healing Family
- Sproutling
- Bloomelle

Capabilities:
 - Heal
 - Attack

Transform Family
- Shiftling
- Morphagon

Capabilities:
 - Transform
 - Attack (changes with state)
- Revert

Factories
 - HealingCreatureFactory
 - Sproutling
 - Bloomelle

TransformCreatureFactory
 - Shiftling
 - Morphagon
Rules
No direct access to concrete creatures
Only factories are exposed
*Learning Goals
1) Multiple inheritance
2) Interface separation
3) State-based behavior
4) Factory extension

 
 
# EX2 — Abstract Strategy Tournament
Implements the Strategy Pattern to manage battle behavior dynamically.

Each creature is paired with a strategy.

- Main Idea

"The strategy defines how a creature fights"

BattleStrategy Interface
            
            is_valid(creature) -> bool
            act(creature) -> None
Strategies :
1) NormalStrategy
 - attack only
2) AggressiveStrategy
 - transform → attack → revert
3) DefensiveStrategy
 - attack → heal


Tournament Flow
1) Create factories
2) Assign strategies
3) Generate creatures
4) Run battles
5) Delegate logic to strategies

 
- Error Handling

         If invalid pairing:

         Battle error, aborting tournament: Invalid Creature 'X'

 Structure
          
          ex2/
          ├── battlestrategy.py
          ├── concreteclasses.py
          ├── __init__.py

          tournament.py
 
# Learning Goals
 - Strategy pattern
 - Runtime behavior selection
 - Clean architecture
 - Decoupled design

