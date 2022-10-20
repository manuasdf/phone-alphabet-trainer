#!/usr/bin/python3
import sys
import json

# Import alphabets
german = open("./alphabets/german.json")
international = open("./alphabets/international.json")

dataSet = json.load(german)


def questionnaire():
    for letter in dataSet
    while True:
        guess = input(dataSet['A'] + ": ")
        if guess == "q":
            exit()
        else guess == dataSet['']:
            return

if __name__ == "__main__":
    questionnaire()
