import random
from time import time

distances = {'1-2': 24, '1-3': 31, '1-4': 18, '1-5': 19, '1-6': 40, '1-7': 39, '1-8': 74,
             '2-3': 41, '2-4': 50, '2-5': 67, '2-6': 46, '2-7': 41, '2-8': 65,
             '3-4': 17, '3-5': 37, '3-6': 29, '3-7': 39, '3-8': 65,
             '4-5': 42, '4-6': 39, '4-7': 57, '4-8': 67,
             '5-6': 25, '5-7': 69, '5-8': 17,
             '6-7': 45, '6-8': 37,
             '7-8': 79}


def random_generated_lst(current_lst):
    mutated_lst = random.sample(current_lst[1:-1], len(current_lst[1:-1]))
    mutated_lst.insert(0, current_lst[0])
    mutated_lst.append(current_lst[-1])
    return mutated_lst


def sum_len(lst):
    length = 0
    for i in range(len(lst) - 1):
        try:
            length += distances[f'{lst[i]}-{lst[i + 1]}']
        except:
            length += distances[f'{lst[i + 1]}-{lst[i]}']
    return length


current = [1, 2, 3, 4, 5, 6, 7, 8, 1]
current_length = sum_len(current)
similar_count = 0
operations = 0

begin = time()
run = True
while run:
    operations += 1
    print(f"Current: {current}, with length: {current_length}")
    new_lst = random_generated_lst(current)
    new_len = sum_len(new_lst)
    if new_len < current_length:
        similar_count = 0
        current_length = new_len
        current = new_lst

    elif (new_len == current_length) or (new_len > current_length):
        similar_count += 1
        if similar_count >= 1000:
            run = False

end = time()
print(f"Time: {end - begin}, Operations: {operations}")
