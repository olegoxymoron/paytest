FROM python:3.7
ADD . /backend
WORKDIR /backend

EXPOSE 5000

RUN pip install -r requirements.txt

ENV FLASK_APP app:app
CMD ["flask", "run", "--host", "0.0.0.0"]
