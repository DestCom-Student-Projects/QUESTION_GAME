import inquirer

from helpers import clear

class Question():
    def __init__(self, question, correct_answer, incorrect_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        
    def ask_question(self):
        clear()
        print("The question is: ")
        print(self.question)
        
    def ask_answers(self):
        while True:
            questions = [inquirer.Checkbox(
            'answers',
            message="What is/are the answer(s) ?",
            choices=self.incorrect_answers + [self.correct_answer],
            )]
            answers = inquirer.prompt(questions)
            
            if answers['answers'] == []:
                clear()
                print("Please, select at least one answer.")
                print(self.question)
                continue
            
            verify = self.verify_answer(answers['answers'])
            if verify:
                print("Correct !")
                return True
            else:
                print("Incorrect !")
                return False
        
        
    def verify_answer(self, answer):
        return answer[0] == self.correct_answer