import multiprocessing 
import sys
from multiprocessing import Process, Value, Array

def fibonacci(s):
    n = len(s)

    for i in range(2, n):
        s[i] = s[i-1] + s[i-2]



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fibo_value_array.py <index>")
        sys.exit(1)

    try:
        index = int(sys.argv[1])
        if index < 1:
            raise ValueError("Index should be a positive integer.")
        sequence = Array('i', range(index+1))
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    process = multiprocessing.Process(target=fibonacci, args=(sequence,))
    process.start()
    process.join()
    print(sequence[:])