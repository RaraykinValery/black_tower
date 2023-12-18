import random


class Character():
    def __init__(self):
        self.skill = random.randint(7, 12)
        self.stamina = random.randint(14, 24)
        self.luck = random.randint(7, 12)
        self.punch_power_tweak = 0

        self.spells = []

    def print_characteristics(self) -> None:
        print(f"Мастерство: {self.skill}")
        print(f"Выносливость: {self.stamina}")
        print(f"Удача: {self.luck}")
        print(f"Изменение силы удара: {self.punch_power_tweak}")

    def change_characteristic(self, characteristic: str, value: int) -> None:
        match characteristic:
            case "skill":
                self.skill += value
            case "stamina":
                self.stamina += value
            case "luck":
                self.luck += value
            case "punch_power_tweak":
                self.punch_power_tweak += value

    def set_characteristic(self, characteristic: str, value: int) -> None:
        match characteristic:
            case "skill":
                self.skill = value
            case "stamina":
                self.stamina = value
            case "luck":
                self.luck = value
            case "punch_power_tweak":
                self.punch_power_tweak = value


if __name__ == "__main__":
    c = Character()
    c.print_characteristics()
