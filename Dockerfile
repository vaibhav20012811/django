FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "ecom_config.wsgi:application"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
