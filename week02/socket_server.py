import socket
from pathlib import Path
import struct

HOST = 'localhost'
PORT = 10000
downPath = Path('C:\\homework\\download')
def echo_server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        fileinfo_size = struct.calcsize('128sI')
        buff = conn.recv(fileinfo_size)
        if buff:
            filename, filesize = struct.unpack('128sI', buff)
            newfile = filename.decode('gbk').strip('\x00')
            filePath = downPath.joinpath(newfile)    
            recv_size = 0   
            with open(filePath, 'wb') as f:
                while not recv_size == filesize:
                    if filesize - recv_size > 1024:
                        data = conn.recv(1024)
                        recv_size += len(data)
                    else:
                        data = conn.recv(filesize - recv_size)
                        recv_size = filesize
                    f.write(data)
        print("finish")
        break
    s.close()


if __name__ == "__main__":
    echo_server()
