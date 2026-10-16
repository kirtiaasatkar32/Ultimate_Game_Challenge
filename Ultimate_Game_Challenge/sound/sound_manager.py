import winsound


def play_correct_sound():

    winsound.Beep(1000, 200)


def play_wrong_sound():

    winsound.Beep(400, 300)


def play_winning_sound():

    winsound.Beep(1000, 200)
    winsound.Beep(1200, 200)
    winsound.Beep(1500, 400)