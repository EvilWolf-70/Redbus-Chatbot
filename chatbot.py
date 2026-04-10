import streamlit as st
import google.genai as genai

# --- Config ---
API_KEY = "AIzaSyCEHGqItYSyxEKW_sRPMKDeRAvcQeBAPqY"  # Replace with your key
KB_FILE = "india_bus_dataset.txt"
MODEL = "gemini-2.5-flash"

# --- Load KB ---
with open(KB_FILE, "r") as f:
    kb = f.read()

SYSTEM_PROMPT = f"""
you are the redbus customer executive your job is to provide answers to the questions asked by the customers ,
you should answer them in polite,
if there is any questions out of the kb say you did not have that info, only refer the kb and provide the response
{kb}
"""

# --- Page Setup ---
st.set_page_config(page_title="RedBus Support", page_icon="🚌")
st.title("🚌 RedBus Customer Support")
st.caption("Ask me anything about your booking, cancellations, or refunds.")

# --- Init session state (client + chat together) ---
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=API_KEY)

if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(
        model=MODEL,
        config={"system_instruction": SYSTEM_PROMPT}
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display chat history ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- Input ---
if user_input := st.chat_input("Type your question..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(user_input)
            reply = response.text
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
