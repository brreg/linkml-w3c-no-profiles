FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# server.py og policies/ vert montert inn ved køyring (sjå MCP_RUN i Makefile).
# Legg att ein tom placeholder slik at CMD ikkje feilar ved bygg utan mount.
RUN touch server.py

RUN useradd -m mcp
USER mcp

CMD ["python", "server.py"]
