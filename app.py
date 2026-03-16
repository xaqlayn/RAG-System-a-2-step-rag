import streamlit as st
import requests
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage

# Import your local modules
import Pipeline_steps
import Configuration
import Retriever_tool_agent_setup

# 1. Setup
Configuration.configure_environment()
settings = Configuration.Settings()

st.set_page_config(page_title="Nike 10K RAG", page_icon="👟")
# --- SIDEBAR STATUS ---
with st.sidebar:
    st.header("⚙️ System Status")

    # Check if Ollama container is reachable
    try:
        # Configuration.Settings().ollama_host might be needed here
        response = requests.get("http://ollama:11434/api/tags", timeout=2)
        if response.status_code == 200:
            st.success("● Ollama: Connected")
        else:
            st.warning("● Ollama: Starting...")
    except:
        st.error("● Ollama: Disconnected")

    st.divider()
    st.info("Ensure you have run `ollama pull` for Llama 3.1 and Nomic inside the container.")

st.title("👟 Nike's RAG system")


# 2. Cache the Pipeline
@st.cache_resource
def initialize_rag():
    docs = Pipeline_steps.load_pdf(settings.pdf_path)

    # We must include all 3 keyword arguments exactly like this:
    chunks = Pipeline_steps.split_documents(
        docs,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        add_start_index=settings.add_start_index  # <--- This was the missing piece!
    )

    embeddings = OllamaEmbeddings(model=settings.embedding_model)
    vector_store = Pipeline_steps.build_vector_store(chunks, embeddings)
    retriever_chain = Retriever_tool_agent_setup.make_retriever_chain(vector_store)
    return retriever_chain


retriever_chain = initialize_rag()

# 3. Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Chat Input
if prompt := st.chat_input("Ask about Nike's 10k..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing documents..."):
            # A. Retrieve Context
            retrieved_docs = retriever_chain.invoke(prompt)
            context = "\n\n".join([d.page_content for d in retrieved_docs])

            # B. Initialize ChatOllama
            llm = ChatOllama(model=settings.llm_model, temperature=settings.temperature)

            # C. Create Structured Messages
            messages = [
                SystemMessage(
                    content="You are a helpful financial assistant. Use the provided context to answer questions. If the answer isn't there, say you don't know."),
                HumanMessage(content=f"Context:\n{context}\n\nQuestion: {prompt}")
            ]

            # D. Invoke with Streaming
            placeholder = st.empty()  # Create a blank space for the text
            full_response = ""

            # Using .stream() instead of .invoke()
            for chunk in llm.stream(messages):
                full_response += chunk.content
                placeholder.markdown(full_response + "▌")  # Add a cursor effect

            placeholder.markdown(full_response)  # Final render without cursor

            # Save to session state
            st.session_state.messages.append({"role": "assistant", "content": full_response})

            # The View Sources expander stays the same
            with st.expander("🔍 View Sources"):
                for doc in retrieved_docs:
                    st.write(f"• {doc.page_content[:150]}...")