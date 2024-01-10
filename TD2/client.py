import sysv_ipc
 
key = 128
 
mq = sysv_ipc.MessageQueue(key)
 
while True:
    request = 1
    try:
        request = int(intput())
    except:
        print("Input error, try again!")
    mq.send(str(request).encode())

    message, t = mq.receive()
    response = message.decode()
    if not response == "0":
        print("received:", value)
    else:
        print("exiting.")
        break

