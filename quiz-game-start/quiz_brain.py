class QuizBrain:
    def __init__(self,qlist):
        self.question_number = 0
        self.score = 0
        self.question_list = qlist
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_a = input(f"Q.{self.question_number}:{current_question.question} (True/False): ")
        self.check_answer(user_a,current_question.answer)
        print(f"Your current score is {self.score}/{self.question_number}")
    def still_has_question(self):
        return self.question_number<len(self.question_list)

    def check_answer(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("YOU GOT IT RIGHT!!!")
            self.score+=1
        else:
            print("That's Wrong!!!")
        print(f"The correct answer is {correct_ans}")