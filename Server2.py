import socket
try:
    port = 6666
    s = socket.socket()
    s.bind(('' , port))
    s.listen(45)
    print("waiting for client")
    c, addr = s.accept()
    print("new connection from {}".format(addr))

    while True:
        rcvData = c.recv(1024).decode()
        print("client says {}".format(rcvData))

        if rcvData == "bye":
            print("End of connection")
            c.send(sendData.encode())
            s.close()
            break

        else:
            sendData = input("Server >")
            c.send(sendData.encode())
except Exception as err:
       print(err)

#s.close()