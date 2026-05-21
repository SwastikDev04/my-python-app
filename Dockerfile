# Use a lightweight official Python image
FROM python:3.10-slim

# Install system dependencies (needed for the ping utility tool)
RUN apt-get update && apt-get install -y \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy and install Python requirements
# Make sure your requirements.txt contains: fastapi, uvicorn, streamlit
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY main.py app.py start.sh ./

# Make the startup script executable
RUN chmod +x start.sh

# Expose both the API port and the Streamlit port
EXPOSE 8000
EXPOSE 8501

# Execute the startup script
CMD ["./start.sh"]
