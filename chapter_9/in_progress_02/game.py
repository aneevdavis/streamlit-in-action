from llm import Llm
from prompts import QUESTION_PROMPT, ANSWER_PROMPT
from answer_evaluation import AnswerEvaluation

class Game:
  def __init__(self, llm_api_key):
    self.llm = Llm(llm_api_key)

  def ask_llm_for_question(self):
    usr_msg, sys_msg = QUESTION_PROMPT['user'], QUESTION_PROMPT['system']
    return self.llm.ask(usr_msg, sys_msg)

  def ask_llm_to_evaluate_answer(self, question, answer):
    sys_msg = ANSWER_PROMPT['system']
    user_msg = (
      ANSWER_PROMPT['user']
      .replace('{question}', question)
      .replace('{answer}', answer)
    )
    return self.llm.ask(user_msg, sys_msg, AnswerEvaluation)
