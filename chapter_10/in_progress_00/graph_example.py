from langgraph.graph import START, END, StateGraph
from langchain_core.messages import AnyMessage, HumanMessage
from langchain_openai import ChatOpenAI
from typing import TypedDict

llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key="sk-proj-...")

class MyGraphState(TypedDict):
  messages: list[AnyMessage]

builder = StateGraph(MyGraphState)

def assistant_node(state):
  messages = state["messages"]
  ai_response_message = llm.invoke(messages)
  return {"messages": messages + [ai_response_message]}

builder.add_node("assistant", assistant_node)
builder.add_edge(START, "assistant")
builder.add_edge("assistant", END)
graph = builder.compile()

input_message = input("Talk to the bot: ")
initial_state = {"messages": [HumanMessage(content=input_message)]}
final_state = graph.invoke(initial_state)

print("Bot:\n" + final_state["messages"][-1].content)
