import random


# def create_random_list(size, max_val):
#    ran_list = []
#    for num in range(size):
#        ran_list.append(random.randint(1,max_val))
#    return ran_list

def create_random_list(size, max_val):
    return [random.randint(1,max_val) for num in range(size)]

print(create_random_list(100,100))
