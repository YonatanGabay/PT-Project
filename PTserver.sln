import socket
import sys


def main():
    serv_soc = socket.socket()
    serv_soc.bind(("0.0.0.0",8231))

    serv_soc.listen(1)

    print "waiting for connection..."
    client_soc,client_address = serv_soc.accept()
    print "got connection from",client_address

    client_data = client_soc.recv(1024)
    client_soc.send("got " + client_data)

    print client_data
    client_soc.close()
    serv_soc.close()







if __name__=="__main__":
    main()
