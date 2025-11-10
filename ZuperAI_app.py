import os
import tabulate
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from groq import Groq
from langchain_experimental.agents import create_csv_agent
load_dotenv()

st.set_page_config(page_icon="💬", layout="wide",
                   page_title="AI Chatbot")


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


st.logo("https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=176,fit=crop,q=95/Aq2oX4vwaKulvNM1/img-20240902-wa0043-removebg-preview-1-A3QOWQv4yxc8XQ8Y.png",size='large')


GROQ_API_KEY = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)




def main():
    st.set_page_config(page_title="ZuperAI Chatbot for Excel files")
    st.header("ZuperAI Chatbot for Excel files", divider="grey", anchor=False)
    st.sidebar.subheader("AI Model Used: llama-3.3-70b (Opensource and can be run offline)")
    st.sidebar.subheader("Backend: Python")
    st.sidebar.subheader("Frontend: Minimal frontend using Python(Streamlit)")
    st.sidebar.subheader("Other Frameworks used: Langchain (Opensource and can be run offline)")


    csv = st.file_uploader("Upload a CSV file", type="csv")
    if csv is not None:
        agent = create_csv_agent(
            ChatGroq(
                model="llama-3.3-70b-versatile",
                temperature=0), 
                csv, 
                verbose=True, 
                handle_parsing_errors=True,
                allow_dangerous_code=True
                )
        user_question = st.chat_input("Chat with the CSV: ")


        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()
