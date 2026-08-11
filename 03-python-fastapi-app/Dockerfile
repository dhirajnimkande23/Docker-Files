# =============================================================
# Python FastAPI Application
# Base image: python:3.12-slim (latest stable, minimal footprint)
# =============================================================
FROM python:3.12-slim

# ── Step 1: Set the working directory inside the container ──
WORKDIR /app

# ── Step 2: Copy requirements first to leverage Docker layer caching ──
COPY requirements.txt .

# ── Step 3: Install Python dependencies without cache to keep image small ──
RUN pip install --no-cache-dir -r requirements.txt

# ── Step 4: Copy the rest of the application source code ──
COPY . .

# ── Step 5: Expose the port Uvicorn listens on ──
EXPOSE 8000

# ── Step 6: Start the Uvicorn ASGI server ──
#    --host 0.0.0.0  → accept connections from outside the container
#    --port 8000     → must match EXPOSE above
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
