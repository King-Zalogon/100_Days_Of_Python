import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = tk.Label(text=f"Score: {self.quiz.score}", fg='white', bg=THEME_COLOR,font=('Arial', 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question Goes HERE",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=15)

        self.true_button = tk.Button()
        self.true_img = tk.PhotoImage(file="images/true.png")
        self.true_button.config(image=self.true_img, highlightthickness=0, pady=20, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button()
        self.false_img = tk.PhotoImage(file="images/false.png")
        self.false_button.config(image=self.false_img, highlightthickness=0, pady=20, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.update()

        else:
            self.canvas.config(bg='red')
            self.canvas.update()

        self.window.after(1000, self.get_next_question)
