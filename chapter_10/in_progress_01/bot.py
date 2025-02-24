from langchain_openai import ChatOpenAI
from graph import SupportAgentGraph

class Bot:
  def __init__(self, api_keys):
    self.api_keys = api_keys
    self.llm = self.get_llm()
    self.graph = SupportAgentGraph(llm=self.llm)

  def get_llm(self):
    return ChatOpenAI(
      model_name="gpt-4o-mini",
      openai_api_key=self.api_keys["OPENAI_API_KEY"],
      max_tokens=2000
    )

  def chat(self, human_message_text):
    final_state = self.graph.invoke(human_message_text)
    return final_state["messages"][-1].content
