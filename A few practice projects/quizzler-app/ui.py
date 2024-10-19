from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # set the data type to a quizbrain object
        self.quiz = quiz_brain
        self.score = self.quiz.score
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150, 125, text='Question goes here', font=('Arial', 20, 'italic',),
                                                width=280)
        self.create_canvas()
        self.Label = Label(text=f"Score: {self.score}/20", bg=THEME_COLOR, fg='white', padx=40, pady=40)
        self.Label.grid(row=0, column=1)

        self.green_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=self.green_image, padx=0, pady=40, highlightthickness=0,
                                  command=self.guess_answer_true)
        self.true_button.grid(row=2, column=0, )

        self.red_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=self.red_image, highlightthickness=0, command=self.guess_answer_false)
        self.false_button.grid(row=2, column=1, padx=0, pady=40)

        self.get_next_question()

        self.window.mainloop()

    def create_canvas(self):
        self.canvas.grid(row=1, column=0, columnspan=2)

    def guess_answer_true(self):
        answer = "True"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)
        self.window.after(2000, self.get_next_question)

    def guess_answer_false(self):
        answer = "False"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)
        self.window.after(2000, self.get_next_question)


    # def create_buttons(self):
    #     self.green_image = PhotoImage(file='./images/true.png')
    #     self.true_button = Button(image=self.green_image, padx=0, pady=40, highlightthickness=0,
    #                               command=self.guess_answer_true)
    #     self.true_button.grid(row=2, column=0, )
    #
    #     self.red_image = PhotoImage(file='./images/false.png')
    #     self.false_button = Button(image=self.red_image, highlightthickness=0, command=self.guess_answer_false)
    #     self.false_button.grid(row=2, column=1, padx=0, pady=40)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.Label.config(text= f" Score: {self.quiz.score}/20")
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You have reached the end of the quiz. Your final score is:\n "
                                                       f"{self.quiz.score}/20")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def change_colour_green(self):
        self.canvas.config(bg="green")

    def change_colour_red(self):
        self.canvas.config(bg="red")

    def give_feedback(self, is_right):
        if is_right:
            right = self.window.after(1000, self.change_colour_green)
        else:
            wrong = self.window.after(1000, self.change_colour_red)
