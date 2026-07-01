# DataDeck
A strategic card game featuring collectible creatures and turn-based battles, designed with the Abstract Factory and Strategy design patterns to ensure flexibility and extensibility.

# content 
 [EX0](#EX0)
 [EX1](#EX1)




 # Ex0
ex0 — Creature Factory
Overview

This project implements the Abstract Factory design pattern to create and manage different families of creatures.
Each factory is responsible for creating a base creature and its evolved form.

The goal is to separate object creation from object usage, ensuring that the client code does not depend on concrete classes.
 
 Design Pattern

This project uses the Abstract Factory Pattern.

- Factories are responsible for creating related objects.

- Creatures are grouped into families.

- The client interacts only with factories.

Classes

Creature (Abstract Class)

Base class for all creatures.

Attributes:
              
                name: str
                creature_type: str
Methods:
  
              attack() -> str (abstract)
              describe() -> str (concrete)

Creatures
* Fire Family

- Flameling (base creature)

-Pyrodon (evolved creature)
* Water Family

- Aquabub (base creature)
- Torragon (evolved creature)

Each creature implements its own attack() method.

* Factories
-CreatureFactory (Abstract) : Defines the interface for all factories.

Methods:
 - create_base() -> Creature
 - create_evolved() -> Creature

* FlameFactory

Creates:
- Flameling (base)
- Pyrodon (evolved)

*AquaFactory

Creates:

- Aquabub (base)
- Torragon (evolved)


Restrictions
 - The package must NOT expose concrete creature classes.
 - Only factories must be accessible from outside the package.

Usage

The battle.py script is used to test the package.

It:

1) Creates factories
2) Generates base and evolved creatures
3) Calls describe() and attack()
4) Simulates a battle between creatures

*Example Output
                         
                      Testing factory
                      Flameling is a Fire type Creature
                      Flameling uses Ember!
                      Pyrodon is a Fire/Flying type Creature
                      Pyrodon uses Flamethrower!

                     Testing factory
                     Aquabub is a Water type Creature
                     Aquabub uses Water Gun!
                     Torragon is a Water type Creature
                     Torragon uses Hydro Pump!

                     Testing battle
                     Flameling is a Fire type Creature
                     vs.
                     Aquabub is a Water type Creature
                     fight!
                     Flameling uses Ember!
                     Aquabub uses Water Gun!

                    
                     
Project Structure
                        
                        ex0/
                           ├── __init__.py
                           ├── creature.py
                           ├── factory.py
                           ├── flame_factory.py
                           ├── aqua_factory.py

                       battle.py              

# EX1

##  Overview

This exercise extends the previous Creature system (ex0) by introducing **capabilities** using multiple inheritance.

Instead of binding abilities directly to creatures, we separate behaviors into independent interfaces:

- HealCapability
- TransformCapability

This makes the system more flexible, reusable, and extensible.

---

##  Main Idea

In ex0, creatures had fixed behaviors.

In ex1, we apply:

> "Composition through Capabilities instead of rigid inheritance"

This means:
- A creature can have healing ability OR transformation ability OR both
- Abilities are not tied to a specific creature type

---

##  Architecture

### 1. Capabilities (Interfaces)

#### HealCapability
Defines healing behavior:

- `heal(target=None) -> str`

Used by creatures that can heal themselves or others.

---

#### TransformCapability
Defines transformation behavior:

- `transform() -> str`
- `revert() -> str`
- Maintains internal state:
  - `self.transformed: bool`

This state affects the creature’s `attack()` behavior.

---

##  Creature Families

### Healing Family

These creatures inherit:
- Creature
- HealCapability

#### Sproutling
- Base grass creature
- Heals itself

#### Bloomelle
- Advanced grass/fairy creature
- Stronger healing ability

---

###  Transform Family

These creatures inherit:
- Creature
- TransformCapability

#### Shiftling
- Normal type creature
- Attack changes when transformed

#### Morphagon
- Normal/Dragon type creature
- Stronger transformed attacks

---

##  Factories

To enforce encapsulation, creatures are NOT created directly.

Instead, we use factories:

### HealingCreatureFactory
Creates:
- `Sproutling` (base)
- `Bloomelle` (evolved)

---

### TransformCreatureFactory
Creates:
- `Shiftling` (base)
- `Morphagon` (evolved)

---

##  Design Restrictions

- Concrete creatures must NOT be imported outside the package
- Only factories are exposed via `ex1/__init__.py`
- This enforces abstraction and encapsulation

---

## ⚔️ Behavior Summary

### Healing Creatures
- can attack normally
- can heal using `heal()`

### Transform Creatures
- can attack normally
- can transform using `transform()`
- attack behavior changes when transformed
- can revert back using `revert()`

---

## State Logic

For Transform creatures:

- Default state: `transformed = False`
- After `transform()` → True
- After `revert()` → False

Attack behavior depends on this state.

---

##  Learning Goals

This exercise teaches:

- Multiple inheritance
- Interface separation
- State-based behavior design
- Factory pattern extension
- Encapsulation (hiding concrete classes)

---

Instead of designing rigid creatures, we now design:

> Flexible creatures built from independent capabilities.

This makes the system scalable and easy to extend in future exercises.
