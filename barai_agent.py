from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from tools import get_current_weather, get_news_headlines, get_info_from_wikipedia 
from dotenv import load_dotenv
load_dotenv()

prompt = """
You are a helpful assistant.
You have access to the following tools:
1- get_current_weather: Get the current weather or temperature in a given location.
2- get_news_headlines: Get the latest news headlines for asked region.
3- get_info_from_wikipedia: Get information on a given topic from wikipedia.
Use the tools to answer the user's questions.
"""
llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

agent = create_react_agent(
    tools=[get_current_weather, get_news_headlines, get_info_from_wikipedia],
    model=llm,
)

query = input("you : ")
if query.lower() == "exit":
    exit()
answer = agent.invoke({"messages": [
    {"role": "user", "content": query}]})
print("agent : ", answer['messages'][2].content)











import streamlit as st
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
from tools import get_current_weather, get_news_headlines, get_info_from_wikipedia 
from dotenv import load_dotenv
load_dotenv()


# streamlit

# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("https://images.unsplash.com/photo-1503264116251-35a269479413");
#         background-attachment: fixed;
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# st.markdown(
#     """
#     <style>
#     /* Style user chat bubble */
#     .stChatMessage.user {
#         background-color: #DCF8C6;   /* light green like WhatsApp */
#         border-radius: 30px;
#         padding: 8px;
#     }

#     /* Style assistant chat bubble */
#     .stChatMessage.assistant {
#         background-color:  #DCF8C6;   /* light blue */
#         border-radius: 12px;
#         padding: 8px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# st.markdown(
#     """
#     <style>
#     /* General chat bubble style */
#     div[data-testid="stChatMessage"] {
#         border-radius: 20px;
#         padding: 10px;
#         margin: 5px 0;
#     }

#     /* User bubble (first child div inside chat message) */
#     div[data-testid="stChatMessage"][data-testid="stChatMessage-user"] {
#         background-color: #DCF8C6; /* WhatsApp-like green */
#     }

#     /* Assistant bubble */
#     div[data-testid="stChatMessage"][data-testid="stChatMessage-assistant"] {
#         background-color: #DCF8C6; /* light blue */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# st.markdown(
#     """
#     <style>
#     /* Apply to the inner markdown container used in chat messages */
#     div[data-testid="stChatMessage"] .stMarkdown {
#         background-color: #E6F3FF !important;
#         padding: 10px;
#         border-radius: 12px;
#         margin: 2px 0;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown(
#     """
#     <style>
#     /* General bubble style */
#     div[data-testid="stChatMessage"] .stMarkdown {
#         padding: 10px;
#         border-radius: 12px;
#         margin: 2px 0;
#     }

#     /* User bubbles = odd */
#     div[data-testid="stChatMessage"]:nth-of-type(odd) .stMarkdown {
#         background-color: #DCF8C6 !important;
#     }

#     /* Assistant bubbles = even */
#     div[data-testid="stChatMessage"]:nth-of-type(even) .stMarkdown {
#         background-color: #E6F3FF !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown(
#     """
#     <style>
#     /* target the content column of each chat message (avatar is first child, content second) */
#     div[data-testid="stChatMessage"] > div > div:nth-child(2) .stMarkdown {
#         background-color: #E6F3FF !important;
#         padding: 10px;
#         border-radius: 12px;
#         margin: 2px 0;
#     }

#     /* user content column — assuming it appears with reversed order; adjust if needed */
#     div[data-testid="stChatMessage"] > div[style*="row-reverse"] > div:nth-child(2) .stMarkdown,
#     div[data-testid="stChatMessage"] > div[style*="flex-direction: row-reverse"] > div:nth-child(2) .stMarkdown {
#         background-color: #DCF8C6 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown(
#     """
#     <style>
#     /* Assistant chat bubble */
#     div[data-testid="stChatMessage"] > div > div:nth-child(2) .stMarkdown {
#         background-color: #E6F3FF !important;
#         padding: 10px;
#         border-radius: 12px;
#         margin: 2px 0;

#         /* Font customization */
#         # font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* change font */
#         font-family: 'sans-serif'; /* change font */
#         font-size: 16px;      /* change size */
#         font-style: normal;   /* italic | normal */
#         font-weight: 500;     /* 400=normal, 700=bold */
#         color: #000000;       /* text color */
#     }

#     /* User chat bubble */
#     div[data-testid="stChatMessage"] > div[style*="row-reverse"] > div:nth-child(2) .stMarkdown,
#     div[data-testid="stChatMessage"] > div[style*="flex-direction: row-reverse"] > div:nth-child(2) .stMarkdown {
#         background-color: #DCF8C6 !important;

#         /* Font customization */
#         # font-family: 'Courier New', monospace;
#         font-family: 'sans-serif';
#         font-size: 25px;
#         font-style: italic;
#         font-weight: 600;
#         color: #003300;
        
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# st.markdown(
#     """
#     <style>
#     /* Remove red border on st.chat_input */
#     div[data-baseweb="input"] input:focus,
#     div[data-baseweb="textarea"] textarea:focus {
#         border: 1px solid #00FF7F !important;  /* green border instead of red */
#         box-shadow: 0 0 4px rgba(0, 255, 127, 0.5); /* soft glow */
#         outline: none !important;
#     }

#     /* Optional: also handle invalid state */
#     div[data-baseweb="input"] input:invalid,
#     div[data-baseweb="textarea"] textarea:invalid {
#         border: 1px solid #00FF7F !important;
#         outline: none !important;
#         box-shadow: none !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.markdown("<h1 style='color:#00FF7F;'>Barai AI Assistant</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* Target Streamlit chat input */
    div[data-baseweb="input"] input:focus,
    div[data-baseweb="textarea"] textarea:focus {
        border: 1px solid transparent !important; /* no red border */
        box-shadow: none !important;              /* remove glow */
        outline: none !important;                 /* remove outline */
    }

    /* Also prevent red when invalid */
    div[data-baseweb="input"] input:invalid,
    div[data-baseweb="textarea"] textarea:invalid {
        border: 1px solid transparent !important;
        box-shadow: none !important;
        outline: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
# Display old messages
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar="🤵"):  # user avatar
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant", avatar="🧛‍♂️"):  # assistant avatar
            st.markdown(message["content"])



if query := st.chat_input("Ask anything..."):
# if prompt := st.text_input("Say something..."):
    # Show user message
    with st.chat_message("user",avatar = "🤵"):
         st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Format full conversation into prompt
    chat_history = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages if m["role"] == "user"])

prompt = """
You are a helpful and so friendly assistant.
You have access to the following tools:
1- get_current_weather: Get the current weather or temperature of given location.
2- get_news_headlines: Get the latest news headlines for the asked region.
3- get_info_from_wikipedia: Get information on a given topic from wikipedia.
Use the tools to answer the user's questions.
"""
llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

agent = create_react_agent(
    tools=[get_current_weather, get_news_headlines, get_info_from_wikipedia],
    model=llm,
)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent_with_memory = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=[get_current_weather, get_news_headlines, get_info_from_wikipedia],
    memory=memory
)
try:
    answer = agent.invoke({"messages": [
    {"role": "user", "content": query}]})

# Get the last assistant message (if available)
    assistant_msg = None
    for msg in answer["messages"]:
        if msg.type == "ai" :
            assistant_msg = msg.content

    if assistant_msg:
        with st.chat_message("assistant",avatar = "🧛‍♂️"):
             st.markdown(assistant_msg)
             st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
        print("agent :", assistant_msg)
    else:
        with st.chat_message("assistant"):
            st.markdown("⚠️ No response from agent.")
except Exception as e:
    with st.chat_message("assistant"):
        # st.markdown(f"⚠️ Error: {e}")
        st.markdown("titi fish")
