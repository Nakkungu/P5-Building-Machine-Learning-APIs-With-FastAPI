# Set up a base image for your container
FROM python:3.11.9

# Install system dependencies (Rust and Cargo)
RUN apt-get update && \
    apt-get install -y rustc cargo && \
    rm -rf /var/lib/apt/lists/*

# Create a working directory for the container for the application
WORKDIR /app

# Copy the contents of the requirements.txt file into the container
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy all the files and folders into the container's working directory
COPY . .

# Expose the port
EXPOSE 8077

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8077"]
