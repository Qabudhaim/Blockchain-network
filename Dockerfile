FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY /dev/blockchain.py /app
COPY /dev/network.py /app
COPY /dev/requirements.txt /app
# COPY /dev/templates /app/templates

COPY /dev/block_explorer /app/block_explorer
# COPY /dev/block_explorer/.env /app/block_explorer/

# RUN cd /app/block_explorer
# RUN touch .env
# RUN echo "VITE_APP_ADDRESS=1234" >> .env

RUN echo "VITE_APP_ADDRESS=85" > /app/block_explorer/.env

# Install app dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Start the server
CMD ["uvicorn", "network:app", "--host", "0.0.0.0", "--port", "80"]

# sudo docker build -t blockchain .
# sudo docker run --env ADDRESS=85 --network=blockchain_network -p 85:80 blockchain