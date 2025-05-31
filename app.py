import streamlit as st
from streamlit_chat import message
import random
import time

# Page configuration
st.set_page_config(
    page_title="EduCareer Pro",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .logo-box {
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            text-align: center;
        }
        .login-box {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .feature-box {
            padding: 20px;
            background-color: #f0f8ff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .btn-primary {
            background-color: #3498db !important;
            color: white !important;
            border: none !important;
            width: 100%;
            margin-bottom: 10px;
        }
        .btn-secondary {
            background-color: #2ecc71 !important;
            color: white !important;
            border: none !important;
            width: 100%;
            margin-bottom: 10px;
        }
        .btn-tertiary {
            background-color: #9b59b6 !important;
            color: white !important;
            border: none !important;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize chat messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "assistant", "content": "Hello! I'm your EduCareer assistant. How can I help you today?"}
    ]

# Main page layout
col1, col2, col3 = st.columns([1, 1, 1])

# Left column - Logo and Buttons
with col1:
    # Logo Box
    st.markdown("""
        <div class="logo-box">
            <img src="https://via.placeholder.com/150" alt="Logo" style="width:150px; margin-bottom:15px;">
            <h2>EduCareer Pro</h2>
            <p>"Empowering Your Future Through Education"</p>
            <button class="btn-tertiary">Explore Courses</button>
        </div>
    """, unsafe_allow_html=True)
    
    # Login Box
    with st.container():
        st.markdown("""
            <div class="login-box">
                <h3>Login</h3>
                <input type="text" placeholder="Email" style="width:100%; margin-bottom:10px; padding:8px; border-radius:5px; border:1px solid #ddd;">
                <input type="password" placeholder="Password" style="width:100%; margin-bottom:10px; padding:8px; border-radius:5px; border:1px solid #ddd;">
                <button class="btn-primary">Login</button>
                <button class="btn-secondary">Sign Up</button>
            </div>
        """, unsafe_allow_html=True)

# Middle column - Career Options
with col2:
    with st.container():
        st.markdown("""
            <div class="feature-box">
                <h3>Career Paths</h3>
                <div style="margin-bottom:15px;">
                    <h4>Technology</h4>
                    <p>Software Development, Data Science, Cybersecurity</p>
                </div>
                <div style="margin-bottom:15px;">
                    <h4>Business</h4>
                    <p>Management, Marketing, Finance</p>
                </div>
                <div style="margin-bottom:15px;">
                    <h4>Healthcare</h4>
                    <p>Medicine, Nursing, Pharmacy</p>
                </div>
                <div>
                    <h4>Creative Arts</h4>
                    <p>Design, Media, Performing Arts</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Right column - Features
with col3:
    with st.container():
        st.markdown("""
            <div class="feature-box">
                <h3>Why Choose Us?</h3>
                <div style="margin-bottom:15px;">
                    <h4>Industry Experts</h4>
                    <p>Learn from professionals with real-world experience</p>
                </div>
                <div style="margin-bottom:15px;">
                    <h4>Job Placement</h4>
                    <p>90% placement rate within 3 months</p>
                </div>
                <div style="margin-bottom:15px;">
                    <h4>Flexible Learning</h4>
                    <p>Study at your own pace, anytime, anywhere</p>
                </div>
                <div>
                    <h4>Affordable</h4>
                    <p>Quality education at competitive prices</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Simple chat interface (without the toggle functionality)
st.markdown("---")
st.subheader("Chat with our Career Advisor")

user_input = st.text_input("Type your question here...", key="chat_input")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Simulate bot response
    bot_responses = [
        "We have excellent programs in that field. Would you like more details?",
        "Many students pursue that career path. What specifically interests you?",
        "We offer several courses that can help with that career.",
        "That's a growing field with good job opportunities."
    ]
    bot_response = random.choice(bot_responses)
    time.sleep(1)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        message(msg["content"], is_user=True)
    else:
        message(msg["content"])

# Footer
st.markdown("""
    <div style="margin-top: 50px; padding: 20px; text-align: center; background-color: #f8f9fa; border-radius: 10px;">
        <p>© 2023 EduCareer Pro. All rights reserved.</p>
        <p>Contact us: info@educareerpro.com | +91 9876543210</p>
    </div>
""", unsafe_allow_html=True)
