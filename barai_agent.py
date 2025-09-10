import streamlit as st
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from tools import get_current_weather, get_news_headlines, get_info_from_wikipedia
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the app title with custom color
st.markdown("<h1 style='color:#00FF7F;'>Barai AI Assistant</h1>", unsafe_allow_html=True)

# Initialize chat message history in session state if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize conversation memory in session state if not present
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True
    )

# Display previous chat messages with appropriate avatars
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar="🤵"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant", avatar="🧛‍♂️"):
            st.markdown(message["content"])

# System prompt to guide the agent's behavior and tool usage
system_prompt = system_prompt = """
You are a helpful and friendly assistant.
You have access to the following tools:
1- get_current_weather: Get the current weather or temperature of given location.
2- get_news_headlines: Get the latest news headlines for the asked region and strictly follow the instructions inside the tool.
3- get_info_from_wikipedia: Get information on a given topic from wikipedia.
Use the tools to answer the user's questions.

IMPORTANT:
- When showing news headlines, always include the source exactly as returned (e.g., "BBC News", "Reuters").
- Do not remove or rewrite the sources.
"""

# Initialize the language model (LLM) from Groq
llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# Create the agent with memory and the specified tools
agent_with_memory = initialize_agent(
    tools=[get_current_weather, get_news_headlines, get_info_from_wikipedia],
    llm=llm,
    agent="chat-conversational-react-description",
    memory=st.session_state.memory,   # persistent memory
    verbose=True
)

# Handle user input from the chat box
if query := st.chat_input("Ask anything..."):

    # Show user message in chat and add to session state
    with st.chat_message("user", avatar="🤵"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Call the agent with memory to get a response
    answer = agent_with_memory.invoke({"input": query})
    assistant_msg = answer.get("output", None)

    # Show assistant's response in chat and add to session state
    if assistant_msg:
        with st.chat_message("assistant", avatar="🧛‍♂️"):
            st.markdown(assistant_msg)
        st.session_state.messages.append({"role": "assistant", "content": assistant_msg})


        