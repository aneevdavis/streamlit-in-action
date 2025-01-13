from llm import Llm
from prompts import QUESTION_PROMPT, ANSWER_PROMPT
from answer_evaluation import AnswerEvaluation

class Game:
  def __init__(self, llm_api_key):
    self.llm = Llm(llm_api_key)
    self.status = 'GET_QUESTION'

    self.curr_question = None
    self.curr_answer = None
    self.curr_eval = None

    self.score = 0
    self.num_questions_completed = 0
    self.max_questions = 1

  def ask_llm_for_question(self):
    usr_msg, sys_msg = QUESTION_PROMPT['user'], QUESTION_PROMPT['system']
    return self.llm.ask(usr_msg, sys_msg)

  def ask_llm_to_evaluate_answer(self):
    sys_msg = ANSWER_PROMPT['system']
    user_msg = (
      ANSWER_PROMPT['user']
      .replace('{question}', self.curr_question)
      .replace('{answer}', self.curr_answer)
    )
    reply = self.llm.ask(user_msg, sys_msg, AnswerEvaluation)
    return reply

  def obtain_question(self):
    self.curr_question = self.ask_llm_for_question()
    self.status = 'ASK_QUESTION'
    return self.curr_question

  def accept_answer(self, answer):
    self.curr_answer = answer
    self.status = 'EVALUATE_ANSWER'

  def evaluate_answer(self):
    self.curr_eval = self.ask_llm_to_evaluate_answer()
    self.num_questions_completed += 1
    if self.curr_eval.is_correct:
      self.score += 1
    self.status = 'STATE_RESULT'

  def is_over(self):
    return self.num_questions_completed >= self.max_questions