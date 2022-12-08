FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install flask
RUN pip install mysql-connector-python
COPY . .
CMD ["python", "app.py"]
