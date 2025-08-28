FROM python:3.9

# Install PostgreSQL client (psql) for wait-for-db.sh
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

EXPOSE 8000

# ✅ Run as module so imports work
CMD ["python", "-m", "app.main"]
