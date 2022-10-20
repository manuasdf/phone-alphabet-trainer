#!/usr/bin/python3
import sys
import json
import random

# Import alphabets
german = open("./alphabets/german.json")
international = open("./alphabets/international.json")

dataSet = json.load(german)


def questionnaire(set, randomized = True, exclude = []):
    for entry in set:
        while True:
            if randomized:
                entry = random.choice(set)
            guess = input(entry['character'] + ": ")
            if guess == "q":
                exit()
            if guess == entry['word']:
                break

if __name__ == "__main__":
    questionnaire(dataSet)
