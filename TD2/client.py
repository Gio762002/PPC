import sysv_ipc
 
key = 128
 
mq = sysv_ipc.MessageQueue(key)

while True:
    request = int(input("Enter message type (1 for time request, 2 for termination): "))
    mq.send(str(request).encode(), type=request)
    if request == 1:
        message, t = mq.receive()
        if t == 3:
            print("Received time:", message.decode())
    elif request == 2:
        break