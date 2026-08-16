from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealFactory, TransformFactory
from ex2 import (
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]
                creature_a = factory_a.create_base()
                creature_b = factory_b.create_base()
                print("* Battle *")
                print(creature_a.describe())
                print("vs.")
                print(creature_b.describe())
                print("now fight!")
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory(), normal), (HealFactory(), defensive)])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(FlameFactory(), aggressive), (HealFactory(), defensive)])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), normal),
        (HealFactory(), defensive),
        (TransformFactory(), aggressive),
    ])