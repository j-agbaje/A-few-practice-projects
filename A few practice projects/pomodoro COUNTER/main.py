from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Define color constants for the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Set the font and the timer intervals (in minutes)
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Initialize variables to keep track of repetitions and checkmarks
reps = 1
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
# Function to reset the timer
def reset_timer():
    # Cancel the ongoing timer using the window's after_cancel method
    window.after_cancel(timer)
    # Reset the timer label text and color
    timer_label.config(text="Timer", fg=GREEN)
    # Reset the timer text on the canvas to 00:00
    canvas.itemconfig(timer_text, text='00:00')
    # Clear the checkmark label
    check_label.config(text='')
    # Reset the repetition counter
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
# Function to start the timer
def start_timer():
    # Access the global repetitions variable
    global reps
    # Convert the work, short break, and long break times to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If the current repetition is odd, start the work timer
    if reps % 2 != 0:
        countdown(work_sec)
        # Update the timer label to show "Focus" with the appropriate color
        timer_label.config(text="Focus", fg=RED)

    # If the current repetition is even and not a multiple of 8, start the short break timer
    if reps % 2 == 0 and reps % 8 != 0:
        countdown(short_break_sec)
        # Update the timer label to show "Short Break" with the appropriate color
        timer_label.config(text="Short Break", fg=GREEN)

    # If the current repetition is a multiple of 8, start the long break timer
    if reps % 8 == 0:
        countdown(long_break_sec)
        # Update the timer label to show "Long Break" with the appropriate color
        timer_label.config(text="Long Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Function to handle the countdown
def countdown(count):
    # Access the global variables for repetitions and checkmarks
    global reps
    global marks

    # Calculate the minutes and seconds remaining
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Format seconds to always show two digits
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update the timer text on the canvas
    if count >= 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
        # Set up the next call to countdown after 1 second
        timer = window.after(1000, countdown, count - 1)

    # When the countdown reaches zero, update repetitions and checkmarks
    if count == 0:
        reps += 1
        # Print the current number of repetitions for debugging purposes
        print(reps)
        # If the current repetition is even, add a checkmark
        if reps % 2 == 0:
            marks += '✔'
            check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Initialize the main application window
window = Tk()
window.title("Pomodoro Counter")
# Set up padding and background color for the window
window.config(padx=100, pady=50, bg=YELLOW)

# Create a canvas to hold the timer image and text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# Place the tomato image at the center of the canvas
canvas.create_image(100, 112, image=tomato_img)
# Create the text object for the timer and place it on the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

# Create a label for the timer title and place it above the canvas
timer_label = Label(text='Timer', fg=GREEN, font=("Times New Roman", 40), bg=YELLOW)
timer_label.grid(column=1, row=0)

# Create the start button and place it to the left of the canvas
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, borderwidth=0, command=start_timer)
start_button.grid(column=0, row=2)

# Create the reset button and place it to the right of the canvas
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Create the label for checkmarks and place it below the canvas
check_label = Label(fg=GREEN, font=20, bg=YELLOW)
check_label.grid(column=1, row=3)

# Start the Tkinter main event loop
window.mainloop()

