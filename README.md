# DataDeck
A strategic card game featuring collectible creatures and turn-based battles, designed with the Abstract Factory and Strategy design patterns to ensure flexibility and extensibility.

# content 
 [EX0](#EX0)




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
              
