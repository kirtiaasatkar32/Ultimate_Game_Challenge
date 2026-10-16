import tkinter as tk
from tkinter import messagebox

from rich.console import Console
from rich.panel import Panel
#from rich import print

from student.student_manager import select_student

from games.logical_game import get_logical_questions
from games.riddle_game import get_riddle_questions
from games.python_quiz import get_python_questions

from score.scoreboard import calculate_score
from score.scoreboard import level_passed
from score.scoreboard import final_level_passed

from sound.sound_manager import play_correct_sound
from sound.sound_manager import play_wrong_sound
from sound.sound_manager import play_winning_sound

from gui.interface import create_gui


console = Console()


student_name = select_student()

level1 = get_logical_questions()
level2 = get_riddle_questions()
level3 = get_python_questions()


console.print(
    Panel(
        "[bold yellow]ULTIMATE GAME CHALLENGE[/bold yellow]",
        title="[bold cyan]WELCOME[/bold cyan]",
        border_style="green"
    )
)


console.print(
    f"[bold cyan]Selected Student:[/bold cyan] "
    f"[bold green]{student_name}[/bold green]"
)


console.print("\n[bold magenta]GAME LEVELS[/bold magenta]")

console.print(
    f"[cyan]Level 1 - Logical:[/cyan] {len(level1)} questions"
)

console.print(
    f"[green]Level 2 - Riddle:[/green] {len(level2)} questions"
)

console.print(
    f"[blue]Level 3 - Python Quiz:[/blue] {len(level3)} questions"
)


create_gui(
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
)