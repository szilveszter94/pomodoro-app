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
timer = None
marks = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
# this function reset the timer and check marks
def reset_timer():
    global marks
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="Timer", fg=GREEN)
    reps = 0
    check_box.config(text="")


# reset timer and increase the sessions by 1
def start_timer():
    global reps
    reps += 1

    # config work and break period
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        text_label.config(text="Break", fg=RED)
        count_down(long_break_min)
    elif reps % 2 == 0:
        text_label.config(text="Break", fg=PINK)
        count_down(short_break_min)
    else:
        text_label.config(text="Work", fg=GREEN)
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# set counter
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # format seconds below 10 e.g 9 to 09 format
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # check if remaining time is greater than 0
    if count >= 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    # if remaining time is 0 reset the timer and checks the session with a green mark
    else:
        global marks
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
            check_box.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# set screen
window = Tk()
# config screen
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
# image
tomato = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato)
# buttons
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=3, row=3)
# check box
check_box = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_box.grid(column=1, row=4)
# timer text label
text_label = Label(text="Timer", font=("BioRhyme", 30, "bold"), fg=GREEN, bg=YELLOW)
text_label.grid(column=1, row=0)
# time label
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=("Impact", 25, "normal"))
canvas.grid(column=1, row=1)
# refresh the screen
window.mainloop()
