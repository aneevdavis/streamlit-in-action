# Start with Python 3.12 as base image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
# (We do this first to leverage Docker's layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Set Streamlit to run in headless mode
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Command to run when the container starts
CMD ["streamlit", "run", "main.py"]
