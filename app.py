import streamlit as st
from core.coordinator import Coordinator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="AI Multi-Agent System",
    page_icon="⚡",
    layout="wide",
)

# --- ADVANCED UI STYLING (Full Page Dark Theme & White Text) ---
st.markdown("""
    <style>
    /* Full Page Background */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"], .stApp {
        background-color: #0d1117 !important;
        color: #ffffff !important;
    }
    
    /* Ensure no white margins/borders */
    [data-testid="stMainViewContainer"] {
        background-color: #0d1117 !important;
    }

    /* Force all text to white */
    html, body, [data-testid="stMarkdownContainer"] p, span, div, label {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }

    /* Bottom block and Chat input styling */
    [data-testid="stBottomBlockContainer"], [data-testid="stChatInput"], [data-testid="stChatInputTextArea"] {
        background-color: #0d1117 !important;
        color: #ffffff !important;
    }

    /* Target the actual textarea inside the wrapper */
    [data-testid="stChatInputTextArea"] {
        background-color: #161b22 !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: 1px solid #30363d !important;
    }

    /* Ensure writing color is white regardless of focus or browser state */
    [data-testid="stChatInputTextArea"] textarea {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    
    /* Ensure the outer wrapper of the input is also dark */
    .stChatInput {
        background-color: transparent !important;
    }

    /* Target the specific Emotion Cache classes for the input area if needed */
    div[class*="st-emotion-cache"] {
        /* We use a broad selector but limit it to bottom containers to avoid breaking other things */
    }
    
    [data-testid="stBottomBlockContainer"] {
        background-color: #0d1117 !important;
        border-top: 1px solid #30363d !important;
    }

    /* Status and Progress styling (Agent Buttons) */
    .stStatusWidget, [data-testid="stStatusWidget"], [data-testid="stStatusWidget"] summary {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        transition: background-color 0.3s ease !important;
    }
    
    /* Hover effect: Grey background */
    .stStatusWidget:hover, [data-testid="stStatusWidget"]:hover, [data-testid="stStatusWidget"] summary:hover {
        background-color: #30363d !important;
        cursor: pointer !important;
    }

    /* Ensure text inside status remains white */
    .stStatusWidget div, .stStatusWidget span, .stStatusWidget p {
        color: #ffffff !important;
    }
    
    /* Code block background */
    code {
        color: #e6edf3 !important;
    }

    /* Final Summary Box */
    .stInfo {
        background-color: #161b22 !important;
        border: 1px solid #238636 !important;
        color: white !important;
    }

    /* Custom Scrollbar for modern look */
    ::-webkit-scrollbar {
        width: 10px;
        background: #0d1117;
    }
    ::-webkit-scrollbar-thumb {
        background: #30363d;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("⚡ AI Multi-Agent Dashboard")
    st.markdown("---")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Sidebar
    with st.sidebar:
        st.header("🚀 Project Overview")
        st.markdown("""
        **AI Multi-Agent System** is an advanced platform where specialized AI agents work together to solve complex tasks.
        
        The system works in 3 easy steps:
        1. **Research** 🔍: Finds detailed information.
        2. **Coding** 💻: Writes Python code solutions.
        3. **Summary** 📝: Explains everything clearly.
        
        It is designed to make research and coding simple and fast for everyone.
        """)
        st.markdown("---")
        
        st.header("🛠️ System Control")
        st.write("Active Agents:")
        st.markdown("- 🔍 **Research Agent**")
        st.markdown("- 💻 **Coding Agent**")
        st.markdown("- 📝 **Summarizer Agent**")
        st.markdown("---")
        if st.button("🗑️ Clear History"):
            st.session_state.messages = []
            st.rerun()

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Enter your task here..."):
        # 1. Immediately show user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 2. Save to history
        st.session_state.messages.append({"role": "user", "content": prompt})

        coordinator = Coordinator()

        # 3. Process with Agents
        with st.chat_message("assistant"):
            try:
                # --- Step 1: Research ---
                with st.status("🔍 **Research Agent** is exploring...", expanded=True) as status:
                    research = coordinator.research_agent.think(prompt)
                    status.update(label="✅ Research Complete", state="complete", expanded=False)
                
                # Show research results outside status
                st.markdown("### 🔍 Research Results")
                st.markdown(research)

                # --- Step 2: Coding ---
                with st.status("💻 **Coding Agent** is building...", expanded=True) as status:
                    coding_prompt = f"Based on this research:\n{research}"
                    code = coordinator.coding_agent.think(coding_prompt)
                    status.update(label="✅ Code Generated", state="complete", expanded=False)
                
                # Show code results outside status
                st.markdown("### 💻 Generated Solution")
                st.code(code, language='python')

                # --- Step 3: Summary ---
                with st.status("📝 **Summarizer Agent** is finishing...", expanded=True) as status:
                    summary_prompt = f"Summarize the following research and code:\n\nRESEARCH:\n{research}\n\nCODE:\n{code}"
                    summary = coordinator.summarizer_agent.think(summary_prompt)
                    status.update(label="✅ Task Finished", state="complete", expanded=False)

                # --- Final Result Display ---
                st.markdown("### 🏁 Final Summary")
                st.info(summary)
                
                # Save assistant response to history
                st.session_state.messages.append({"role": "assistant", "content": summary})

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
