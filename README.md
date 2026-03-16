# 👟 Nike 10K - Local RAG Agent System

A high-performance **RAG Agent** application designed to query complex financial documents (Nike 2023 10-K) using a fully **local LLM stack**. This project demonstrates a production-grade AI pipeline focused on **data privacy**, **LangChain orchestration**, and **Docker containerization**.

## 🔐 Privacy-First Architecture
Unlike cloud-based AI solutions, this system is built for maximum data security:
- **100% Local Inference:** Powered by Ollama; no data ever leaves your local environment.
- **Privacy-Compliant:** Ideal for sensitive financial documents where cloud uploads are restricted.
- **No Third-Party APIs:** Eliminates dependency on OpenAI, Anthropic, or other external providers.

## 🧠 System Architecture: The Agentic Approach
This system utilizes an autonomous **RAG Agent** workflow:
1.  **Tool Reasoning:** The LLM (Llama 3.1) dynamically decides when to consult the Nike 10-K report based on user intent.
2.  **Autonomous Retrieval:** The Agent uses a specialized `retriever_tool` and **Nomic Embeddings** to extract high-precision data from the vector store.
3.  **Synthesized Response:** The Agent synthesizes the findings into a coherent response, grounded strictly in the provided local context.

---

## 🛠️ Tech Stack
* **LLM:** Llama 3.1:8b (Local via Ollama)
* **Embeddings:** Nomic-Embed-Text (Local via Ollama)
* **Agent Framework:** LangChain (ChatOllama, AgentExecutor)
* **UI:** Streamlit
* **DevOps:** Docker, Docker Hub, Docker Compose

---

## 🚀 Deployment & Installation

## ⚡ Quick Start (The One-Click Way)
If you have Docker installed, simply run the setup script to pull the images and models automatically:


chmod +x setup.sh
./setup.sh
---

## 🔧 Technical Challenges Overcome
* **Local Optimization:** Configured the system to run efficiently on local hardware with 8GB RAM using `python-slim` images.
* **Service Isolation:** Used Docker Compose to isolate the AI engine from the UI, communicating solely through a secure internal bridge network.
* **Agent Logic:** Fine-tuned the retrieval chain to prevent the Agent from "hallucinating" facts outside of the provided Nike 10-K context.

---

### 🐳 Option A: The Docker Way (Recommended)
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/xaqlayn/RAG-System-a-2-step-rag.git](https://github.com/xaqlayn/RAG-System-a-2-step-rag.git)
    cd RAG-System-a-2-step-rag
    ```
2.  **Launch the System:**
    ```bash
    docker compose up -d
    ```
3.  **Initialize the Local Models:**
    ```bash
    docker exec -it ollama ollama pull llama3.1:8b
    docker exec -it ollama ollama pull nomic-embed-text
    ```
4.  **View the App:** Go to [http://localhost:8501](http://localhost:8501)

---
### 🐍 Option B: Local Development (PyCharm/Terminal)
If you want to run the code directly on your machine:

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Ensure Ollama is running** on your Mac/PC and pull the models:
    ```bash
    ollama pull llama3.1:8b
    ollama pull nomic-embed-text
    ```

3.  **Run the UI:**
    ```bash
    streamlit run app.py
    ```

---


## 👨‍💻 Author
**Saqlain Majeed** [GitHub](https://github.com/xaqlayn) | [Docker Hub](https://hub.docker.com/u/xack1122)
