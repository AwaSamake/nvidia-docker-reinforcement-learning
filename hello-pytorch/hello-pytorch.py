import datetime
import socket 
import torch

if __name__ == '__main__':
    print('Docker Container:',socket.gethostname(),'Date:', str(datetime.datetime.now()))
    if torch.cuda.is_available():
        print('List of GPUs:'+'\n')
        number_of_gpu = torch.cuda.device_count()
        for i in range(number_of_gpu):
            print('('+str(i)+') '+torch.cuda.get_device_name(i)+'\n')
    else:
        print('GPU is Not available'+'\n')
    