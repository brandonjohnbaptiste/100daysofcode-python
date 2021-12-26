#!/usr/bin/env python3

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question['text'], question['answer']) for question in question_data]
quiz = QuizBrain(question_bank)

if __name__ == '__main__':
    while quiz.still_has_questions():
        quiz.next_question()

    print('You\'ve completed the quiz')
    print(f'Your final score was {quiz.score}/{quiz.question_number}')