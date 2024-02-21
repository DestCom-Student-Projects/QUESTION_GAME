from os import system, name 
from opentdb import CATEGORIES

def clear(): 
    if name == 'nt': 
        x = system('cls') 
    else: 
        x = system('clear') 


def extract_categories(answers):
    if "ALL" in answers:
        return None
    else:
        return [category["id"] for category in CATEGORIES if category["name"] in answers]
