import streamlit as st

def home_page(navigate_to):
    """
    Displays the Home Page with a Huge Button for Navigation
    Args:
        navigate_to (function): Function to change the navigation state
    """
    st.markdown(
        """
        <div style="background-color: #4CAF50; padding: 20px; text-align: center; border-radius: 10px; color: white;">
            <h1 style="font-family: Arial, sans-serif;">Welcome to the Quiz Generator Platform</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("This platform allows you to generate quizzes easily and quickly. Click the button below to get started!")

    # Huge button for navigation
    if st.button("Go to Quiz Generator", key="navigate_button", help="Click to create your quiz"):
        navigate_to("Generate Quiz")
