FROM shahil/nvidia-docker-rl

WORKDIR /app

#COPY requirements.txt ./app
#RUN pip install --no-cache-dir -r requirements.txt

ADD . /app

CMD [ "python3", "hello-pytorch.py" ]