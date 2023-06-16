"""
There is class name DescriptiveQuestion and inherits the class Question.
"""

from question import Question

class DescriptiveQuestion(Question):

    def __init__(self, text):
        self.text = text

    def update(self, new_text):
        self.text = new_text