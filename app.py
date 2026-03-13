import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
# Import your specific retrieval logic here from your existing code

st.set_page_config(page_title="2-Step RAG Demo", page_icon="🤖")
st.title("🦙 Local RAG System (Llama 2 + Nomic)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about your documents"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # This calls your local Ollama instance inside the Docker container
        llm = Ollama(model="llama2")
        # Replace the line below with your actual RAG chain logic
        response = llm.invoke(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})