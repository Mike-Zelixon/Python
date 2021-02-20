import socket
try:
    s = socket.socket()
    s.connect(('', 6666))

    while True:
            sendData = input("Client >")
            s.send(sendData.encode())

            rcvData = s.recv(1024).decode()
            print("the server says {}".format(rcvData))

            if rcvData == "bye":
                print("End of connection")
                s.send(sendData.encode())
                s.close()
                break

            #else:
                #sendData = input("Client >")
                #s.send(sendData.encode())
except Exception as err:
    print(err)
