#ADS ANTOINE 

import inquirer
import requests
import time

from opentdb import CATEGORIES
from helpers import extract_categories
from QuestionClass import Question
from helpers import clear

API_URL = "https://opentdb.com/api.php"



if __name__ == "__main__":
    SCORE = 0
    print("Hello, and welcome into Question Game!")
    print("Please, choose your topics first.")
    
    category_names = [category["name"] for category in CATEGORIES]
    category_names.insert(0, "ALL")
    
    questions = [inquirer.Checkbox(
    'topics',
    message="With what topics do you want to play ?",
    choices=category_names,
    ),
    inquirer.Text('rounds', message="How many rounds ?"),]
    answers = inquirer.prompt(questions)

    if answers['rounds'] == "" or int(answers['rounds']) < 1 or int(answers['rounds']) > 50 or answers['rounds'] == "0" or answers['rounds'] == " ":
        answers['rounds'] = "10"
    if answers['topics'] == []:
        answers['topics'] = ["ALL"]
    
    if "ALL" in answers['topics']:
        API_URL += "?amount=" + answers['rounds']
    
    if "ALL" not in answers['topics']:
        API_URL += "?amount=" + answers['rounds'] + "&category=" + ",".join(str(x) for x in extract_categories(answers['topics']))
            
    while True:
        response = requests.get(API_URL)
        data = response.json()
        
        if data['response_code'] == 5:
            print("Your going to fast ! Please wait 10 seconds before trying again.")
            time.sleep(10)
            continue 
        else:
            break
    
    questions = data['results']
    
    clear()
    for question in questions:
        q = Question(question['question'], question['correct_answer'], question['incorrect_answers'])
        q.ask_question()
        does_it_pass = q.ask_answers()
        if does_it_pass:
            SCORE += 1
    
    if SCORE < 0:
        SCORE = 0
    clear()
    print("Your score is: " + str(SCORE))
            
    
    
    
  