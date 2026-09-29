FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Keep the service importable as the `hello_svc` package in the image as well as
# from the repository's test suite.
COPY *.py hello_svc/

EXPOSE 8000

CMD ["uvicorn", "--app-dir", "hello_svc", "main:app", "--host", "0.0.0.0", "--port", "8000"]
