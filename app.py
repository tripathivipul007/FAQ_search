import streamlit as st
from faqs import model
from faqs import faqs
from faqs import index as faiss_index

# Streamlit page configuration
st.set_page_config(page_title="Albeena FAQ Bot", page_icon="💬", layout="wide")

# Custom CSS for chat styling
st.markdown("""
    <style>
        .chat-container {
            max-width: 600px;
            margin: 0 auto;
        }
        .chat-bubble {
            padding: 10px 15px;
            border-radius: 20px;
            margin: 10px 0;
            display: inline-block;
            max-width: 80%;
        }
        .chat-bubble-user {
            background-color: #d1e7ff;
            color: #0c1b33;
            text-align: right;
            align-self: flex-end;
            margin-left: auto;
        }
        .chat-bubble-bot {
            background-color: #f0f4f7;
            color: #333333;
            text-align: left;
            align-self: flex-start;
            margin-right: auto;
        }
        .bot-name {
            font-weight: bold;
            color: #2c82c9;
        }
        .input-container {
            position: fixed;
            bottom: 0;
            width: 80%;
            background-color: #ffffff;
            padding: 10px 15px;
            border-top: 1px solid #e1e1e1;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
        }
        .input-box {
            width: calc(100% - 60px);
            padding: 10px;
            border: 1px solid #d1d1d1;
            border-radius: 20px;
            outline: none;
        }
        .ask-button {
            background-color: #2c82c9;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 8px 15px;
            font-size: 0.9rem;
            cursor: pointer;
            margin-left: 10px;
        }
        .ask-button:hover {
            background-color: #216b9b;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title and subtitle
st.markdown("<h1 style='text-align: center; color: #2c82c9;'>Albeena FAQ Bot</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #6c757d;'>Your friendly assistant for quick answers!</h3>", unsafe_allow_html=True)

# Chat container
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"""
            <div class="chat-bubble chat-bubble-user">
                {message["content"]}
            </div>
        """, unsafe_allow_html=True)
    elif message["role"] == "bot":
        st.markdown(f"""
            <div class="chat-bubble chat-bubble-bot">
                <span class="bot-name">Albeena:</span> {message["content"]}
            </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Input box and button container using columns
col1, col2 = st.columns([4, 1])  # Create two columns, one for input and one for the button

with col1:
    user_input = st.text_input(
        label="Ask your question:",
        placeholder="Type your question here...",
        label_visibility="collapsed",
        key="user_input",
    )

with col2:
    ask_button = st.button("Ask", use_container_width=True, key="ask_button")

# Process input when the "Ask" button is clicked
if ask_button and user_input.strip():
    # Add user question to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Generate embedding for user query
    query_embedding = model.encode([user_input])

    # Search FAISS index for the closest match
    distances, indices = faiss_index.search(query_embedding, k=1)

    # Determine response
    if distances[0][0] < 1.5:  # A threshold to determine a good match
        matched_faq = faqs[indices[0][0]]
        bot_response = matched_faq['answer']
    else:
        bot_response = "Our Support Staff will assist you shortly."

    # Add bot response to chat history
    st.session_state.chat_history.append({"role": "bot", "content": bot_response})

    # Rerun to update chat
    st.experimental_rerun()
