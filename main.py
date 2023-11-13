import json


if __name__ == "__main__":
    print("Black tower game")
    with open("test_paragraphs.json") as f:
        paragraphs_data = json.load(f)

    print(paragraphs_data)
