#!/usr/bin/env python3
import json
import string
import argparse

parser = argparse.ArgumentParser(description='Find borked translations')
parser.add_argument('files', type=str, nargs='*')
args = parser.parse_args()

for file in args.files:
	with open(file) as jsonData:
		data = json.load(jsonData)
		for text, translation in data.items():
			translation = translation.rstrip()
			if (
					(len(translation) < len(text) and len(text) - len(translation) > 10 and translation[-1].lower() in string.ascii_letters) or
				 	translation[-1] in string.ascii_uppercase and translation[-2] not in string.ascii_uppercase
				):
				print(file)
				print(text)
				print(translation)
				print()
