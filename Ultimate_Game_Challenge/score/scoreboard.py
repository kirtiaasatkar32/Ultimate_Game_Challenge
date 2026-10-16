def calculate_score(correct_answers):
    score = correct_answers * 2
    return score


def level_passed(correct_answers):
    if correct_answers >= 4:
        return True
    else:
        return False


def final_level_passed(correct_answers):
    if correct_answers == 5:
        return True
    else:
        return False


def total_score(scores):
    total = sum(scores)
    return total