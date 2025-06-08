from langchain_openai import ChatOpenAI
from graph import SupportAgentGraph
from vector_store import VectorStore
from tools import tools

class Bot:
  def __init__(self, api_keys, config):
    self.api_keys = api_keys
    self.config = config

    self.llm = self.get_llm().bind_tools(tools)
    self.vector_store = self.get_vector_store()

    self.graph = SupportAgentGraph(
      llm=self.llm, vector_store=self.vector_store)

  def get_vector_store(self):
    index_name = self.config["VECTOR_STORE_INDEX_NAME"]
    model_name = self.config["EMBEDDING_MODEL_NAME"]
    return VectorStore(
      api_keys=self.api_keys, index_name=index_name, model_name=model_name)

  def get_llm(self):
    return ChatOpenAI(
      model_name="gpt-4o-mini",
      openai_api_key=self.api_keys["OPENAI_API_KEY"],
      max_tokens=2000
    )

  def chat(self, human_message_text):
    final_state = self.graph.invoke(human_message_text)
    return final_state["messages"][-1].content

  def get_history(self):
    return self.graph.get_conversation()

