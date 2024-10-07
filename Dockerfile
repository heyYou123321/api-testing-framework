# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set environment variable to treat src as a package root
ENV PYTHONPATH=/app/src

# Run the tests
CMD ["pytest -v tests/integration_test/tests_api.py", "--html=src/reporting/report.html"]
