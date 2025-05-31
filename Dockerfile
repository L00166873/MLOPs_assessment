FROM python:3.9

WORKDIR /opt/mlops_a

COPY requirements_folder/flaskapp.txt .
COPY flaskapp.py .
COPY model.pkl .

RUN pip3 install -r model.txt

EXPOSE 5000
CMD ["python3","flaskapp.py"]
