# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn[standard]

# Copy application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the server with hot reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]