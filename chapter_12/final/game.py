import time

from llm import Llm
from prompts import QUESTION_PROMPT, ANSWER_PROMPT
from answer_evaluation import AnswerEvaluation

class Game:
  def __init__(self, llm_api_key, settings):
    self.llm = Llm(llm_api_key)
    self.settings = settings
    self.status = 'GET_QUESTION'

    self.curr_question = None
    self.curr_answer = None
    self.curr_eval = None

    self.score = 0
    self.num_questions_completed = 0
    self.max_questions = 5
    self.questions = []

  def get_setting(self, setting_name):
    return self.settings[setting_name][0]

  def modify_settings(self, new_settings):
    self.settings = new_settings

  def ask_llm_for_question(self):
    seed = int(time.time())
    sys_msg = (
      QUESTION_PROMPT['system']
      .replace('{quizmaster}', self.get_setting('Quizmaster'))
    )
    usr_msg = (
      QUESTION_PROMPT['user']
      .replace('{already_asked}', '\n'.join(self.questions))
      .replace('{seed}', str(seed))
      .replace('{difficulty}', self.get_setting('Difficulty'))
    )
    return self.llm.ask(usr_msg, sys_msg, temperature=0.7, top_p=0.9)

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
    self.questions.append(self.curr_question)
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

  def proceed_to_next_question(self):
    self.status = 'GET_QUESTION'

  def is_over(self):
    return self.num_questions_completed >= self.max_questions

