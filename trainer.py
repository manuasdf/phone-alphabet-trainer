#!/usr/bin/python3
import sys
import json

# Import alphabets
german = open("./alphabets/german.json")
international = open("./alphabets/international.json")

dataSet = json.load(german)


def questionnaire():
    for entry in dataSet:
        while True:
            guess = input(entry['character'] + ": ")
            if guess == "q":
                exit()
            if guess == entry['word']:
                return

if __name__ == "__main__":
    questionnaire()
