# Use Python 3.10
FROM python:3.10-slim

# Install system dependencies & Ollama
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Create a script to run Ollama and the App together
RUN printf "#!/bin/bash\nollama serve &\nsleep 10\nollama pull llama2\nollama pull nomic-embed-text\nstreamlit run app.py --server.port 7860 --server.address 0.0.0.0" > entrypoint.sh
RUN chmod +x entrypoint.sh

# Expose Hugging Face's default port
EXPOSE 7860

# Run the startup script
ENTRYPOINT ["./entrypoint.sh"]