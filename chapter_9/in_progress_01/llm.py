from openai import OpenAI

class Llm:
  def __init__(self, api_key):
    self.client = OpenAI(api_key=api_key)

  @staticmethod
  def construct_messages(user_msg, sys_msg=None):
    messages = []
    if sys_msg:
      messages.append({"role": "system", "content": sys_msg})
    messages.append({"role": "user", "content": user_msg})
    return messages

  def ask(self, user_msg, sys_msg=None):
    messages = self.construct_messages(user_msg, sys_msg)
    completion = self.client.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages
    )
    return completion.choices[0].message.content
