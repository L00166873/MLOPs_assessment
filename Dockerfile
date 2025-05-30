FROM python:3.9

WORKDIR /opt/mlops_a
COPY . .

RUN pip3 install -r requirements.txt
RUN python3 model.py

EXPOSE 5000
CMD ["python3","flaskapp.py"]
