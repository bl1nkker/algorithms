import pygame
import math
import random


# class for cities
class City(object):
    def __init__(self, pos, rad, surface_params):
        self.pos = pos
        self.radius = rad
        self.surf_params = surface_params

    def draw_city(self):
        pygame.draw.circle(main_win, (0, 127, 255), (self.pos[0], self.pos[1]), self.radius)

    def draw_next(self):
        found = False
        new_x = 0
        len_between = 0
        while not found:
            len_between = random.randint(140, 160)
            ran_sign = random.randint(0, 1)
            new_x = 0
            if ran_sign == 1:
                new_x = self.pos[0] - len_between
            else:
                new_x = self.pos[0] + len_between
            if (new_x > self.radius + 1) and (new_x < self.surf_params[0] - 1):
                found = True
        length_between.append(len_between)

        found = False
        while not found:
            ran_sign = random.randint(0, 1)
            new_y = 0
            if ran_sign == 1:
                new_y = self.pos[1] - (len_between - new_x)
            else:
                new_y = self.pos[1] + (len_between - new_x)
            if (new_y > self.radius + 1) and (new_y < self.surf_params[0] - 1):
                found = True
        return [new_x, new_y]


# class for lines between cities
class Node(object):
    def __init__(self, pos_1_circle, pos_2_circle):
        self.start = pos_1_circle
        self.end = pos_2_circle

    def draw_node(self, color):
        pygame.draw.line(main_win, (227, 38, 64), self.start, self.end)


def draw_situation(solution_alg, len_alg, cities_alg, surface, coords_surf, alg_name):
    main_win.blit(surface, coords_surf)
    for coords in cities_alg:
        new_city = City(coords, radius, surf_params)
        new_city.draw_city()
        nums = num_img.render(f'{cities_alg.index(coords) + 1}', 1, (0, 0, 0))
        main_win.blit(nums, coords)

    for i in range(len(solution_alg) - 1):
        new_node = Node(cities_alg[solution_alg[i] - 1], cities_alg[solution_alg[i + 1] - 1])
        new_node.draw_node((0, 0, 0))

    good = ''
    for city in solution_alg:
        good += f'{city} '
    text = font.render(f'Best way: {good}, with length: {len_alg}', 1, (0, 0, 0))
    text_2 = font.render(alg_name, 1, (0, 0, 0))
    main_win.blit(text_2, (coords_surf[0] + int(surf_params[0] / 2), coords_surf[1] + 5))
    main_win.blit(text, (coords_surf[0] + 15, coords_surf[1] + surf_params[1] - 20))


# create length of Nodes
def get_distance(dist1, dist2):
    distance = math.sqrt((dist2[0] - dist1[0]) ** 2 + (dist2[1] - dist1[1]) ** 2)
    return distance


# evaluate current situation. In our case it evaluates length of solution
def evaluate(solution):
    lenght = 0
    for i in range(len(solution) - 1):
        try:
            lenght += distances[f'{solution[i]} - {solution[i + 1]}']
        except:
            lenght += distances[f'{solution[i + 1]} - {solution[i]}']
    return lenght


# randomly generate new solution (RandomFind)
def random_generated_solution_rf(solution):
    mutated_lst = random.sample(solution[1:-1], len(solution[1:-1]))
    mutated_lst.insert(0, solution[0])
    mutated_lst.append(solution[-1])
    return mutated_lst


# mutate solution (change 1 or 2 elements in solution list)
def mutate_solution_am_hc(solution):
    new = solution
    first_pos = random.randint(1, len(solution) - 2)
    second_pos = random.randint(1, len(solution) - 2)
    new[first_pos], new[second_pos] = new[second_pos], new[first_pos]
    return new


# Only for Annealing method. Calculate probability of passing the bad situation
def probability_am(current_len, new_len):
    random_num = random.randint(0, 100)
    dS = new_len - current_len
    chance = 100 * e ** (-(dS / temper))
    if random_num < chance:
        return [new_len, new_solution_am]
    else:
        return [current_len, current_solution_am]


pygame.init()
pygame.display.set_caption("Optimization Algorithms")
main_win_params = (700, 700)

# Surface params
surf_params = (int(main_win_params[0] / 2), int(main_win_params[1] / 2))
surf_hc_params = (0, 0)
surf_am_params = (int(main_win_params[0] / 2), 0)
surf_rf_params = (0, int(main_win_params[1] / 2))
surf_x_params = (int(main_win_params[0] / 2), int(main_win_params[1] / 2))
main_win = pygame.display.set_mode(main_win_params)

# Surfaces
surf_hc = pygame.Surface((surf_params))
surf_am = pygame.Surface((surf_params))
surf_rf = pygame.Surface((surf_params))
surf_ = pygame.Surface((surf_params))
surf_hc.fill(( 188, 150, 0))
surf_am.fill((0, 188, 150))
surf_rf.fill((100, 150, 150))
surf_.fill((150, 188, 0))

begin_1 = False
begin_2 = False
lim_of_operations = 0
num_of_cities = 0

# Fonts for texts
font_for_nums_menu = pygame.font.SysFont('arial', 50, True, False)
text_menu_cities = pygame.font.SysFont('arial', 50, True, True)
text_menu_operations = pygame.font.SysFont('arial', 35, True, True)
note_menu_font = pygame.font.SysFont('arial', 15, True, True)

coords_menu = [(225, 150), (225, 250), (225, 350), (225, 450)]
coords_menu_2 = [(225, 150), (225, 225), (225, 300), (225, 375), (225, 450)]

# Choose num of cities
while not begin_1:

    main_win.fill((153, 102, 204))
    menu_text = text_menu_cities.render("Choose the number of cities:", 1, (229, 43, 80))
    main_win.blit(menu_text, (100, 10))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu[0][0], coords_menu[0][1], 250, 50))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu[1][0], coords_menu[1][1], 250, 50))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu[2][0], coords_menu[2][1], 250, 50))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu[3][0], coords_menu[3][1], 250, 50))
    note_text = note_menu_font.render(
        "*this program shows the work of different algorithms on the 'Traveling salesman problem'",
        1, (0, 0, 0))
    main_win.blit(note_text, (10, 600))
    for i in range(4):
        nums = font_for_nums_menu.render(f'{i + 5} cities', 1, (0, 0, 0))
        main_win.blit(nums, (coords_menu[i][0] + 20, coords_menu[i][1] - 5))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            if pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 150 and pos_mouse[1] < 200:
                num_of_cities = 4
                begin_1 = True
            elif pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 250 and pos_mouse[1] < 300:
                num_of_cities = 5
                begin_1 = True
            elif pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 350 and pos_mouse[1] < 400:
                num_of_cities = 6
                begin_1 = True
            elif pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 450 and pos_mouse[1] < 500:
                num_of_cities = 7
                begin_1 = True
    pygame.display.update()

# Choose num of operations
while not begin_2:
    operations = [300, 400, 500, 600, 'Endless mode']
    main_win.fill((153, 102, 204))
    menu_text = font_for_nums_menu.render("Choose the number of operations:", 1, (229, 43, 80))
    main_win.blit(menu_text, (10, 10))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu_2[0][0], coords_menu_2[0][1], 250, 50))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu_2[1][0], coords_menu_2[1][1], 250, 50))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu_2[2][0], coords_menu_2[2][1], 250, 50))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu_2[3][0], coords_menu_2[3][1], 250, 50))
    pygame.draw.rect(main_win, (255, 255, 255), (coords_menu_2[4][0], coords_menu_2[4][1], 250, 50))
    for i in range(len(operations)):
        if i == 4:
            nums = text_menu_operations.render(f'{operations[i]}', 1, (0, 0, 0))
        else:
            nums = text_menu_operations.render(f'{operations[i]} operations', 1, (0, 0, 0))
        main_win.blit(nums, (coords_menu_2[i][0] + 20, coords_menu_2[i][1] - 5))
    note_text = note_menu_font.render(
        "*this program shows the work of different algorithms on the 'Traveling salesman problem'",
        1, (0, 0, 0))
    main_win.blit(note_text, (10, 600))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            if pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 150 and pos_mouse[1] < 225:
                lim_of_operations = 300
                begin_2 = True
            elif pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 225 and pos_mouse[1] < 300:
                lim_of_operations = 400
                begin_2 = True
            elif pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 300 and pos_mouse[1] < 375:
                lim_of_operations = 500
                begin_2 = True
            elif pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 375 and pos_mouse[1] < 450:
                lim_of_operations = 600
                begin_2 = True
            elif pos_mouse[0] > 225 and pos_mouse[0] < 475 and pos_mouse[1] > 450 and pos_mouse[1] < 525:
                lim_of_operations = 999999999999
                begin_2 = True

    pygame.display.update()

cities_hc = [[20, 20]]
cities_am = []
cities_rf = []
cities_ = []
font = pygame.font.SysFont('arial', 15, True, False)
num_img = pygame.font.SysFont('arial', 15, True, False)

radius = 15
temper = 100
alpha = 0.95
e = math.e
num_of_operations = 0

length_between = []
distances = {}

for i in range(num_of_cities):
    newCity = City(cities_hc[-1], radius, surf_params)
    cities_hc.append(newCity.draw_next())

for i in range(len(cities_hc) - 1):
    for j in range(i + 1, len(cities_hc)):
        distances[f'{i + 1} - {j + 1}'] = get_distance(cities_hc[i], cities_hc[j])

for city_pos in cities_hc:
    cities_am.append([city_pos[0] + surf_params[0], city_pos[1]])

for city_pos in cities_hc:
    cities_rf.append([city_pos[0], city_pos[1] + surf_params[1]])

for city_pos in cities_hc:
    cities_.append([city_pos[0] + surf_params[0], city_pos[1] + surf_params[1]])

current_solution_hc = []
current_solution_am = []
current_solution_rf = []
current_solution_ = []

for i in range(len(cities_)):
    current_solution_am.append(i + 1)
    current_solution_hc.append(i + 1)
    current_solution_rf.append(i + 1)
    current_solution_.append(i + 1)

current_len_hc = evaluate(current_solution_hc)
current_len_am = evaluate(current_solution_am)
current_len_rf = evaluate(current_solution_rf)
current_len_ = evaluate(current_solution_)

run = True
while run:
    num_of_operations += 1
    draw_situation(current_solution_am, current_len_am, cities_am, surf_am, surf_am_params, 'ANNEALING METHOD')
    draw_situation(current_solution_hc, current_len_hc, cities_hc, surf_hc, surf_hc_params, 'HILL CLINBING')
    draw_situation(current_solution_rf, current_len_rf, cities_rf, surf_rf, surf_rf_params, 'RANDOM FIND')
    draw_situation(current_solution_, current_len_, cities_, surf_, surf_x_params, 'X')

    # Random Find
    new_solution_rf = random_generated_solution_rf(current_solution_rf)
    new_len_rf = evaluate(new_solution_rf)
    if current_len_rf > new_len_rf:
        current_len_rf = new_len_rf
        current_solution_rf = new_solution_rf

    # Annealing Method
    new_solution_am = mutate_solution_am_hc(current_solution_am)
    new_len_am = evaluate(new_solution_am)
    if new_len_am < current_len_am:
        similar = 0
        current_len_am = new_len_am
        current_solution_am = new_solution_am
    elif new_len_am >= current_len_am:
        current_len_am = probability_am(current_len_am, new_len_am)[0]
        best = probability_am(current_len_am, new_len_am)[1]
    temper = temper * alpha

    # Hill Climbing
    new_solution_hc = mutate_solution_am_hc(current_solution_hc)
    new_len_hc = evaluate(new_solution_am)
    if new_len_hc < current_len_hc:
        similar = 0
        current_len_hc = new_len_hc
        current_solution_hc = new_solution_hc

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if num_of_operations == lim_of_operations:
        run = False
    pygame.display.update()
    pygame.time.delay(500)

while 1:
    print()
