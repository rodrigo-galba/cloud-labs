FROM python:3.12

WORKDIR /app

COPY src/ /app/src

WORKDIR /app/src

# CMD ["python", "./script.py"]
CMD ["sh", "-c", "python write_logs.py && python read_logs.py"]