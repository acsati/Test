FROM python

WORKDIR /code

RUN pip install Flask

COPY app.py .

CMD ["python", "./app.py"]
