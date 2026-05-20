# Use a lightweight official Python image
FROM python:3.11-slim

# Install system utilities needed for network ping tools inside Linux containers
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

# Set the active working directory inside the container
WORKDIR /app

# Copy the app script into the container workspace
COPY app.py /app/

# Install the required Python dependencies
RUN pip install --no-cache-dir streamlit

# Streamlit uses port 8501 by default
EXPOSE 8501

# Command to execute the app and bind it to standard container networking parameters
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
