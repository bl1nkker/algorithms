import random
import string
from time import time


def mutate_solution(current):
    new = current
    first_pos = random.randint(1, len(current) - 2)
    second_pos = random.randint(1, len(current) - 2)
    new[first_pos], new[second_pos] = new[second_pos], new[first_pos]
    return new


def evaluate(solution):
    lenght = 0
    for i in range(len(solution) - 1):
        try:
            lenght += distances[f'{solution[i]}-{solution[i + 1]}']
        except:
            lenght += distances[f'{solution[i + 1]}-{solution[i]}']
    return lenght


distances = {'1-2': 24, '1-3': 31, '1-4': 18, '1-5': 19, '1-6': 40, '1-7': 39, '1-8': 74,
             '2-3': 41, '2-4': 50, '2-5': 67, '2-6': 46, '2-7': 41, '2-8': 65,
             '3-4': 17, '3-5': 37, '3-6': 29, '3-7': 39, '3-8': 65,
             '4-5': 42, '4-6': 39, '4-7': 57, '4-8': 67,
             '5-6': 25, '5-7': 69, '5-8': 17,
             '6-7': 45, '6-8': 37,
             '7-8': 79}

best = [1, 3, 2, 4, 5, 6, 7, 8, 1]
current_len = evaluate(best)

similar = 0
operations = 0

run = True
begin = time()
while run:
    operations += 1
    print(f'Best: {best}, with length: {current_len}')

    new_solution = mutate_solution(best)
    new_len = evaluate(new_solution)

    if new_len < current_len:
        similar = 0
        current_len = new_len
        best = new_solution

    if (new_len == current_len) or (new_len > current_len):
        similar += 1
        if similar >= 1000:
            run = False
end = time()
print(f"Time: {end - begin}, Operations: {operations}")
