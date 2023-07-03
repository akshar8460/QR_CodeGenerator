# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code into the container
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "main.py"]
