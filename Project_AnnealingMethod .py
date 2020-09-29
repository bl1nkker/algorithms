import random
import math
from time import time

e = math.e


def mutate_solution(current):
    new = current
    first_pos = random.randint(1, len(current) - 2)
    second_pos = random.randint(1, len(current) - 2)
    new[first_pos], new[second_pos] = new[second_pos], new[first_pos]
    return new


def full_distance(solution):
    lenght = 0
    for i in range(len(solution) - 1):
        try:
            lenght += distances[f'{solution[i]}-{solution[i + 1]}']
        except:
            lenght += distances[f'{solution[i + 1]}-{solution[i]}']
    return lenght


def probability(current, new):
    random_num = random.randint(0, 100)
    dS = new - current
    chance = 100 * e ** (-(dS / temper))
    if random_num < chance:
        return [new, new_solution]
    else:
        return [current, best]


# При "рандомном словаре" удалить все цифры, превратить словарь в список и поставить distancesLst вместо distances
distances = {'1-2': 24, '1-3': 31, '1-4': 18, '1-5': 19, '1-6': 40,
             '2-3': 41, '2-4': 50, '2-5': 67, '2-6': 46,
             '3-4': 17, '3-5': 37, '3-6': 29,
             '4-5': 42, '4-6': 39,
             '5-6': 25}

# distances = {}
# for dist in distancesLst:
#     distances[dist] = random.randint(10, 50)
# print(distances)


best = [1, 4, 3, 5, 6, 2, 1]
current_len = full_distance(best)
temper = 100
alpha = 0.95
similar = 0
operations = 0


run = True
begin = time()
while run:
    operations += 1
    print(f'Best: {best}, with length: {current_len}, temperature at the mo: {temper}')

    new_solution = mutate_solution(best)
    new_len = full_distance(new_solution)

    if new_len < current_len:
        similar = 0
        current_len = new_len
        best = new_solution

    elif new_len > current_len:
        current_len = probability(current_len, new_len)[0]
        best = probability(current_len, new_len)[1]

    if new_len == current_len or best == current_len:
        similar += 1
        if similar == 50:
            run = False

    temper = temper * alpha

end = time()
print(f"Time: {end - begin}, Operations: {operations}")
