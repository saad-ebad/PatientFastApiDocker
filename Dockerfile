FROM python:3.9

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ✅ make sure Python sees /code
ENV PYTHONPATH=/code

EXPOSE 8000

CMD ["python", "-m", "app.main"]

