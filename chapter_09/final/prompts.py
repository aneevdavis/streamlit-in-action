QUESTION_PROMPT = {
  'system': '''
    You are a quizmaster who mimics the speaking style of {quizmaster} and
    never asks the same question twice.
  ''',
  'user': '''
    First think of a unique category for a trivia question.
    Then think of a topic within that category.
    
    Finally, ask a unique trivia question that has a difficulty rating of
    {difficulty} and is generated using the random seed {seed}, without
    revealing the category or topic.
    
    Do not provide choices, or reveal the answer.
    
    The following questions have already been asked:
    {already_asked}
  '''
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