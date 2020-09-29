import pygame

# Инициализация PyGame и установка дисплея
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Queen Problem Backtracking")


# This class is needed for the cells in which the horses will be located.
class Node(object):
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def draw_node(self, length, width, color):
        pygame.draw.rect(win, color, (self.x, self.y, width, length))


# A function that checks for the validity of all positions of the horses that are at the moment
def check_for_valid(lst_of_pos, current):
    for pos in lst_of_pos:
        if pos[0] == current[0] or pos[1] == current[1] or abs(pos[0] - current[0]) == abs(pos[1] - current[1]):
            return False
    return True


# Main Funct. BackTracking
def solve(board_, lst_of_pos, row):
    if len(lst_of_pos) == len(board_):
        return lst_of_pos
    for column in range(len(board_)):
        if not check_for_valid(lst_of_pos, (row, column)):
            continue
        lst_of_pos.append((row, column))
        ready = solve(board_, lst_of_pos, row + 1)
        if ready:
            return ready
        lst_of_pos.pop()
    return False


# RGB Colors
red_color = (255, 0, 0)
blue_color = (0, 0, 255)
green_color = (0, 255, 0)
white_color = (255, 255, 255)
black_color = (0, 0, 0)
grey_color = (125, 125, 125)
yellow_color = (250, 230, 110)


# Visualization  Part
def draw_screen(field):
    win.fill(red_color)
    for i in range(len(field)):
        for j in range(len(field)):
            new_node = Node((30 + j * 70, 30 + i * 70))
            if field[i][j] == 0:
                color = green_color
            else:
                color = black_color
            new_node.draw_node(45, 45, color)


def main():
    iter = 0  # Not a very important variable. If you change it, the initial position of the first knight will change
    run = True

    while run:
        lst = [(0, iter)]
        board_to_draw = [[0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0]]
        new_solution = solve(board_to_draw, lst, 1)
        for pos in new_solution:
            board_to_draw[pos[0]][pos[1]] = 1

        draw_screen(board_to_draw)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.delay(500)
        pygame.display.update()
        iter += 1
        if iter == 8:
            iter = 0


if __name__ == '__main__':
    main()
