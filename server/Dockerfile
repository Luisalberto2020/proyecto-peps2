FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install flask
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
