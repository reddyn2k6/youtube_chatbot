import streamlit as st
from src.pipeline import final_pipeline

st.set_page_config(
    page_title="YouTube ChatBot",
    page_icon="🎥",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

.stTextInput > div > div > input {
    border-radius: 12px;
}

.stTextArea textarea {
    border-radius: 12px;
}

.result-box {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #2d3139;
    color: white;
    font-size: 16px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🎥 YouTube ChatBot")
    st.markdown("---")
    st.markdown("""
    Ask questions about any YouTube video.

    **How it works:**
    - Extract transcript
    - Chunk text
    - Create embeddings
    - Retrieve relevant context
    - Query Gemini
    """)
    st.markdown("---")
    st.info("Built with LangChain + Streamlit")

# Main UI
st.title("🎬 Chat with YouTube Videos")
st.caption("Paste a YouTube link and ask anything about the video")

col1, col2 = st.columns([3, 2])

with col1:
    youtube_url = st.text_input(
        "Enter YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=..."
    )

with col2:
    question = st.text_input(
        "Ask your question",
        placeholder="What is this video about?"
    )

if st.button("🚀 Ask", use_container_width=True):
    if not youtube_url:
        st.warning("Please enter a YouTube URL.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing video..."):
            try:
                answer = final_pipeline(youtube_url, question)

                st.markdown("## Answer")
                st.markdown(
                    f"""
                    <div class="result-box">
                        {answer}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")