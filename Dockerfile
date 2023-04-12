FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY /dev/blockchain.py /app
COPY /dev/network.py /app
COPY /dev/requirements.txt /app
COPY /dev/templates /app/templates

# Install app dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Start the server
CMD ["uvicorn", "network:app", "--host", "0.0.0.0", "--port", "80"]
