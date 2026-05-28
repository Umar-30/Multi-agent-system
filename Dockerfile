# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Streamlit will run on (Hugging Face uses 7860)
EXPOSE 7860

# Healthcheck to ensure the container is running correctly
HEALTHCHECK CMD curl --fail http://localhost:7860/_stcore/health

# Run streamlit when the container launches
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
