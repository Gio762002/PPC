import os
import signal
import time
import multiprocessing

def child_process():
    # Sleep for 5 seconds
    time.sleep(5)
    
    # Send SIGUSR1 signal to the parent process
    os.kill(os.getppid(), signal.SIGUSR1)

if __name__ == '__main__':
    # Create a pipe to handle signal communication
    r, w = os.pipe()

    # Create a child process
    pid = os.fork()

    if pid == 0:  # Child process
        os.close(r)  # Close the unused read end of the pipe in the child
        child_process()
        os._exit(0)  # Exit the child process

    else:  # Parent process
        os.close(w)  # Close the unused write end of the pipe in the parent
        signal_received = False

        def handle_signal(signum, frame):
            nonlocal signal_received
            signal_received = True

        # Set up a signal handler for SIGUSR1
        signal.signal(signal.SIGUSR1, handle_signal)

        try:
            # Wait for the child to terminate or receive a signal
            while True:
                try:
                    # Wait for the signal or timeout after 1 second
                    _, _, _ = os.select([r], [], [], 1)
                    
                    if signal_received:
                        print("Parent: Received SIGUSR1 signal from child. Terminating child.")
                        os.kill(pid, signal.SIGTERM)  # Terminate the child
                        os.waitpid(pid, 0)  # Wait for the child to finish
                        break

                except OSError:
                    # OSError occurs when the child process terminates
                    break

        finally:
            os.close(r)  # Close the read end of the pipe

    print("Parent: Exiting.")
