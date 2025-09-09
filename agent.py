# import streamlit as st
# from langchain_groq import ChatGroq
# from langgraph.prebuilt import create_react_agent
# from langchain.memory import ConversationBufferMemory
# from langchain.agents import AgentExecutor
# from tools import get_current_weather, get_news_headlines, get_info_from_wikipedia 
# from dotenv import load_dotenv
# load_dotenv()


# # streamlit

# # st.markdown(
# #     """
# #     <style>
# #     .stApp {
# #         background-image: url("https://images.unsplash.com/photo-1503264116251-35a269479413");
# #         background-attachment: fixed;
# #         background-size: cover;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )


# # st.markdown(
# #     """
# #     <style>
# #     /* Style user chat bubble */
# #     .stChatMessage.user {
# #         background-color: #DCF8C6;   /* light green like WhatsApp */
# #         border-radius: 30px;
# #         padding: 8px;
# #     }

# #     /* Style assistant chat bubble */
# #     .stChatMessage.assistant {
# #         background-color:  #DCF8C6;   /* light blue */
# #         border-radius: 12px;
# #         padding: 8px;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )


# # st.markdown(
# #     """
# #     <style>
# #     /* General chat bubble style */
# #     div[data-testid="stChatMessage"] {
# #         border-radius: 20px;
# #         padding: 10px;
# #         margin: 5px 0;
# #     }

# #     /* User bubble (first child div inside chat message) */
# #     div[data-testid="stChatMessage"][data-testid="stChatMessage-user"] {
# #         background-color: #DCF8C6; /* WhatsApp-like green */
# #     }

# #     /* Assistant bubble */
# #     div[data-testid="stChatMessage"][data-testid="stChatMessage-assistant"] {
# #         background-color: #DCF8C6; /* light blue */
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )


# # st.markdown(
# #     """
# #     <style>
# #     /* Apply to the inner markdown container used in chat messages */
# #     div[data-testid="stChatMessage"] .stMarkdown {
# #         background-color: #E6F3FF !important;
# #         padding: 10px;
# #         border-radius: 12px;
# #         margin: 2px 0;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # st.markdown(
# #     """
# #     <style>
# #     /* General bubble style */
# #     div[data-testid="stChatMessage"] .stMarkdown {
# #         padding: 10px;
# #         border-radius: 12px;
# #         margin: 2px 0;
# #     }

# #     /* User bubbles = odd */
# #     div[data-testid="stChatMessage"]:nth-of-type(odd) .stMarkdown {
# #         background-color: #DCF8C6 !important;
# #     }

# #     /* Assistant bubbles = even */
# #     div[data-testid="stChatMessage"]:nth-of-type(even) .stMarkdown {
# #         background-color: #E6F3FF !important;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # st.markdown(
# #     """
# #     <style>
# #     /* target the content column of each chat message (avatar is first child, content second) */
# #     div[data-testid="stChatMessage"] > div > div:nth-child(2) .stMarkdown {
# #         background-color: #E6F3FF !important;
# #         padding: 10px;
# #         border-radius: 12px;
# #         margin: 2px 0;
# #     }

# #     /* user content column — assuming it appears with reversed order; adjust if needed */
# #     div[data-testid="stChatMessage"] > div[style*="row-reverse"] > div:nth-child(2) .stMarkdown,
# #     div[data-testid="stChatMessage"] > div[style*="flex-direction: row-reverse"] > div:nth-child(2) .stMarkdown {
# #         background-color: #DCF8C6 !important;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # st.markdown(
# #     """
# #     <style>
# #     /* Assistant chat bubble */
# #     div[data-testid="stChatMessage"] > div > div:nth-child(2) .stMarkdown {
# #         background-color: #E6F3FF !important;
# #         padding: 10px;
# #         border-radius: 12px;
# #         margin: 2px 0;

# #         /* Font customization */
# #         # font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* change font */
# #         font-family: 'sans-serif'; /* change font */
# #         font-size: 16px;      /* change size */
# #         font-style: normal;   /* italic | normal */
# #         font-weight: 500;     /* 400=normal, 700=bold */
# #         color: #000000;       /* text color */
# #     }

# #     /* User chat bubble */
# #     div[data-testid="stChatMessage"] > div[style*="row-reverse"] > div:nth-child(2) .stMarkdown,
# #     div[data-testid="stChatMessage"] > div[style*="flex-direction: row-reverse"] > div:nth-child(2) .stMarkdown {
# #         background-color: #DCF8C6 !important;

# #         /* Font customization */
# #         # font-family: 'Courier New', monospace;
# #         font-family: 'sans-serif';
# #         font-size: 25px;
# #         font-style: italic;
# #         font-weight: 600;
# #         color: #003300;
        
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )
# # st.markdown(
# #     """
# #     <style>
# #     /* Remove red border on st.chat_input */
# #     div[data-baseweb="input"] input:focus,
# #     div[data-baseweb="textarea"] textarea:focus {
# #         border: 1px solid #00FF7F !important;  /* green border instead of red */
# #         box-shadow: 0 0 4px rgba(0, 255, 127, 0.5); /* soft glow */
# #         outline: none !important;
# #     }

# #     /* Optional: also handle invalid state */
# #     div[data-baseweb="input"] input:invalid,
# #     div[data-baseweb="textarea"] textarea:invalid {
# #         border: 1px solid #00FF7F !important;
# #         outline: none !important;
# #         box-shadow: none !important;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )

# st.markdown("<h1 style='color:#00FF7F;'>Barai AI Assistant</h1>", unsafe_allow_html=True)
# st.markdown(
#     """
#     <style>
#     /* Target Streamlit chat input */
#     div[data-baseweb="input"] input:focus,
#     div[data-baseweb="textarea"] textarea:focus {
#         border: 1px solid transparent !important; /* no red border */
#         box-shadow: none !important;              /* remove glow */
#         outline: none !important;                 /* remove outline */
#     }

#     /* Also prevent red when invalid */
#     div[data-baseweb="input"] input:invalid,
#     div[data-baseweb="textarea"] textarea:invalid {
#         border: 1px solid transparent !important;
#         box-shadow: none !important;
#         outline: none !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display old messages
# # Display old messages
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         with st.chat_message("user", avatar="🤵"):  # user avatar
#             st.markdown(message["content"])
#     else:
#         with st.chat_message("assistant", avatar="🧛‍♂️"):  # assistant avatar
#             st.markdown(message["content"])



# if query := st.chat_input("Ask anything..."):
# # if prompt := st.text_input("Say something..."):
#     # Show user message
#     with st.chat_message("user",avatar = "🤵"):
#          st.markdown(query)
#     st.session_state.messages.append({"role": "user", "content": query})

#     # Format full conversation into prompt
#     chat_history = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages if m["role"] == "user"])

# prompt = """
# You are a helpful and so friendly assistant.
# You have access to the following tools:
# 1- get_current_weather: Get the current weather or temperature of given location.
# 2- get_news_headlines: Get the latest news headlines for the asked region.
# 3- get_info_from_wikipedia: Get information on a given topic from wikipedia.
# Use the tools to answer the user's questions.
# """



# from langchain.agents import initialize_agent

# llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# agent_with_memory = initialize_agent(
#     tools=[get_current_weather, get_news_headlines, get_info_from_wikipedia],
#     llm=llm,
#     agent="chat-conversational-react-description",
#     memory=memory,
#     verbose=True
# )

# answer = agent_with_memory.invoke({"input": query})
# assistant_msg = answer.get("output", None)

# if assistant_msg:
#         with st.chat_message("assistant", avatar="🧛‍♂️"):
#             st.markdown(assistant_msg)
#             st.session_state.messages.append({"role": "assistant", "content": assistant_msg})





import streamlit as st
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from tools import get_current_weather, get_news_headlines, get_info_from_wikipedia
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# Streamlit UI Styling
# ----------------------------
st.markdown("<h1 style='color:#00FF7F;'>Barai AI Assistant</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* --- Broad selectors covering common Streamlit chat/input structures --- */
    div[data-testid="stChatInput"] textarea,
    div[data-testid="stChatInput"] input,
    div[data-baseweb="input"] textarea,
    div[data-baseweb="input"] input,
    div[role="textbox"],
    textarea,
    input {
      outline: none !important;
      box-shadow: none !important;
      border: 0 !important;
    }

    /* Override focus / invalid states specifically */
    div[data-testid="stChatInput"] textarea:focus,
    div[data-testid="stChatInput"] input:focus,
    div[data-baseweb="input"] textarea:focus,
    div[data-baseweb="input"] input:focus,
    div[role="textbox"]:focus,
    textarea:focus,
    input:focus,
    textarea:invalid,
    input:invalid {
      outline: none !important;
      box-shadow: none !important;
      border: 0 !important;
    }

    /* If Streamlit uses an inner editor element (Draft/Slate), remove its ring too */
    .public-DraftEditor-content,
    .DraftEditor-root,
    .notranslate[contenteditable="true"] {
      box-shadow: none !important;
      outline: none !important;
    }

    /* Optional: keep a subtle focus ring (accessible) but not red */
    div[data-testid="stChatInput"] textarea:focus,
    div[data-testid="stChatInput"] input:focus {
      box-shadow: 0 0 0 3px rgba(0, 255, 127, 0.12) !important;
      border-radius: 6px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------
# Initialize chat history
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True
    )

# Display old messages
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar="🤵"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant", avatar="🧛‍♂️"):
            st.markdown(message["content"])

# ----------------------------
# Define system prompt
# ----------------------------
system_prompt = """
You are a helpful and friendly assistant.
You have access to the following tools:
1- get_current_weather: Get the current weather or temperature of given location.
2- get_news_headlines: Get the latest news headlines for the asked region.
3- get_info_from_wikipedia: Get information on a given topic from wikipedia.
Use the tools to answer the user's questions.
"""

# ----------------------------
# Initialize Agent with Memory
# ----------------------------
llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

agent_with_memory = initialize_agent(
    tools=[get_current_weather, get_news_headlines, get_info_from_wikipedia],
    llm=llm,
    agent="chat-conversational-react-description",
    memory=st.session_state.memory,   # ✅ persistent memory
    verbose=True
)

# ----------------------------
# Handle User Input
# ----------------------------
if query := st.chat_input("Ask anything..."):

    # Show user message
    with st.chat_message("user", avatar="🤵"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Call agent with memory
    answer = agent_with_memory.invoke({"input": query})
    assistant_msg = answer.get("output", None)

    if assistant_msg:
        with st.chat_message("assistant", avatar="🧛‍♂️"):
            st.markdown(assistant_msg)
        st.session_state.messages.append({"role": "assistant", "content": assistant_msg})









# from typing import List, Dict
# from langgraph.graph import StateGraph, START, END
# from langgraph.prebuilt import create_react_agent
# from langchain_groq import ChatGroq
# from langchain_core.messages import BaseMessage, HumanMessage
# from tools import get_current_weather, get_news_headlines, get_info_from_wikipedia
# from dotenv import load_dotenv

# load_dotenv()

# # 1. Define your state with memory
# class State(Dict):
#     messages: List[BaseMessage]   # chat history (memory)

# # 2. Create LLM
# llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# # 3. Create the agent
# agent = create_react_agent(
#     model=llm,
#     tools=[get_current_weather, get_news_headlines, get_info_from_wikipedia],
# )

# # 4. Build graph
# graph = StateGraph(State)
# graph.add_node("agent", agent)
# graph.add_edge(START, "agent")
# graph.add_edge("agent", END)

# app = graph.compile()

# # 5. Run with persistent memory
# state = {"messages": []}  # start empty

# # --- Turn 1 ---
# state["messages"].append(HumanMessage(content="Hello, who am I?"))
# result = app.invoke(state)
# print("Assistant:", result["messages"][-1].content)

# # --- Turn 2 (memory works) ---
# state["messages"].append(HumanMessage(content="What did I just say?"))
# result = app.invoke(state)
# print("Assistant:", result["messages"][-1].content)

# # --- Turn 3 (tool use example) ---
# state["messages"].append(HumanMessage(content="What is the current weather in Karachi?"))
# result = app.invoke(state)
# print("Assistant:", result["messages"][-1].content)

