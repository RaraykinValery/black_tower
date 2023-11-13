import json
import re


file: str = "./raw_book_files/adventure_paragraphs.txt"
final_dict: dict = {"paragraphs": {}}
number_line_re: re.Pattern = re.compile(r'^\d*$')

f = open(file)
lines = f.readlines()
paragraph = {}
paragraph_number = 0

for i, line in enumerate(lines):
    number_match = number_line_re.match(line)

    if number_match:
        paragraph = {
            "text": "",
            "enemies": [],
            "luck test": {},
            "handicap": {},
            "spells": [],
            "next_paragraphs": [],
            "state": "continue"
        }
        paragraph_number = number_match
    else:
        paragraph["text"] += line
        if len(lines) - 1 == i or number_line_re.match(lines[i+1]):
            final_dict["paragraphs"][paragraph_number.group(0)] = paragraph

f.close()

print(json.dumps(final_dict, indent=4, ensure_ascii=False))
