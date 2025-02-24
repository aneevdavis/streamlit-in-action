from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, END, StateGraph, MessagesState
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.documents import Document
from prompts import *

class AgentState(MessagesState):
  sys_msg_text: str
  retrieved_docs: list[Document]

class SupportAgentGraph:
  def __init__(self, llm, vector_store):
    self.llm = llm
    self.vector_store = vector_store

    self.config = {"configurable": {"thread_id": "1"}}
    self.graph = self.build_graph()

  @staticmethod
  def base_context_node(state):
    return {"sys_msg_text": BASE_SYS_MSG}

  def get_retrieve_node(self):
    def retrieve_node(state: AgentState):
      messages = state["messages"]
      message_contents = [message.content for message in messages]
      retrieval_query = "\n".join(message_contents)
      docs = self.vector_store.retrieve(retrieval_query)
      return {"retrieved_docs": docs}
    return retrieve_node

  @staticmethod
  def augment_node(state: AgentState):
    docs = state["retrieved_docs"]
    docs_content_list = [doc.page_content for doc in docs]
    content = "\n".join(docs_content_list)
    new_text = SYS_MSG_AUGMENTATION.replace("{docs_content}", content)
    return {"sys_msg_text": BASE_SYS_MSG + "\n\n" + new_text}

  def get_assistant_node(self):
    def assistant_node(state):
      sys_msg = SystemMessage(content=state["sys_msg_text"])
      messages_to_send = [sys_msg] + state["messages"]
      ai_response_message = self.llm.invoke(messages_to_send)
      return {"messages": [ai_response_message]}
    return assistant_node

  def build_graph(self):
    memory = MemorySaver()
    builder = StateGraph(AgentState)

    builder.add_node("base_context", self.base_context_node)
    builder.add_node("retrieve", self.get_retrieve_node())
    builder.add_node("augment", self.augment_node)
    builder.add_node("assistant", self.get_assistant_node())

    builder.add_edge(START, "base_context")
    builder.add_edge("base_context", "retrieve")
    builder.add_edge("retrieve", "augment")
    builder.add_edge("augment", "assistant")
    builder.add_edge("assistant", END)

    return builder.compile(checkpointer=memory)

  def invoke(self, human_message_text):
    human_msg = HumanMessage(content=human_message_text)
    state = {"messages": [human_msg]}
    return self.graph.invoke(state, self.config)

  def get_conversation(self):
    state = self.graph.get_state(self.config)
    if "messages" not in state.values:
      return []
    return state.values["messages"]
