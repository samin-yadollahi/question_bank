"""
There is a class named OptionalQuestion and inherits the class Question.
"""

from question import Question

class OptionalQuestion(Question):

    def __init__(self, text, option):
        self.text = text
        self.option = option

    def update(self, new_text, new_option):
        self.text = new_text
        self.option = new_option