from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import create_react_agent

print("Load model")
llm = ChatOllama(
    model= "qwen3:4b",
    temperature=0.1,
)

print("Load agent")
research_agent = create_react_agent(
    model= llm,
    tools=[],
    prompt=(
        "You are a helpful agent"
    ),
    name="research_agent",
    verbose= True,
)

print("start response")
resp = research_agent.invoke({"role": "user", "content": "2+2"})

print(resp)