FROM python:3.11-slim

WORKDIR /

RUN pip install duckdb numpy pandas "pyiceberg[duckdb,s3fs,sql-postgres]"

# Copy application code
COPY src/insert_data_pyiceberg.py /app.py

CMD ["python", "app.py"]