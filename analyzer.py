import random
import time
from sorting_algorithms import quicksort, mergesort, bubblesort

# def create_random_list(size, max_val):
#    ran_list = []
#    for num in range(size):
#        ran_list.append(random.randint(1,max_val))
#    return ran_list

def create_random_list(size, max_val):
    return [random.randint(1,max_val) for num in range(size)]

def analyze(func_name, arr):
    start_time = time.time()
    func_name(arr)
    end_time = time.time()
    seconds = end_time-start_time
    print(f"{func_name.__name__.capitalize()}\t Elapsed time: {seconds}")

size = int(input("Enter size of list: "))
max_val = int(input("Enter max value of range: "))

l = create_random_list(size,max_val)
analyze(quicksort,l)
analyze(mergesort,l)
analyze(bubblesort,l.copy())
