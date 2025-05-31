import streamlit as st
from streamlit_chat import message
import random
import time

# Page configuration
st.set_page_config(
    page_title="EduCareer Pro - Your Pathway to Success",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .logo-container {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .logo-img {
            height: 80px;
            margin-right: 15px;
        }
        .slogan {
            font-size: 24px;
            color: #2c3e50;
            font-weight: bold;
            font-style: italic;
        }
        .left-box {
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .right-box {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            height: 100%;
        }
        .feature-item {
            padding: 10px;
            margin-bottom: 10px;
            border-left: 4px solid #3498db;
            background-color: #f0f8ff;
            border-radius: 0 5px 5px 0;
        }
        .feature-title {
            font-weight: bold;
            color: #2c3e50;
        }
        .login-btn {
            background-color: #3498db !important;
            color: white !important;
            border: none !important;
            width: 100%;
            margin-bottom: 10px;
        }
        .signup-btn {
            background-color: #2ecc71 !important;
            color: white !important;
            border: none !important;
            width: 100%;
        }
        .chat-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 350px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            z-index: 1000;
            display: none;
        }
        .chat-header {
            background-color: #3498db;
            color: white;
            padding: 10px;
            border-radius: 10px 10px 0 0;
            cursor: pointer;
        }
        .chat-body {
            padding: 10px;
            height: 300px;
            overflow-y: auto;
        }
        .chat-input {
            padding: 10px;
            border-top: 1px solid #eee;
        }
        .chat-toggle {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #3498db;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            z-index: 1001;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize chat messages if not already in session state
if 'chat_open' not in st.session_state:
    st.session_state['chat_open'] = False
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "assistant", "content": "Hello! I'm your EduCareer assistant. How can I help you today?"}
    ]

# Chatbot functions
def toggle_chat():
    st.session_state['chat_open'] = not st.session_state['chat_open']

def send_message():
    user_input = st.session_state.chat_input
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Simulate bot response
        bot_responses = [
            "That's a great question! Our platform offers various courses to help with that.",
            "I can recommend some resources for that topic. What specific area are you interested in?",
            "Many students ask about that. We have a dedicated section for it in our learning materials.",
            "For that topic, I suggest checking our 'Career Preparation' section.",
            "Our platform has several success stories related to that. Would you like me to share some?",
            "That's an important aspect of education. We cover it in our advanced courses.",
            "I can help you find the right learning path for your goals. Can you share more details?"
        ]
        bot_response = random.choice(bot_responses)
        
        # Add slight delay to simulate typing
        time.sleep(1)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        # Clear input
        st.session_state.chat_input = ""

# Main page layout
col1, col2 = st.columns([1, 1])

# Left column - Logo, Slogan, Login/Signup
with col1:
    # Logo and Slogan
    st.markdown("""
        <div class="logo-container">
            <img src="https://via.placeholder.com/80" class="logo-img" alt="EduCareer Pro Logo">
            <div>
                <h1>EduCareer Pro</h1>
                <div class="slogan">"Empowering Your Future Through Education"</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Login/Signup Box
    with st.container():
        st.markdown("""
            <div class="left-box">
                <h3>Get Started</h3>
                <p>Login to access your personalized learning dashboard or sign up to begin your journey.</p>
        """, unsafe_allow_html=True)
        
        # Login/Signup buttons
        login_email = st.text_input("Email", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_password")
        st.button("Login", key="login_btn", on_click=lambda: st.success("Login functionality would go here"))
        
        st.markdown("<div style='text-align: center; margin: 10px 0;'>OR</div>", unsafe_allow_html=True)
        
        signup_name = st.text_input("Full Name", key="signup_name")
        signup_email = st.text_input("Email", key="signup_email")
        signup_password = st.text_input("Password", type="password", key="signup_password")
        st.button("Sign Up", key="signup_btn", on_click=lambda: st.success("Signup functionality would go here"))
        
        st.markdown("</div>", unsafe_allow_html=True)

# Right column - Features
with col2:
    with st.container():
        st.markdown("""
            <div class="right-box">
                <h3>Why Choose EduCareer Pro?</h3>
                
                <div class="feature-item">
                    <div class="feature-title">Education for Job</div>
                    <p>Industry-relevant courses designed to make you job-ready in today's competitive market.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-title">Job Opportunities in India</div>
                    <p>Direct connections with top employers and exclusive job postings across India.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-title">Success Stories</div>
                    <p>Learn from the experiences of successful professionals who started just like you.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-title">YouTube Learning Experience</div>
                    <p>Curated video content from the best educational channels integrated with our platform.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-title">Best Learning Platform</div>
                    <p>Award-winning platform with interactive lessons, quizzes, and hands-on projects.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-title">Portfolio Projects</div>
                    <p>Build real-world projects to showcase your skills to potential employers.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-title">Interview Preparation</div>
                    <p>Comprehensive resources including mock interviews, coding challenges, and soft skills training.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Chatbot toggle button
st.markdown("""
    <div class="chat-toggle" onclick="toggleChat()">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        </svg>
    </div>
""", unsafe_allow_html=True)

# Chatbot container
if st.session_state['chat_open']:
    st.markdown("""
        <div class="chat-container" style="display: block;">
            <div class="chat-header" onclick="toggleChat()">
                EduCareer Assistant
            </div>
            <div class="chat-body">
    """, unsafe_allow_html=True)
    
    # Display chat messages
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            message(msg["content"], is_user=True, key=f"user_msg_{i}")
        else:
            message(msg["content"], key=f"bot_msg_{i}")
    
    st.markdown("""
            </div>
            <div class="chat-input">
                <input type="text" id="chat_input" placeholder="Type your message..." onkeyup="if(event.keyCode==13) sendMessage()">
            </div>
        </div>
    """, unsafe_allow_html=True)

# JavaScript for chat functionality
st.markdown("""
    <script>
        function toggleChat() {
            const chatContainer = document.querySelector('.chat-container');
            if (chatContainer.style.display === 'none' || !chatContainer.style.display) {
                chatContainer.style.display = 'block';
            } else {
                chatContainer.style.display = 'none';
            }
        }
        
        function sendMessage() {
            const input = document.getElementById('chat_input');
            if (input.value.trim() !== '') {
                // In a real app, you would send this to your Streamlit backend
                console.log('Message sent:', input.value);
                input.value = '';
            }
        }
    </script>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="margin-top: 50px; padding: 20px; text-align: center; background-color: #f8f9fa; border-radius: 10px;">
        <p>© 2023 EduCareer Pro. All rights reserved.</p>
        <p>Contact us: info@educareerpro.com | +91 9876543210</p>
    </div>
""", unsafe_allow_html=True)
