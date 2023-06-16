"""
This class is going to create questions, which included Descriptive and optional Questions.
It is needed to have update method for every single question.
"""
from abc import ABC

class Question(ABC):

    def __init__(self, text):
        self.text

