# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy only requirements file first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
