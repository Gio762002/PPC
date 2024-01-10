import sysv_ipc
import time
key = 128
 
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
 
value = 1
while value:
    message_receive, t = mq.receive()
    value = message_received.decode()
    value = int(value)
    if value == 1:
        time = time.asctime()
        message_send = str(time).encode()
        mq.send(message_send)
    elif value != 0:
        message_send = "enter 1 to get current time, 0 to exit".encode()
        mq.send(message_send)
    else:
        mq.send(str(0).encode())
        print("exiting.")
mq.remove()