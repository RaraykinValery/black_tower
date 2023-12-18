from typing import NamedTuple
from character import Character
import json
import random


class paragraphs_types(NamedTuple):
    prod: str = "all_paragraphs.json"
    test: str = "test_paragraphs.json"
    test_normal: str = "test_normal_paragraphs.json"


def test_luck() -> str:
    if character.luck >= random.randint(2, 12):
        return "luck"
    else:
        return "unluck"


def play_level(level):
    paragraph = paragraphs_data["paragraphs"][level]
    print(paragraph["text"])

    if paragraph["state"] != "continue":
        return None
    else:
        if paragraph["luck_test"]["proposed"] == "yes":
            answer: str = input("Хотите проверить удачу? [да/нет] ")
            if answer.lower == "да":
                luck_test_result = test_luck()
                if luck_test_result == "luck":
                    print("Вы удачливы!")
                else:
                    print("Удача в этот раз отвернулась от вас.")
            else:
                luck_test_result = "unluck"

            luck_data = paragraph["luck_test"][luck_test_result]
            match luck_data["action"]:
                case "go to":
                    return luck_data["paragraph"]
                case "characteristics_tweak":
                    character.change_characteristic(
                        luck_data["characteristic"], luck_data["value"]
                    )
                    character.print_characteristics()

            character.change_characteristic("luck", -1)

        character.set_characteristic("punch_power_tweak", 0)
        next_paragraph = input("You are going to: ")
        return next_paragraph


paragraphs_types = paragraphs_types()

with open(paragraphs_types.test_normal) as f:
    paragraphs_data = json.load(f)

character: Character = Character()
print("Характеристики персонажа:")
character.print_characteristics()
print()

if __name__ == "__main__":
    print("Black tower game\n")

    level = "54"

    while True:
        level = play_level(level)

        if not level:
            break
