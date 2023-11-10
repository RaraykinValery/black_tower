import json
import re


file: str = "/home/valery/Code/black_tower/content/adventure_paragraphs.txt"
final_dict: dict = {"paragraphs": {}}
number_line_re: re.Pattern = re.compile(r'^\d*$')

with open(file) as f:
    for line in f:
        paragraph_number = number_line_re.match(line)

        if paragraph_number
