from ex1 import TransformFactory, HealFactory

healfactory = HealFactory()
transformfactory = TransformFactory()

base_heal = healfactory.create_base()
evolved_heal = healfactory.create_evolved()

base_transform = transformfactory.create_base()
evolved_transform = transformfactory.create_evolved()

if __name__ == "__main__":
    print("base:")
    print(base_heal.describe())
    print(base_heal.attack())
    print(base_heal.heal())
    print("evolved:")
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    print(evolved_heal.heal())
    print("Transform:")
    print("base:")
    print(base_transform.describe())
    print(base_transform.attack())
    print(base_transform.transform())
    print(base_transform.attack())
    print(base_transform.revert())
    print("evolved:")
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    print(evolved_transform.transform())
    print(evolved_transform.attack())
    print(evolved_transform.revert())