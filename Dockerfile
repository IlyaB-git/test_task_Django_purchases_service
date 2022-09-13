FROM python:3.10.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /app/
WORKDIR /app/
COPY . .
EXPOSE 8000
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "project/manage.py", "runserver"]
