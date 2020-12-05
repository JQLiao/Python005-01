import socket
from pathlib import Path
import struct

HOST = 'localhost'
PORT = 10000
uploadPath = Path('C:\\homework\\upload')

def echo_client():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))


    while True:
        fileName = str(input('please input filename:'))
        filePath = uploadPath.joinpath(fileName)
        if filePath.exists():
            fileinfo_size = struct.calcsize('128sI')
            filehead = struct.pack('128sI', fileName.encode('gbk'), os.stat(filePath).st_size)
            s.send(filehead)
            print(f'client send filePath:{filePath}')

            with open(filePath, 'rb') as f:
                data = f.read(1024)
                if not data:
                    print(f'{fileName} send successful')
                    break
                s.send(data)
        break
    s.close()

if __name__ == "__main__":
    echo_client()