import streamlit as st
import pyttsx3
from qdrant_client import QdrantClient
from response import token

client = QdrantClient(
    url = "<your QDrant URL>", 
    api_key = "<your QDrant API_KEY>",
    check_compatibility = False
)
client.set_model("sentence-transformers/all-MiniLM-L6-v2")
client.set_sparse_model("Qdrant/bm25")
COLLECTION_NAME = "manual"

st.set_page_config(page_title="📘 Product Manual Assistant", page_icon="📘")
st.title("📘 Product Manual Assistant AI")

st.sidebar.header("⚙️ Settings")
rate = st.sidebar.slider("🔊 Speech Rate", 100, 200, 125)
voice_gender = st.sidebar.radio("🎤 Voice", ["Male", "Female"])
enable_voice = st.sidebar.checkbox("Enable Voice Output", value=True)

if "history" not in st.session_state:
    st.session_state.history = []

question = st.chat_input("Ask a question about the product manual...")

if question:
    with st.chat_message("user"):
        st.write(question)

    st.info("🔎 Searching product manual...")

    results = client.query(
        collection_name=COLLECTION_NAME,
        query_text=question,
        limit=5,
    )

    context = "\n".join([r.document for r in results])

    prompt = f"""
    Context: {context}
    Question: {question}
    Based on the context provided, answer the question. Give me as a plain text, don't use md format.
    """

    with st.chat_message("assistant"):
        placeholder = st.empty()
        final_output = ""

        with st.spinner("🧠 Thinking..."):
            for tok in token(prompt, model="gpt-4o-mini"):
                final_output += tok
                placeholder.markdown(final_output)

        st.session_state.history.append((question, final_output))

        if enable_voice:
            engine = pyttsx3.init()
            engine.setProperty('rate', rate)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id if voice_gender == "Female" else voices[0].id)
            engine.say(final_output)
            engine.runAndWait()

if st.session_state.history:
    st.markdown("---")
    st.subheader("🕘 Previous Questions")
    for q, a in reversed(st.session_state.history[-3:]):
        with st.expander(f"🗨️ Q: {q}"):
            st.write(a)

st.markdown("---")
st.markdown("🛠️ Built by [Team M.S.D.](https://github.com/sukeshofficial) | [GitHub Repo](https://github.com/team_msd/product_manual_assistant)", unsafe_allow_html=True)
