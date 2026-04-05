FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for XGBoost (libomp)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY pages/ pages/

# Copy data files from parent project directories (needed by Credit Risk page)
# These get baked into the image at build time
COPY data/ data/

EXPOSE 8080

# Cloud Run sets PORT env var — Streamlit must bind to it
ENV PORT=8080

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:${PORT}/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", \
    "--server.port=8080", \
    "--server.address=0.0.0.0", \
    "--server.headless=true", \
    "--browser.gatherUsageStats=false", \
    "--server.fileWatcherType=none"]
