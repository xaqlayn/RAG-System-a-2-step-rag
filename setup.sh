#!/bin/bash

# Define colors for pretty output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Starting Nike RAG Agent Setup...${NC}"

# 1. Start the Docker containers in the background
echo -e "${GREEN}📦 Pulling images and starting containers...${NC}"
docker compose up -d

# 2. Wait for Ollama to be ready
echo -e "${BLUE}⏳ Waiting for AI Engine to initialize...${NC}"
sleep 5

# 3. Pull the specific models required for the RAG Agent
echo -e "${GREEN}🧠 Downloading Llama 3.1 (LLM) and Nomic (Embeddings)...${NC}"
docker exec -it ollama ollama pull llama3.1:8b
docker exec -it ollama ollama pull nomic-embed-text

echo -e "${GREEN}✅ Setup Complete!${NC}"
echo -e "${BLUE}👉 Access your RAG Agent at: http://localhost:8501${NC}"
