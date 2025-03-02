FROM python:3

WORKDIR / app

COPY req.txt .

RUN pip install -r req.txt

COPY . . 

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]