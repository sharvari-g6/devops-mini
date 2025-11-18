FROM python:3.9

WORKDIR /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask flask-cors

# Expose port
EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]

