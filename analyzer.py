import random
import sorting_algorithms

# def create_random_list(size, max_val):
#    ran_list = []
#    for num in range(size):
#        ran_list.append(random.randint(1,max_val))
#    return ran_list

def create_random_list(size, max_val):
    return [random.randint(1,max_val) for num in range(size)]


size = input("Enter size of list: ")
max_val = input("Enter max value of range: ")

print(create_random_list(size,max_val))
