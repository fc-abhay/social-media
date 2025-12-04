# Use official Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Django port
EXPOSE 8000

# Run Django server using gunicorn
CMD ["gunicorn", "YOUR_PROJECT_NAME.wsgi:application", "--bind", "0.0.0.0:8000"]
