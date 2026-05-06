FROM python:3.11

WORKDIR /app

COPY app/requirements.txt ./
RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 5000

ENV FLASK_APP=app/index.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]