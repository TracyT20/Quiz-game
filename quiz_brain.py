import html
class Quizbrain:
    def __init__(self,question_list):
        self.question_number=0
        self.score = 0
        self.question_list=question_list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_qtn=self.question_list[self.question_number]
        self.question_number += 1
        quiz_txt=html.unescape(self.current_qtn.text)
        return (f"Q{self.question_number}: { quiz_txt} ")

    def check_answer(self,user_answer):
        correct_answer=self.current_qtn.answer
        print(correct_answer)
        if str(user_answer)==correct_answer:
            return True
            # self.score+=1
        else:
            return False

