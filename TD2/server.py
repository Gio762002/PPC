import sysv_ipc
import time
key = 128
 
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
 
while True:
    message, t = mq.receive()
    if t == 1:
        current_time = time.asctime()
        mq.send(current_time, type=3)
    elif t == 2:
        mq.remove()
        break