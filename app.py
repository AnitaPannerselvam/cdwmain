from dotenv import load_dotenv
import chain
import streamlit as st

# from langchain_groq import ChatGroq
# from model import create_chat_groq
load_dotenv()

def poem_generator_app():
    """
    Poem Generator App
    """
    with st.form("poem_generator"):
        topic = st.text_input("Enter the Topic for the Poem")
        submitted = st.form_submit_button("Submit")

        if(submitted):
            response = chain.generate_poem(topic)
            st.info(response)

poem_generator_app()

# llm = ChatGroq(
#     model="mixtral-8x7b-32768",
#     temperature=1,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2  #for the Avoiding the failuers
# )

# llm = create_chat_groq()
# response = llm.invoke("Hi")
# print(response.content)
# print (create_chat_groq())