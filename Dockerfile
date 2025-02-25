FROM python:3.7.3-slim-stretch

RUN apt-get update -y
RUN apt-get install python3 python3-pip python3-dev python-pip-whl -y
RUN pip install --upgrade pip
RUN apt-get install build-essential libssl-dev libffi-dev -y
RUN pip install --upgrade setuptools
RUN cp [/config] [/app/config]
WORKDIR /app
ADD . /app
RUN pip3 install -r config/req.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
RUN chmod +x ["/config/wsgi.py"]
CMD ["/config/wsgi.py"]
