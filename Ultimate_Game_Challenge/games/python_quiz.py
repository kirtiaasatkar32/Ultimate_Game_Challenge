import random

from data.python_questions import questions


def get_python_questions():
    selected_questions = random.sample(questions, 5)
    return selected_questions