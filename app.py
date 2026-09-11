import streamlit as st
from agent import SpotifySupportAgent

# Page configuration for a professional wide layout
st.set_page_config(
    page_title="Spotify Cares AI Support",
    page_icon="🎧",
    layout="centered"
)

# Custom CSS injection for Spotify Theme Styling
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Input box styling */
    textarea {
        background-color: #242424 !important;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
    }
    
    /* Primary Button styling */
    .stButton>button {
        background-color: #1DB954;
        color: #000000;
        font-weight: bold;
        border-radius: 500px;
        padding: 0.6rem 2rem;
        border: none;
        transition: transform 0.1s ease;
    }
    .stButton>button:hover {
        background-color: #1ed760;
        transform: scale(1.02);
    }

    /* Custom Card Containers */
    .spotify-card {
        background-color: #181818;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #1DB954;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    
    .spotify-card-escalate {
        background-color: #181818;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #e91429;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='color: #1DB954; text-align: center;'>🎧 Spotify Cares AI Support Hub</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #B3B3B3;'>Automated Intent Classification, Smart Escalation Routing, and Response Generation</p>", unsafe_allow_html=True)
st.markdown("---")

agent = SpotifySupportAgent()

# Main Input Section
st.markdown("### 💬 Customer Inquiry")
customer_input = st.text_area(
    "Enter customer tweet or support message:", 
    "My music keeps skipping every 2 seconds on my android phone, please fix this!",
    height=100
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run_btn = st.button("Run AI Agent Pipeline", use_container_width=True)

if run_btn:
    if customer_input.strip():
        with st.spinner("Analyzing customer intent and routing..."):
            result = agent.run_pipeline(customer_input)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 📊 Agent Decision Dashboard")
        
        # Intent Card
        st.markdown(f"""
            <div class='spotify-card'>
                <h4 style='color: #1DB954; margin:0;'>Detected Intent</h4>
                <p style='font-size: 18px; font-weight: bold; margin: 5px 0 0 0;'>{result['intent']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Escalation Card
        is_escalated = result['escalation_decision'] == "Escalate to Human"
        card_class = "spotify-card-escalate" if is_escalated else "spotify-card"
        decision_color = "#e91429" if is_escalated else "#1DB954"
        
        st.markdown(f"""
            <div class='{card_class}'>
                <h4 style='color: {decision_color}; margin:0;'>Escalation Status: {result['escalation_decision']}</h4>
                <p style='color: #B3B3B3; margin: 5px 0 0 0;'><b>Reason:</b> {result['escalation_reason']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Drafted Reply Card
        st.markdown(f"""
            <div class='spotify-card'>
                <h4 style='color: #1DB954; margin:0;'>Drafted Brand Response</h4>
                <p style='font-style: italic; color: #FFFFFF; margin: 10px 0 0 0; background: #242424; padding: 12px; border-radius: 8px;'>"{result['drafted_reply']}"</p>
            </div>
        """, unsafe_allow_html=True)
        
    else:
        st.warning("Please enter a valid message before running the pipeline.")