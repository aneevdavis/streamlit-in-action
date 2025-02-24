from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, END, StateGraph, MessagesState
from langchain_core.messages import HumanMessage

class SupportAgentGraph:
  def __init__(self, llm):
    self.llm = llm

    self.config = {"configurable": {"thread_id": "1"}}
    self.graph = self.build_graph()

  def get_assistant_node(self):
    def assistant_node(state):
      ai_response_message = self.llm.invoke(state["messages"])
      return {"messages": [ai_response_message]}
    return assistant_node

  def build_graph(self):
    memory = MemorySaver()
    builder = StateGraph(MessagesState)
    builder.add_node("assistant", self.get_assistant_node())
    builder.add_edge(START, "assistant")
    builder.add_edge("assistant", END)
    return builder.compile(checkpointer=memory)

  def invoke(self, human_message_text):
    human_msg = HumanMessage(content=human_message_text)
    state = {"messages": [human_msg]}
    return self.graph.invoke(state, self.config)
