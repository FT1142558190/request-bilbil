from socket import socket  ,SOCK_STREAM ,AF_INET
from datetime import datetime

def main():
    server = socket(family=AF_INET,type=SOCK_STREAM)
    server.bind(('10.181.14.0',6789))
    server.listen(512)
    print('working')
    while True:
        print('客户')
        client,addr =server.accept()
        print(f'{addr}')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()
if __name__ == '__main__':
    main()