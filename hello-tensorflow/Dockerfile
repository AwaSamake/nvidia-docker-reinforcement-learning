FROM nvcr.io/nvidia/tensorflow:18.08-py3

LABEL Name=hello-tensorflow Version=0.0.1

RUN  apt-get update && apt-get install -y cmake=3.5.1-1ubuntu3 

WORKDIR /app
ADD ./requirements.txt /app

RUN pip install -r requirements.txt

WORKDIR /app
ADD . /app

CMD ["python", "-m", "hello-tensorflow"]
