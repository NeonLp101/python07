from ex0 import AquaFactory, FlameFactory, CreatureFactory

def verify(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())

def fight(factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
    print("Testing battle")
    base_a = factory_a.create_base()
    base_b = factory_b.create_base()
    print(base_a.describe())
    print("vs.")
    print(base_b.describe())
    print("fight!")
    print(base_a.attack())
    print(base_b.attack())

if __name__ == "__main__":
    verify(FlameFactory())
    verify(AquaFactory())
    fight(FlameFactory(), AquaFactory())