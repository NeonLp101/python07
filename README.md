# python07

42 Heilbronn — Python module 07: design patterns.

A trading-card creature game used to work through Abstract Factory and
capability mixins.

## Layout

```
ex0/                     Abstract Factory
├── _creature.py         Creature ABC + Flameling, Pyrodon, Aquabub, Torragon
├── factory.py           CreatureFactory ABC + FlameFactory, AquaFactory
└── __init__.py          exports the factories and the two ABCs only

ex1/                     Capabilities
├── _capability.py       HealCapability, TransformCapability
├── _creature.py         Sproutling, Bloomelle, Shiftling, Morphagon
├── factory.py           HealFactory, TransformFactory
└── __init__.py          exports factories and capability ABCs only

battle.py                ex0 scenario
capacitor.py             ex1 scenario
```

## Design notes

Neither script names a concrete creature class. `battle.py` and `capacitor.py`
talk to `CreatureFactory` and `Creature` only, so adding a new family means
writing a factory rather than editing the callers. The concrete creatures live
in underscore-prefixed modules and are never re-exported.

Capability classes deliberately do not inherit from `Creature` — they could be
mixed into anything. `TransformCapability` carries a class-level `transformed`
flag; calling `transform()` sets an instance attribute that shadows it, and
`attack()` branches on that flag to return a different string.

`ex1` imports `Creature` and `CreatureFactory` from `ex0` rather than
redefining them, so both packages share one class hierarchy.

## Running

```
python3 battle.py
python3 capacitor.py
```
