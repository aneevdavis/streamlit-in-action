from llm import Llm

class Game:
  def __init__(self, llm_api_key):
    self.llm = Llm(llm_api_key)

  def ask_llm_for_question(self):
    return self.llm.ask(
      'Ask a trivia question. Do not provide choices or the answer.',
      'You are a quizmaster.'
    )