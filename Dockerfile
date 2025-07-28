FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY main.py .
COPY src/ ./src/
COPY approach_explanation.md .
COPY README.md .

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Set Python path
ENV PYTHONPATH=/app

# Set the entrypoint
ENTRYPOINT ["python", "main.py", "/app/output"]

# Add labels for documentation
LABEL maintainer="Adobe Challenge Submission"
LABEL version="1.0.0"
LABEL description="Universal Document Intelligence System for Persona-Driven Document Analysis"
