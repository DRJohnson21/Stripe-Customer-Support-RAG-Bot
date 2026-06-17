import os
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI
from system_prompt import SYSTEM_PROMPT

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")

st.set_page_config(page_title="Stripe Support Bot", page_icon="💬")

st.title("Stripe Customer Support Bot")
st.caption("Azure OpenAI chatbot with safety prompt. RAG retrieval can be added next.")

if not endpoint or not api_key or not deployment:
    st.error("Missing Azure OpenAI settings. Check your .env file.")
    st.stop()

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version=api_version,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# Display previous chat messages, excluding the system prompt
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_input = st.chat_input("Ask a Stripe support question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=deployment,
                    messages=st.session_state.messages,
                    temperature=0.2,
                    max_tokens=1500,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                )

                bot_reply = response.choices[0].message.content
                st.markdown(bot_reply)

                st.session_state.messages.append(
                    {"role": "assistant", "content": bot_reply}
                )

            except Exception as e:
                st.error(f"Error: {e}")