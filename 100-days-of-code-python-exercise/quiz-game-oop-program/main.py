from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for el in question_data:
    new_question = Question(el['text'], el['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")