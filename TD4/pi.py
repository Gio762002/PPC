import threading
import random

def generate_random_point(generated_point):
    print("Starting thread:", threading.current_thread().name)
    total_number_of_points=1000000
    for i in range(total_number_of_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        generated_point.append((x,y))
    print("Ending thread:", threading.current_thread().name)
    return generated_point

if __name__ == '__main__':
    generated_point = []
    print("Starting thread:", threading.current_thread().name)
    thread = threading.Thread(target=generate_random_point, args=(generated_point,))
    thread.start()
    thread.join()
    print("Ending thread:", threading.current_thread().name)
    
    number_of_points_in_circle = 0
    for (x,y) in generated_point:
        if x**2 + y**2 <= 1:
            number_of_points_in_circle += 1
    pi = 4 * number_of_points_in_circle / len(generated_point)
    print("Pi: ", pi)