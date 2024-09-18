FROM python:3.8-slim-buster
RUN apt-get -y update && apt-get -y install curl
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
EXPOSE 8000

HEALTHCHECK --interval=1m --timeout=3s CMD curl -s -f http://localhost:8000/health

RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

