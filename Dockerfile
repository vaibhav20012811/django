# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker's caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Expose the port
EXPOSE 8000

# Set the default command for the container
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "ecom_config.wsgi:application"]
