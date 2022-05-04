FROM python:3.9-slim-buster
WORKDIR /code
COPY ./mysite /code
RUN python -m pip install Django
CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
