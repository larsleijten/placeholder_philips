FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY *.py .
COPY images /images/
CMD ["python", "app.py"]