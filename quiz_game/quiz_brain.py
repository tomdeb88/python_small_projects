class QuizBrain:
    def __init__(self,given_list):
        self.question_number=0
        self.question_list=given_list
        self.score=0

    def still_has_questions(self):
        if self.question_number ==len(self.question_list):
            return False
        else:
            return True



    def get_question(self):
        next_q=self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"Q.{self.question_number}: {next_q.text} (True/False)?: ")
        self.check_answer(answer,next_q.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")



