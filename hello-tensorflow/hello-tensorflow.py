import tensorflow as tf
from tensorflow.python.client import device_lib
import socket 

if __name__ == '__main__':
    print('--------------------------------------------------------------')
    print('Hello from Docker Container (', socket.gethostname(),')')
    print('--------------------------------------------------------------')
    print('Tensorflow Version:',tf.__version__)
    print('--------------------------------------------------------------')
    print(device_lib.list_local_devices())
    print('--------------------------------------------------------------')