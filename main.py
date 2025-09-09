
# from dotenv import load_dotenv
# from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_groq import ChatGroq
# from langchain_community.chat_message_histories import ChatMessageHistory

# load_dotenv()

# # Groq LLM
# llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# # Prompt with history placeholder
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     MessagesPlaceholder(variable_name="history"),  # 👈 injects memory
#     ("human", "{question}")
# ])

# # Store all histories by session_id
# histories = {}

# def get_history(session_id: str):
#     if session_id not in histories:
#         histories[session_id] = ChatMessageHistory()
#     return histories[session_id]

# # Runnable with memory
# chain = RunnableWithMessageHistory(
#     prompt | llm,
#     get_history,
#     input_messages_key="question",
#     history_messages_key="history",
# )

# # Run loop
# while True:
#     query = input("You: ")
#     if query.lower() == "exit":
#         break
#     response = chain.invoke(
#         {"question": query},
#         config={"configurable": {"session_id": "abc123"}}
#     )
#     print("Bot:", response.content)