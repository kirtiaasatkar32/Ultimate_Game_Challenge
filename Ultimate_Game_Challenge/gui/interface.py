import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def create_gui(
    student_name,
    level1,
    level2,
    level3,
    calculate_score,
    level_passed,
    final_level_passed,
    play_correct_sound,
    play_wrong_sound,
    play_winning_sound
):

    window = tk.Tk()

    window.title("Ultimate Game Challenge")
    window.geometry("700x500")


    title = tk.Label(
        window,
        text="🎮 ULTIMATE GAME CHALLENGE",
        font=("Arial", 24, "bold")
    )

    title.pack(pady=30)


    student = tk.Label(
        window,
        text="Student: " + student_name,
        font=("Arial", 16)
    )

    student.pack(pady=10)


    tabs = ttk.Notebook(window)

    home = tk.Frame(tabs)
    game = tk.Frame(tabs)
    score = tk.Frame(tabs)

    tabs.add(home, text="Home")
    tabs.add(game, text="Game")
    tabs.add(score, text="Score")

    tabs.pack(
        expand=True,
        fill="both"
    )


    welcome = tk.Label(
        home,
        text="Welcome to the Game!",
        font=("Arial", 18, "bold")
    )

    welcome.pack(pady=40)


    score_text = tk.Label(
        score,
        text="SCORE\n\n0 / 40",
        font=("Arial", 32, "bold")
    )

    score_text.pack(
        expand=True
    )


    scores = []


    def play_level(level_number, questions, final=False):

        correct_answers = 0

        game_window = tk.Toplevel()

        game_window.title("Ultimate Game Challenge")

        game_window.geometry("700x500")

        question_number = 0


        title = tk.Label(
            game_window,
            text="LEVEL " + str(level_number),
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)


        question_text = tk.Label(
            game_window,
            text="",
            font=("Arial", 16),
            wraplength=600
        )

        question_text.pack(pady=20)


        selected_answer = tk.StringVar()


        options_frame = tk.Frame(game_window)

        options_frame.pack(pady=10)


        result_text = tk.Label(
            game_window,
            text="",
            font=("Arial", 12)
        )

        result_text.pack(pady=10)


        def show_question():

            selected_answer.set("")

            question = questions[question_number]


            question_text.config(
                text=str(question_number + 1) +
                ". " +
                question["question"]
            )


            for widget in options_frame.winfo_children():

                widget.destroy()


            for option in question["options"]:

                radio = tk.Radiobutton(
                    options_frame,
                    text=option,
                    variable=selected_answer,
                    value=option,
                    font=("Arial", 13)
                )

                radio.pack(
                    anchor="w",
                    pady=5
                )


        def submit_answer():

            nonlocal question_number
            nonlocal correct_answers


            answer = selected_answer.get()


            if answer == "":

                messagebox.showinfo(
                    "Answer",
                    "Please select an answer."
                )

                return


            correct_answer = questions[question_number]["answer"]


            if answer == correct_answer:

                correct_answers += 1

                result_text.config(
                    text="Correct!"
                )

                play_correct_sound()


            else:

                result_text.config(
                    text="Wrong!"
                )

                play_wrong_sound()


            question_number += 1


            if question_number < 5:

                game_window.after(
                    500,
                    show_question
                )


            else:

                score = calculate_score(
                    correct_answers
                )

                scores.append(score)

                game_window.destroy()


                if final:

                    if final_level_passed(
                        correct_answers
                    ):

                        play_winning_sound()

                        total = sum(scores)


                        score_text.config(
                            text="FINAL SCORE\n\n" +
                            str(total) +
                            " / 40"
                        )


                        messagebox.showinfo(
                            "Congratulations",
                            "You Won!\n\n"
                            "Level 4 Score: " +
                            str(score) +
                            "\nFinal Score: " +
                            str(total) +
                            " / 40"
                        )


                    else:

                        total = sum(scores)


                        score_text.config(
                            text="FINAL SCORE\n\n" +
                            str(total) +
                            " / 40"
                        )


                        messagebox.showinfo(
                            "Game Over",
                            "You did not complete Level 4.\n\n"
                            "Final Score: " +
                            str(total) +
                            " / 40"
                        )


                else:

                    if level_passed(
                        correct_answers
                    ):

                        start_next_level(
                            level_number + 1
                        )


                    else:

                        total = sum(scores)


                        score_text.config(
                            text="FINAL SCORE\n\n" +
                            str(total) +
                            " / 40"
                        )


                        messagebox.showinfo(
                            "Game Over",
                            "You need 4 correct answers "
                            "to continue.\n\n"
                            "Your Score: " +
                            str(total) +
                            " / 40"
                        )


        submit = tk.Button(
            game_window,
            text="SUBMIT ANSWER",
            font=("Arial", 13, "bold"),
            bg="#3498DB",
            fg="white",
            padx=20,
            pady=8,
            command=submit_answer
        )

        submit.pack(pady=20)


        show_question()


    def start_next_level(level_number):

        if level_number == 2:

            play_level(
                2,
                level2
            )

        elif level_number == 3:

            play_level(
                3,
                level3,
                True
            )
    def start_game():

        scores.clear()

        score_text.config(
            text="SCORE\n\n0 / 40"
        )


        play_level(
            1,
            level1
        )


    start = tk.Button(
        home,
        text="▶ START GAME",
        font=("Arial", 16, "bold"),
        command=start_game
    )

    start.pack(pady=20)


    window.mainloop()