from pydantic import BaseModel

class AnswerEvaluation(BaseModel):
  is_correct: bool
  correct_answer: str
