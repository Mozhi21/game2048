"""
CS5001/3 Final Project Part1
Mozhi Shen
5-2-2022

This is the third version of 2048 game.
Constants are stored in G2048_v3_constant.py
"""
import random
import pygame
from pygame.locals import *
from copy import deepcopy
from G2048_v3_constant import *


class Matrix:
    """Hold the matrix with size n * n as the data of the game"""
    def __init__(self, size=4):
        self.size = size
        self.data = [[0] * size for i in range(size)]
        # matrix was stored as a nested list

    def __str__(self):
        return f"{self.data}"

    def add_number(self):
        """add a random number to the self.data. identify all 0 place and
        then randomly choose one and change it to 2 or 4"""
        empty_list = [] # store the places that are empty

        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == 0:
                    empty_list.append([i, j])
        if empty_list:  # if there is no empty place, skip.
            a = random.choice(empty_list)
            self.data[a[0]][a[1]] = \
                random.choices([2, 4], weights=(30, 10), k=1)[0]
        # else:

    def covert(self):
        """return the transpose of the matrix"""
        covert_matrix = [[0] * self.size for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                covert_matrix[i][j] = self.data[j][i]
        self.data = covert_matrix

    def move(self, move):
        """use get_line()to implement the move"""

        if move in "ud":
            self.covert()

        for i in range(self.size):
            if move in "rd":
                self.data[i][::-1] = get_line(self.data[i][::-1])
            else:
                self.data[i] = get_line(self.data[i])

        if move in "ud":
            self.covert()

    def game_over(self):
        """Justify if game is over by trying all possilbe move"""
        save_matrix = deepcopy(self.data)
        cant_move = True
        for i in "lrud":
            self.move(i)
            if self.data != save_matrix:
                cant_move = False
                break
        self.data = save_matrix
        return cant_move

    def get_score(self):
        """add up the score and return"""
        return sum(sum(self.data[i]) for i in range(self.size))


def get_line(line_lst):
    """get a list and return the left-shift of the list"""
    lst0 = [0] * len(line_lst)
    lst1 = [i for i in line_lst if i != 0]
    for i in range(len(lst1) - 1):
        if lst1[i] == lst1[i + 1]:
            lst1[i] *= 2
            lst1[i + 1] = 0
    lst3 = [j for j in lst1 if j != 0]
    for k in range(len(lst3)):
        lst0[k] += lst3[k]
    return lst0


def draw_game(screen, matrix, myfont):
    """draw the game with pygame"""
    screen.fill(color['back'])

    for i in range(size):
        for j in range(size):
            n = matrix[i][j]

            rect_x = j * W // size + SPACING
            rect_y = i * H // size + SPACING + O_height - W
            rect_w = W // size - 2 * SPACING
            rect_h = H // size - 2 * SPACING

            pygame.draw.rect(screen,
                             color[n],
                             pygame.Rect(rect_x, rect_y, rect_w, rect_h),
                             border_radius=7)
            if n != 0:
                text_surface = myfont.render(f'{n}', True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(rect_x + rect_w / 2,
                                                          rect_y + rect_h / 2))
                screen.blit(text_surface, text_rect)


def show_score(screen, score, scorefont):
    """Show score at the center top of the game"""
    text_surface = scorefont.render(f'Score: {score}', True, (10, 10, 10))
    text_rect = text_surface.get_rect(center=(W / 2, 4 * SPACING))
    screen.blit(text_surface, text_rect)


def show_gameover(screen, myfont):
    """Show game over at the center of the game when called"""
    text_surface = myfont.render('Game over', True, (10, 10, 10))
    text_rect = text_surface.get_rect(center=(O_width / 2, O_height / 2))
    screen.blit(text_surface, text_rect)


def wait_for_key():
    """get the key press from keyboard by event in pygame.event.get()"""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 'q'
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    return 'u'
                elif event.key == K_RIGHT:
                    return 'r'
                elif event.key == K_LEFT:
                    return 'l'
                elif event.key == K_DOWN:
                    return 'd'
                elif event.key == K_q or event.key == K_ESCAPE:
                    return 'q'


def get_size():
    """defensively get the size of the game"""
    print("")
    print("{:*^75}".format("  Welcome to game 2048!  "))
    print("")
    print("Please enter the size of the game you want.")
    size = input("It should between 3 to 6, end with Enter: ")
    try:
        while int(size) > 7 or int(size) < 3:
            print("Size too big or too small, please select another size.\n")
            print("Game restart, Please enter the size of the game you want.")
            size = input("It should between 3 to 6, end with Enter: ")
        print(f"Size {size} selected.\n")
        return int(size)
    except Exception:
        print("Error, please use integer as size, game would restart \n")
        return get_size()


def main():
    global size
    size = get_size()

    pygame.init()
    pygame.display.set_caption("2048: Mozhi Shen")
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    scorefont = pygame.font.SysFont('Comic Sans MS', 30)
    overfont = pygame.font.SysFont('Comic Sans MS', 50)
    screen = pygame.display.set_mode((O_width, O_height))

    a = Matrix(size)
    a.add_number()

    running = True
    while running:

        draw_game(screen, a.data, myfont)
        show_score(screen, a.get_score(), scorefont)
        if a.game_over():
            show_gameover(screen, overfont)

        pygame.display.flip()
        key = wait_for_key()
        if key == 'q':
            running = False
        elif not a.game_over():
            save_matrix = deepcopy(a.data)
            a.move(key)
            if save_matrix != a.data:
                a.add_number()


if __name__ == "__main__":
    main()
