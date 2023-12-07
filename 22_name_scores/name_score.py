import json
import logging

CAPITAL_NUMBER_KEY = 64


def load_names(filename: str):
    try:
        with open(filename, "r") as file:
            loaded_data = json.load(file)
            names = loaded_data.get("names")
            return assign_scores(names)
    except Exception as e:
        logging.error("There was an error loading the names")
    return None


def assign_scores(names):
    list_of_name_scores = []
    i = 0
    names.sort()
    for name in names:
        i += 1
        score_counter = 0
        characters = ([*name])
        for character in characters:
            score_counter += ord(character) - CAPITAL_NUMBER_KEY
        list_of_name_scores.append(score_counter * i)
    return list_of_name_scores


def score_names(filename):
    return sum(
        load_names(
            filename
        )
    )


print(score_names("names.txt"))
