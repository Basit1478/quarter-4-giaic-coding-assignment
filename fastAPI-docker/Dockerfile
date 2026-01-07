# Install python version 3.12
FROM python:3.12-slim

# Set working directory (where commands will be executed)
WORKDIR /app

# Copy all files to working directory
COPY . .

# Install uv using pip
RUN pip install uv

# Install all dependencies in the project
RUN uv sync

# Expose application port (localhost:8000 or 127.0.0.1:8000)
EXPOSE 8000

# Run the application (PRODUCTION MODE)
CMD ["uv", "run", "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]