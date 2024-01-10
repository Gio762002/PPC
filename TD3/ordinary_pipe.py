from multiprocessing import Pipe, Process

def send_phrase(conn):
    while True:
        phrase = input("Enter a phrase: ")
        if phrase == 'quit':
            conn.send(phrase)
            break
        conn.send(phrase)
        print(conn.recv())
    conn.close()

def reverse(conn):
    while True:
        phrase = conn.recv()
        if phrase == 'quit':
            break
        conn.send(phrase[::-1])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=reverse, args=(child_conn,))
    p.start()
    send_phrase(parent_conn)
    p.join()
    