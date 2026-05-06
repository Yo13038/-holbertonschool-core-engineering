#!/usr/bin/env python3

def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == {}:
        return None

    best_name = list(a_dictionary.keys())[0]

    for name, score in a_dictionary.items():
        if score > a_dictionary[best_name]:
            best_name = name

    return best_name
