# from model import create_chat_groq
# def generate_poem():
#     llm = create_chat_groq()
# response = llm.invoke("Hi")
# print response.content

# import prompt
# from model import create_chat_groq
# from langchain_groq import ChatGroq

# """
# Function to generate poem
# Args:
# topic(str) - topic of the poem 
# Returns:
# response.content (str)
# """

# def generate_poem(topic):


# prompt_template = prompt.poem_generator_prompt()
# llm=create_chat_groq()
# chain = prompt_template | llm
# response = chain.invoke({
#     "topic" :topic
# })
# return response.content
    

from prompt import poem_generator_prompt
from model import create_chat_groq

"""
Function to generate a poem
Args:
    topic (str): The topic of the poem
Returns:
    str: The generated poem content
"""

def generate_poem(topic):

    prompt_template = poem_generator_prompt()
    
    llm = create_chat_groq()
    

    chain = prompt_template | llm
    

    response = chain.invoke({"topic": topic})
    return response.content
