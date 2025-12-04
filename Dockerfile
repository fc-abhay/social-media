# Use official Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run the Django app with gunicorn
CMD ["gunicorn", "server.wsgi:application", "--bind", "0.0.0.0:8000"]
