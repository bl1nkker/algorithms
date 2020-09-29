import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((1050, 625))
pygame.display.set_caption("Optimization Algorithms (second)")


def draw_on_surf(display, surf_pos, img, rad, current, chosen_coords, chosen_names, city_font, len_sol, alg_name):
    display.blit(img, surf_pos)
    for coords in chosen_coords:
        pygame.draw.circle(display, (0, 0, 0), (coords[0] + surf_pos[0], coords[1] + surf_pos[1]), rad), 'Random Find'

    # Node
    for i in range(len(current) - 1):
        pygame.draw.line(display, (220, 50, 50), (chosen_coords[chosen_names.index(current[i])][0] + surf_pos[0],
                                                  chosen_coords[chosen_names.index(current[i])][1] + surf_pos[1]),
                         (chosen_coords[chosen_names.index(current[i + 1])][0] + surf_pos[0],
                          chosen_coords[chosen_names.index(current[i + 1])][1] + surf_pos[1]))

    for i in range(len(chosen_coords)):
        city_text = city_font.render(f'{chosen_names[i]}', 1, (43, 43, 80))
        display.blit(city_text, (chosen_coords[i][0] + surf_pos[0], chosen_coords[i][1] + surf_pos[1] - 15))

    good = ''
    for city_name in current:
        good += f'{city_name} '
    besties = smol_font.render(f'Best way: {good}, with len: {len_sol}', 1, (0, 0, 0))
    length = smol_font.render(f'Length: {len_sol}', 1, (0, 0, 0))
    alg_title = not_so_smol.render(alg_name, 1, (0, 0, 0))
    display.blit(alg_title, (surf_pos[0] + 20, surf_pos[1] + 30))
    display.blit(besties, (surf_pos[0], surf_pos[1] + 280))
    display.blit(length, (surf_pos[0] + 10, surf_pos[1] + 290))
    pygame.display.update()


def evaluate(distances, solution):
    lenght = 0
    for i in range(len(solution) - 1):
        try:
            lenght += distances[f'{solution[i]}-{solution[i + 1]}']
        except:
            lenght += distances[f'{solution[i + 1]}-{solution[i]}']
    return lenght


def get_distance(dist1, dist2):
    distance = math.sqrt((dist2[0] - dist1[0]) ** 2 + (dist2[1] - dist1[1]) ** 2)
    return distance


def create_distances(country_coords, country_names):
    distances = {}
    for i in range(len(country_coords)):
        for j in range(i + 1, len(country_coords)):
            distances[f'{country_names[i]}-{country_names[j]}'] = (
                int(get_distance(country_coords[i], country_coords[j])))
    return distances


def len_total_distance(dist):
    total = 0
    for value in dist.values():
        total += value
    return total


def random_generated_solution_rf(solution):
    mutated_lst = random.sample(solution[1:-1], len(solution[1:-1]))
    mutated_lst.insert(0, solution[0])
    mutated_lst.append(solution[-1])
    return mutated_lst


def mutate_solution_am_hc(solution):
    new = solution
    first_pos = random.randint(1, len(solution) - 2)
    second_pos = random.randint(1, len(solution) - 2)
    new[first_pos], new[second_pos] = new[second_pos], new[first_pos]
    return new


def probability_am(current_len, new_len):
    random_num = random.randint(0, 100)
    dS = new_len - current_len
    chance = 100 * e ** (-(dS / temper))
    if random_num < chance:
        return [new_len, new_solution_am]
    else:
        return [current_len, current_solution_am]


# Variables, needed for algorithms
radius = 4
temper = 100
alpha = 0.95
e = math.e
num_of_operations = 0

countries = ['Kazakhstan', 'Russia', 'USA']

# Countries initialization: Cities positions, names, background maps and country flags
kazakhstan_coords = [[225, 60], [300, 90], [370, 235], [370, 75], [285, 250],
                     [70, 220], [285, 60], [80, 165], [330, 120], [90, 100], [225, 60]]
kazakhstan_names = ['Kostanay', 'Astana', 'Almaty', 'Pavlodar', 'Shymkent', 'Aktau', 'Kokshetau', 'Atyrau', 'Karaganda'
    , 'Uralsk', 'Kostanay']
KzImage = pygame.image.load('kazakhstan.png')
kz_flag = pygame.image.load('kz_flag.jpg')
distances_kz = create_distances(kazakhstan_coords, kazakhstan_names)

russia_coords = [[55, 185], [453, 50], [30, 235], [185, 260], [155, 230], [225, 167], [230, 237], [325, 280],
                 [448, 140], [75, 145], [55, 185]]
russia_names = ['Moscow', 'Anadyr', 'Saratov', 'Omsk', 'Ekaterinburg', 'Norilsk', 'Tomsk', 'Irkutsk',
                'Magadan', 'Saint-Peterburg', 'Moscow']
RuImage = pygame.image.load('russia.jpg')
ru_flag = pygame.image.load('ru_flag.jpg')
distances_ru = create_distances(russia_coords, russia_names)

usa_coords = [[420, 155], [390, 235], [7, 130], [240, 110], [445, 105], [70, 165], [33, 187], [255, 265], [300, 195],
              [430, 127], [420, 155]]
usa_names = ['Washington', 'Orlando', 'San-Francisco', 'Chicago', 'Boston', 'Las-Vegas', 'Los-Angeles', 'Huston',
             'Memphis',
             'New-York', 'Washington']
UsaImage = pygame.image.load('usa.jpg')
usa_flag = pygame.image.load('usa_flag.jpg')
distances_usa = create_distances(usa_coords, usa_names)

choosen_coords = []
choosen_names = []
choosen_img = 0
choosenDict = {}

# Fonts for PyGame
big_font = pygame.font.SysFont('arial', 50, True, False)
medium_font = pygame.font.SysFont('arial', 35, True, True)
not_so_smol = pygame.font.SysFont('arial', 20, True, True)
smol_font = pygame.font.SysFont('arial', 10, True, False)

# Coordinates for menu bars
coords_menu = [(400, 150), (400, 250), (400, 350), (400, 450)]
coords_menu_2 = [(225, 150), (225, 225), (225, 300), (225, 375), (225, 450)]

# Menu "Choose the Country"
begin_1 = False
while not begin_1:
    screen.fill((50, 50, 50))
    menu_text = big_font.render("Choose the country:", 1, (225, 225, 225))
    screen.blit(menu_text, (300, 10))

    # Creating Buttons...
    rect_kz = (coords_menu[0][0], coords_menu[0][1], 250, 50)
    rect_ru = (coords_menu[1][0], coords_menu[1][1])
    rect_usa = (coords_menu[2][0], coords_menu[2][1])
    screen.blit(kz_flag, rect_kz)
    screen.blit(ru_flag, rect_ru)
    screen.blit(usa_flag, rect_usa)
    note_text = smol_font.render(
        "*this program shows the work of different algorithms on the 'Traveling salesman problem'",
        1, (0, 0, 0))
    screen.blit(note_text, (10, 600))

    # On Button Events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            print(pos_mouse)
            if pos_mouse[0] > 400 and pos_mouse[0] < 650 and pos_mouse[1] > 150 and pos_mouse[1] < 200:
                choosen_coords = kazakhstan_coords
                choosen_names = kazakhstan_names
                choosen_img = KzImage
                choosenDict = distances_kz
                begin_1 = True
            elif pos_mouse[0] > 400 and pos_mouse[0] < 650 and pos_mouse[1] > 250 and pos_mouse[1] < 300:
                choosen_coords = russia_coords
                choosen_names = russia_names
                choosen_img = RuImage
                choosenDict = distances_ru
                begin_1 = True
            elif pos_mouse[0] > 400 and pos_mouse[0] < 650 and pos_mouse[1] > 350 and pos_mouse[1] < 400:
                choosen_coords = usa_coords
                choosen_names = usa_names
                choosen_img = UsaImage
                choosenDict = distances_usa
                begin_1 = True
    pygame.display.update()

# 4 surfaces that divide main display
surf_hc = (0, 0)  # hc- Hill Climbing
current_solution_hc = choosen_names[:]
current_len_hc = evaluate(choosenDict, current_solution_hc)

surf_am = (525, 0)  # am- Annealing Method
current_solution_am = choosen_names[:]
current_len_am = evaluate(choosenDict, current_solution_am)

surf_rf = (0, 325)  # rf- Random Find(not Algorithm actually)
current_solution_rf = choosen_names[:]
current_len_rf = evaluate(choosenDict, current_solution_rf)

surf_x = (525, 325)  # x- Nothing. If you want, you can implement your algorithm
current_solution_x = choosen_names[:]
current_len_x = evaluate(choosenDict, current_solution_x)

run = True
screen.fill((0, 0, 0))
# Main loop
while run:
    # Draw on Display
    draw_on_surf(screen, surf_hc, choosen_img, radius, current_solution_hc, choosen_coords,
                 choosen_names, smol_font, current_len_hc, 'Hill Climbing')
    draw_on_surf(screen, surf_am, choosen_img, radius, current_solution_am, choosen_coords,
                 choosen_names, smol_font, current_len_am, 'Annealing Method')
    draw_on_surf(screen, surf_rf, choosen_img, radius, current_solution_rf, choosen_coords,
                 choosen_names, smol_font, current_len_rf, 'Random Find')
    draw_on_surf(screen, surf_x, choosen_img, radius, current_solution_x, choosen_coords, choosen_names, smol_font,
                 current_len_x, 'X')

    # Random Find
    new_solution_rf = random_generated_solution_rf(current_solution_rf)
    new_len_rf = evaluate(choosenDict, new_solution_rf)
    if current_len_rf > new_len_rf:
        current_len_rf = new_len_rf
        current_solution_rf = new_solution_rf

    # Annealing Method
    new_solution_am = mutate_solution_am_hc(current_solution_am)
    new_len_am = evaluate(choosenDict, new_solution_am)
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
    new_len_hc = evaluate(choosenDict, new_solution_am)
    if new_len_hc < current_len_hc:
        similar = 0
        current_len_hc = new_len_hc
        current_solution_hc = new_solution_hc

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(500)
