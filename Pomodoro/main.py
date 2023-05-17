# from email.mime import image
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        # If It's the 8th rep:
        count_down(long_break_min)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        # If It's the 2nd/4th/6th rep:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        # If It's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # if count_min < 10:
    #     count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔"
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=130, bg=YELLOW)

# Show Timer Text
title_label = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start = Button(text="Start", font=(FONT_NAME, 10, "bold"),
               command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

# Reset Button
rest = Button(text="Reset", font=(FONT_NAME, 10, "bold"),
              highlightthickness=0, command=reset_timer)
rest.grid(column=2, row=2)

# Check Mark
check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

"""HINT1 : use fg to color the foreground"""
"""HINT2 : copy-paste the checkmark symbol"""
"""HINT3 : Use to grid method for create a position in a tabular form"""

window.mainloop()
