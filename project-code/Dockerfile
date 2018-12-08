FROM python:2-alpine
FROM python:2 

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install psutil
RUN pip install numpy
RUN pip install pandas
RUN pip install statsmodels
RUN pip install sklearn
RUN pip install azureml
RUN pip install flask
RUN pip install scipy



COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["-m", "swagger_server"]
