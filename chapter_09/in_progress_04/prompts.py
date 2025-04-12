QUESTION_PROMPT = {
  'system': 'You are a quizmaster.',
  'user': 'Ask a trivia question. Do not provide choices or the answer.'
}

ANSWER_PROMPT = {
  'system': 'You are an expert quizmaster.',
  'user': '''
    You have asked the following question: {question}
    The player answered the following: {answer}

    Evaluate if the answer provided by the player is close enough
    to be correct.
    
    Also, provide the correct answer.
  '''
}