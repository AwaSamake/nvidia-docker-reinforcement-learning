FROM shahil/nvidia-docker-rl

RUN apt-get update && apt install -y libsm6 libxext6 libfontconfig1 libxrender1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt 
RUN pip3 install -r requirements.txt

ADD . /app

CMD [ "python3", "train_atari.py" ]