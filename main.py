from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
from UI import QuizInterface

question_bank=[]
for i in question_data:
    new_q=Question(i["question"],i["correct_answer"])
    question_bank.append(new_q)

new_quiz=Quizbrain(question_bank)
quiz_ui=QuizInterface(new_quiz)
# while new_quiz.still_has_questions():
#     new_quiz.next_question()
#     print("\n")
# print("You've completed the quiz."
#       f"\nYour final score is {new_quiz.score}/{new_quiz.question_number}")

