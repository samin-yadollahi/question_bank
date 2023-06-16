"""
Getting the inputs from user
"""

from question import Question
from descriptive_question import DescriptiveQuestion
from optional_question import OptionalQuestion

def descriptive_question_input():

    text = input("Type a new question:\n")
    question_content = DescriptiveQuestion(text)
    return question_content
    


def optional_question_input():

    text = input("Please enter the question text:\n")
    option = input("Please enter the option:\n")
    question_content = OptionalQuestion(text, option)
    return question_content


