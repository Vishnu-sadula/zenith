# ---------- builder ----------

FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements*.txt ./

RUN pip install --no-cache-dir --upgrade pip wheel && pip wheel --no-cache-dir --no-deps -w /wheels -r requirements.txt

# ---------- runtime ----------
FROM python:3.11-slim AS runtime

WORKDIR /app

ENV FLASK_APP=app.py

COPY --from=builder /wheels /wheels

COPY requirements*.txt ./

RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt && rm -rf /wheels

COPY . .

CMD ["python", "app.py"]