FROM python:3.11-slim

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=1000
ENV PIP_RETRIES=10

RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY requirements-ml.txt .

RUN pip install --no-cache-dir setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --timeout 1000 --retries 10 \
    --extra-index-url https://download.pytorch.org/whl/cpu \
    -r requirements-ml.txt


COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]