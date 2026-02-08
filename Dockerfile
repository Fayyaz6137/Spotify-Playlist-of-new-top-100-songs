# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir spotipy python-dotenv beautifulsoup4 requests

# Expose port for Spotify OAuth callback (if needed)
EXPOSE 8888

# Run the script
CMD ["python", "main.py"]
