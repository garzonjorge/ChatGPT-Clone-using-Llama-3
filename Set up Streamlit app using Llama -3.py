# Set up Streamlit app
# import streamlit as st 
# from openai import OpenAI

# st.title("ChatGPT Clone using Local Llama-3")
# st.caption("Chat with locally hosted Llama-3 using the LM Studio")

# # Point to the local server setup using LM Studio
# client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display the chat history
# for message in st.session_state.messages:
#     with st.chat_message(message['role']):
#         st.markdown(message['content'])

# # Accept user input 
# if prompt := st.chat_input('What is up?'):
#     # Add user message to chat history
#     st.session_state.messages.append({'role': 'user', 'content': prompt}) 
#     # Display user message in chat message container
#     with st.chat_message('user'):
#         st.markdown(prompt)

#     # Generate responses
#     response = client.chat.completions.create(
#         model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
#         messages=st.session_state.messages,
#         temperature=0.7,
#     )
#     # Add assistant response to chat history
#     st.session_state.messages.append({'role': "assistant", 'content': response.choices[0].message.content})
#     # Display assistant response in chat message container
#     with st.chat_message('assistant'):
#         st.markdown(response.choices[0].message.content)

############################

## SECOND VERSION ##

# import streamlit as st 
# from openai import OpenAI
# import time

# # Custom CSS for animations and styling
# st.markdown("""
# <style>
# @keyframes fadeIn {
#     from {opacity: 0;}
#     to {opacity: 1;}
# }
# .fade-in {
#     animation: fadeIn 1s ease-in;
# }
# .stApp {
#     background: linear-gradient(to right, #4e54c8, #8f94fb);
#     color: white;
# }
# .chat-message {
#     padding: 1rem;
#     border-radius: 0.5rem;
#     margin-bottom: 1rem;
#     animation: fadeIn 0.5s ease-in;
# }
# .user-message {
#     background-color: rgba(255, 255, 255, 0.1);
# }
# .assistant-message {
#     background-color: rgba(0, 0, 0, 0.1);
# }
# </style>
# """, unsafe_allow_html=True)

# st.title("🤖 ChatGPT Clone using Local Llama-3")
# st.caption("Chat with locally hosted Llama-3 using the LM Studio")

# # ASCII art
# st.text("""
#    _____  _           _   ____        _   
#   / ____|| |         | | |  _ \      | |  
#  | |    | |__   __ _| |_| |_) | ___ | |_ 
#  | |    | '_ \ / _` | __|  _ < / _ \| __|
#  | |____| | | | (_| | |_| |_) | (_) | |_ 
#   \_____|_| |_|\__,_|\__|____/ \___/ \__|
# """)

# # Point to the local server setup using LM Studio
# client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display the chat history with custom styling
# for message in st.session_state.messages:
#     with st.chat_message(message['role'], avatar="🧑‍💻" if message['role'] == 'user' else "🤖"):
#         st.markdown(f"<div class='chat-message {message['role']}-message'>{message['content']}</div>", unsafe_allow_html=True)

# # Accept user input 
# if prompt := st.chat_input('What is up?'):
#     # Add user message to chat history
#     st.session_state.messages.append({'role': 'user', 'content': prompt}) 
#     # Display user message in chat message container
#     with st.chat_message('user', avatar="🧑‍💻"):
#         st.markdown(f"<div class='chat-message user-message'>{prompt}</div>", unsafe_allow_html=True)

#     # Show a loading spinner
#     with st.spinner("🤖 Thinking..."):
#         # Simulate thinking time
#         time.sleep(1)
        
#         # Generate responses
#         response = client.chat.completions.create(
#             model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
#             messages=st.session_state.messages,
#             temperature=0.7,
#         )
    
#     # Add assistant response to chat history
#     assistant_response = response.choices[0].message.content
#     st.session_state.messages.append({'role': "assistant", 'content': assistant_response})
    
#     # Display assistant response in chat message container with typing effect
#     with st.chat_message('assistant', avatar="🤖"):
#         message_placeholder = st.empty()
#         full_response = ""
#         for chunk in assistant_response.split():
#             full_response += chunk + " "
#             time.sleep(0.05)
#             message_placeholder.markdown(f"<div class='chat-message assistant-message'>{full_response}</div>", unsafe_allow_html=True)
#         message_placeholder.markdown(f"<div class='chat-message assistant-message'>{full_response}</div>", unsafe_allow_html=True)

# # Add a cool fact about AI at the bottom
# st.markdown("---")
# st.markdown("<div class='fade-in'>🌟 Cool AI Fact: Did you know that the term 'artificial intelligence' was first coined in 1956 at a conference at Dartmouth College?</div>", unsafe_allow_html=True)
                

########################################

### THIRD VERSION ###

import streamlit as st 
from openai import OpenAI
import time

# Custom CSS for animations and styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

body {
    background-color: #001f3f;
    color: white;
    font-family: 'Arial', sans-serif;
}
.stApp {
    background: linear-gradient(45deg, #001f3f, #003366);
}
.title {
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;
    text-align: center;
    color: #4dd0e1;
    text-shadow: 0 0 10px #4dd0e1;
    animation: glow 2s ease-in-out infinite alternate;
}
@keyframes glow {
    from {
        text-shadow: 0 0 5px #4dd0e1, 0 0 10px #4dd0e1;
    }
    to {
        text-shadow: 0 0 10px #4dd0e1, 0 0 20px #4dd0e1, 0 0 30px #4dd0e1;
    }
}
.chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    animation: fadeIn 0.5s ease-in;
}
.user-message {
    background-color: rgba(255, 255, 255, 0.1);
}
.assistant-message {
    background-color: rgba(77, 208, 225, 0.1);
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
.feature {
    background-color: rgba(77, 208, 225, 0.1);
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    animation: slideIn 0.5s ease-in-out;
}
@keyframes slideIn {
    from {transform: translateX(-100%);}
    to {transform: translateX(0);}
}
.robot-animation {
    text-align: center;
    font-size: 5rem;
    animation: robotMove 2s infinite alternate;
}
@keyframes robotMove {
    from {transform: translateY(0);}
    to {transform: translateY(-20px);}
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>ChatGPT Clone using Local Llama-3</h1>", unsafe_allow_html=True)
st.caption("Chat with locally hosted Llama-3 using the LM Studio")

# Robot animation
st.markdown("<div class='robot-animation'>🤖</div>", unsafe_allow_html=True)

# Point to the local server setup using LM Studio
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat history with custom styling
for message in st.session_state.messages:
    with st.chat_message(message['role'], avatar="🧑‍💻" if message['role'] == 'user' else "🤖"):
        st.markdown(f"<div class='chat-message {message['role']}-message'>{message['content']}</div>", unsafe_allow_html=True)

# Accept user input 
if prompt := st.chat_input('What is up?'):
    # Add user message to chat history
    st.session_state.messages.append({'role': 'user', 'content': prompt}) 
    # Display user message in chat message container
    with st.chat_message('user', avatar="🧑‍💻"):
        st.markdown(f"<div class='chat-message user-message'>{prompt}</div>", unsafe_allow_html=True)

    # Show a loading spinner
    with st.spinner("🤖 Thinking..."):
        # Simulate thinking time
        time.sleep(1)
        
        # Generate responses
        response = client.chat.completions.create(
            model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
            messages=st.session_state.messages,
            temperature=0.7,
        )
    
    # Add assistant response to chat history
    assistant_response = response.choices[0].message.content
    st.session_state.messages.append({'role': "assistant", 'content': assistant_response})
    
    # Display assistant response in chat message container with typing effect
    with st.chat_message('assistant', avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(f"<div class='chat-message assistant-message'>{full_response}</div>", unsafe_allow_html=True)
        message_placeholder.markdown(f"<div class='chat-message assistant-message'>{full_response}</div>", unsafe_allow_html=True)

# Add key features about the chatbot
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #4dd0e1;'>Key Features</h2>", unsafe_allow_html=True)

features = [
    "🧠 Powered by Llama-3, a state-of-the-art language model",
    "🏠 Runs locally on your machine for enhanced privacy",
    "🔄 Maintains conversation context for natural dialogue",
    "🎨 Customizable with LM Studio for various applications"
]

for feature in features:
    st.markdown(f"<div class='feature'>{feature}</div>", unsafe_allow_html=True)
