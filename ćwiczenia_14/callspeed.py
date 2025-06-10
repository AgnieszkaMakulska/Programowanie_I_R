import time
import threading
import multiprocessing
import random
import sys

'''
O progamowaniu równoległym można przeczytać np. tutaj: https://en.wikipedia.org/wiki/Parallel_computing
W Pythonie mamy różne możliwości programowania równoległego:
1. threading - wykonywanie wielu zadań jednocześnie w jednym procesie.
2. multiprocessing - wykonywanie wielu zadań jednocześnie w różnych procesach.

Każdy proces to osobna instancji interpretera Pythona. 
Możemy uruchamiać procesy na osobnych rdzeniach procesora, co pozwala na pełne wykorzystanie mocy obliczeniowej komputera.
'''

def fcall(n, func, *args): 
    ''' Wywołuje funkcję n razy w jednym wątku (*args pozwala przekazać dowolną liczbę argumentów) '''  
    start_time = time.time()
    for _ in range(n):
        func(*args)
    end_time = time.time()
    return end_time - start_time


def fcall_thread(n, func, *args):
    """Wywołuje funkcję n razy w osobnych wątkach."""
    start_time = time.time()
    threads = []
    for _ in range(n):
        thread = threading.Thread(target=func, args=args) #tworzy nowy wątek
        threads.append(thread)
        thread.start() # uruchamia wątek

    for thread in threads:
        thread.join() # czeka na zakończenie wątków

    end_time = time.time()
    return end_time - start_time


def fcall_process(n, func, *args):
    """Wywołuje funkcję n razy w osobnych procesach."""
    start_time = time.time()
    processes = []
    for _ in range(n):
        process = multiprocessing.Process(target=func, args=args) #tworzy nowy proces
        processes.append(process)
        process.start() # uruchamia proces

    for process in processes:
        process.join() # czeka na zakończenie procesów

    end_time = time.time()
    return end_time - start_time


#Przykładowa funkcja do testowania
def create_and_sort_list(size):
    random_list = [random.random() for _ in range(size)]
    random_list.sort()

k = int(sys.argv[1]) if len(sys.argv) > 1 else 5 # 5 wątków lub procesów
print(f"Uruchamianie testów z k={k}\n")
size = 1000000 # rozmiar listy do sortowania

time_fcall = fcall(k, create_and_sort_list, size)
print(f"  fcall: {time_fcall:.4f} s")

time_fcall_thread = fcall_thread(k, create_and_sort_list, size)
print(f"  fcall_thread: {time_fcall_thread:.4f} s")

time_fcall_process = fcall_process(k, create_and_sort_list, size)
print(f"  fcall_process: {time_fcall_process:.4f} s\n")