
from langchain_groq import ChatGroq
def create_chat_groq():
    """
    Function to intialize chat groq
    
    Returns:
    ChatGroq
    """
    return  ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=1,                  
    max_tokens=None,
    timeout=None,
    max_retries=2  #for the Avoiding the failuers  
)