"""
CS5001/3 Final Project Part1
Mozhi Shen
5-2-2022

This is the first version of 2048 game.
"""
import random
import copy


def get_size():
    """get the size of the matrix, defensively get an int between
        3 and 6."""
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
# get_size()


def game_init(size):
    """Return a nested list n*n with value 0 and size n"""
    return [[0] * size for i in range(size)]
# game_init(4)


def print_matrix(g_matrix):
    """print the matrix, as the main interaction part of the game"""
    size = len(g_matrix)
    for i in range(size):
        for j in range(size):
            print(f"{g_matrix[i][j]:4d}", end="")
        print("")
        print("")


def end_game(g_matrix):
    """if game is ended, return True, else return False"""
    size = len(g_matrix)
    for i in range(size):
        for j in range(size):
            if g_matrix[i][j] == 0:
                return False
    return True


def random_generate(g_matrix):
    """locate all 0 elements and make one of them random 2 or 4"""
    size = len(g_matrix)
    empty_list = []

    for i in range(size):
        for j in range(size):
            if g_matrix[i][j] == 0:
                empty_list.append([i, j])
    if not empty_list:
        return g_matrix
    else:
        # print(empty_list)
        a = random.choice(empty_list)
        # print(a)
        # print(a[0],a[1])
        # print(g_matrix[a[0]][a[1]])
        g_matrix[a[0]][a[1]] = random.choices([2, 4], weights=(30, 10), k=1)[0]
        # print_matrix(g_matrix)
        return g_matrix


def get_line(line_lst):
    """get one line of the matrix, return the line when left-key is pushed."""
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
# print(get_line([2,2,0,0,2,2]))
# print(get_line([4,2,0,2,2]))
# print(get_line([1,1,1]))


def left(g_matrix):
    """return a modified matrix, as left_move was chosen """
    size = len(g_matrix)
    for i in range(size):
        # print(i)
        g_matrix[i] = get_line(g_matrix[i])
    return g_matrix


def right(g_matrix):
    """return a modified matrix, as right_move was chosen """
    size = len(g_matrix)
    for i in range(size):
        # print(i)
        g_matrix[i][::-1] = get_line(g_matrix[i][::-1])
    return g_matrix


def covert(g_matrix):
    """Do the transpose of a n*n matrix, return a matrix"""
    size = len(g_matrix)
    covert_matrix = game_init(size)
    for i in range(size):
        for j in range(size):
            covert_matrix[i][j] = g_matrix[j][i]
    g_matrix = covert_matrix
    return g_matrix


def down(g_matrix):
    """return a modified matrix, as down_move was chosen """
    c_matrix = covert(g_matrix)
    right(c_matrix)
    c_matrix = covert(c_matrix)
    return c_matrix


def up(g_matrix):
    """return a modified matrix, as up_move was chosen """
    c_matrix = covert(g_matrix)
    left(c_matrix)
    c_matrix = covert(c_matrix)
    return c_matrix


def main():
    size = get_size()
    game_matrix = game_init(size)
    game_matrix = random_generate(game_matrix)
    print("Use up/down/left/right to move the numbers, same number"
          " merge into one when they touch. Add them up to reach 2048!")
    print("")
    while not end_game(game_matrix):
        print_matrix(game_matrix)
        user = input(
            "input 'U' for move up, 'D' for move down, 'L' for move left, " +
            "'R' for move right and 'E' for exit: ")

        hold_matrix = copy.deepcopy(game_matrix)

        if user == "u" or user == "U":
            game_matrix = up(game_matrix)
        elif user == "d" or user == "D":
            game_matrix = down(game_matrix)

        elif user == "l" or user == "L":
            game_matrix = left(game_matrix)

        elif user == "r" or user == "R":
            game_matrix = right(game_matrix)
        elif user == "e" or user == "E":
            break
        else:
            print("unknown input is ignored, please try again")
        if hold_matrix != game_matrix:
            game_matrix = random_generate(game_matrix)

    print("Game over")
    score = sum(sum(x) for x in game_matrix)
    print(f"your score is: {score}")
    input(f"hit any key to close")


# aa = [[1, 1, 1], [0, 3, 4], [1, 0, 0]]
# print_matrix(aa)

if __name__ == '__main__':
    main()
