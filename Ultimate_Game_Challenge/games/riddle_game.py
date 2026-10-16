import random

from data.riddle_questions import questions


def get_riddle_questions():
    selected_questions = random.sample(questions, 5)
    return selected_questions