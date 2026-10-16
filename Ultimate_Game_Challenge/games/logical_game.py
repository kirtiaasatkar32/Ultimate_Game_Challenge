import random

from data.logical_questions import questions


def get_logical_questions():

    selected_questions = random.sample(questions, 5)

    return selected_questions