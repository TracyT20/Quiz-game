from tkinter import *
from quiz_brain import Quizbrain
THEME_COLOR="#375362"
class QuizInterface:
    def __init__(self,quiz_brain:Quizbrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas=Canvas(height=250,width=300,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.question_text=self.canvas.create_text(150,125,text="put in som text quiz",font=("Arial",20,"italic"),width=280,fill=THEME_COLOR)
        self.true_image=PhotoImage(file="true.png")
        self.False_image = PhotoImage(file="false.png")
        self.true_button=Button(image=self.true_image,highlightthickness=0,command=self.check_if_correct)
        self.true_button.grid(row=2,column=0)
        self.False_button = Button(image=self.False_image, highlightthickness=0,command=self.check_if_wrong)
        self.False_button.grid(row=2, column=1)
        self.score_text=Label(self.window,text="Score: 0",font=("Arial",10),bg=THEME_COLOR,fg="white")
        self.score_text.grid(row=0,column=1)
        self.get_next_guestion()

        self.window.mainloop()
    def get_next_guestion(self):
            self.canvas.config(bg="white")
            if self.quiz.still_has_questions():
                q_text=self.quiz.next_question()
                self.canvas.itemconfig(self.question_text,text=q_text)
            else:
                self.canvas.itemconfig(self.question_text,text="You've reached the end of the Quiz")
                self.true_button.config(state="disabled")
                self.False_button.config(state="disabled")
    def check_if_correct(self):
        self.give_feedback(self.quiz.check_answer(True))

    def check_if_wrong(self):
        self.give_feedback(self.quiz.check_answer(False))
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.quiz.score += 1
            self.score_text.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_guestion)







