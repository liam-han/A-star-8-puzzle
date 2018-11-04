import copy

""" class to create new node
    holds essential variables
"""


class Node():
    def __init__(self):
        self.goal_cost = 0
        self.distance = 0
        self.total = 0
        self.initial_state = []
        self.new_state = []
        self.goal_state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
        self.size = (3, 3)  # default 8 puzzle ( 3 x 3 )
        self.index = (0, 0)
        self.missing = 0


""" switch options"""


def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    # return switcher.get(puzzle_choice)


# ZZZZZZtest = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])


num = [[1, 2, 3], [4, 8, 6], [7, 'b', 9]]
num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

""" Takes user input to fill n puzzle initial state by rows"""


def user_input(rows):
    temp = []
    counter = 0
    while (1):
        line = input()
        gg = len(line) - line.count(' ')
        # print(gg)
        if gg != rows:
            print("Try again: Enter " + str(rows) + " values: ")
            continue
        else:
            temp.append(line)
            counter += 1
            if counter >= rows:
                break
    initial_state = split_array(temp, rows)

    return initial_state


# for x in range(m*n):


""" splits array to handle user input with whitespaces """


def split_array(temp, rows):
    temp2 = []
    for x in range(rows):
        split_val = temp[x].split()
        # print(temp[x])
        temp2.append(split_val)
    return temp2


""" turns matrix into 2D array """


def convert_matrix_2d(temp2, rows, col):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(col):
            matrix[i].append(temp2[i][j])
    print("ASDLKFJALSKDFJAKLS;DFJ")
    print(matrix)


# g = np.matrix(matrix)
# g.T[2,1], g.T[2,0] = g.T[2,0], g.T[2,1]


# PRINTS M X N MATRIX
""" Takes 2D ARRAY and prints matrix"""


def print_matrix(node):
    rows = node.size[0]
    col = node.size[1]

    for x in range(rows):
        for y in range(col):
            if node.initial_state[x][y] == '0' or node.initial_state[x][y] == 0:
                print('b', end=' ')
            else:
                print(node.initial_state[x][y], end=' ')
        print("\n", end='')

    print("\n", end='')


# print_matrix(matrix, m, n)


""" Counting missing tiles
    Have to convert 2d array to 1d and find # of missing tiles using counter 
"""

"""
def misplaced_tiles(Node, m, n):
    matrix2 = str_to_int(Node, m, n)

    misplaced = 0
    for tile in matrix2:
        index = matrix2.index(tile)
        if tile == 0:
            continue
        else:
            if tile != index + 1:
                misplaced += 1
        # index_array.append(index)
    return misplaced
"""


def misplaced_tiles(Node):
    initial = Node.initial_state
    goal = Node.goal_state
    counter = 0
    row = Node.size[0]
    col = Node.size[1]
    for x in range(row):
        for y in range(col):
            if goal[x][y] != initial[x][y]:
                counter += 1
    return counter


def str_to_int(matrix, m, n):
    matrix2 = []
    for i in range(m):
        for j in range(n):
            matrix2.append(int(matrix[i][j]))
    print("matrix 2")
    print(matrix2)
    return matrix2


""" Finds the index of a given value in a 2D array puzzle"""


def find_index(value, node):
    value = str(value)
    row = node.size[0]
    col = node.size[1]
    for x in range(row):
        for y in range(col):
            if node.initial_state[x][y] == value:
                # print([x, y])
                return [x, y]


def is_legal(node):
    """ if node.index[0] > node.size[0] or node.index[0] < 0:
        return False
    if node.index[1] > node.size[1] or node.index[1] < 0:
        return False
    else:
        return True
    """

    index = node.index


def move_up(node):
    x = node.index[0]
    y = node.index[1]
    node.new_state = copy.deepcopy(node.initial_state)
    new_state = node.new_state
    if x > 0:
        new_state[x][y], new_state[x - 1][y] = new_state[x - 1][y], new_state[x][y]
    else:
        raise IndexError
    # sample [2,2] to [1,2]


def move_down(node):
    x = node.index[0]
    y = node.index[1]
    node.new_state = copy.deepcopy(node.initial_state)
    new_state = node.new_state
    new_state[x][y], new_state[x + 1][y] = new_state[x + 1][y], new_state[x][y]
    # sample [1,2] to [2,2]


def move_left(node):
    x = node.index[0]
    y = node.index[1]
    new_state = node.initial_state
    if y > 0:
        new_state[x][y], new_state[x][y - 1] = new_state[x][y - 1], new_state[x][y]
    else:
        raise IndexError
    # sample [1,2] to [1,1]


def move_right(node):
    x = node.index[0]
    y = node.index[1]
    new_state = node.initial_state
    # new_state = copy.deepcopy(old_state)

    new_state[x][y], new_state[x][y + 1] = new_state[x][y + 1], new_state[x][y]
    # node.new_state = new_state
    # sample [1,1] to [1,2]


# def general_search(problem, QUEUEING_FUNCTION):


def main():

    print("Welcome to Bertie Woosters 8-puzzle solver. \n")
    print("Enter the rows with spaces or tabs and press enter")
    """
    # node1 = Node()
    # initial_state = user_input(node1.size[0])
    # node1.initial_state = initial_state
    # h = misplaced_tiles(node1)
    # moves = [move_left(node1), move_right(node1), move_down(node1), move_up(node1)]
    list = {}
    # while h > 0
    # for move in moves:
    
    try:
        print(node1.initial_state)
        move_down(node1)
        print_matrix(node1)
        #k = misplaced_tiles(node1)
        #list.update({node1: 1})
    except IndexError:
        pass
    """

    list = {}
    node = Node()
    node.initial_state = user_input(3)
    node.index = find_index(0, node)
    for move in (move_up(node), move_down(node)):
        print(node.index)
        try:
            move
            print(node.new_state)
            counter +=1
        except IndexError:
            pass


    print_matrix(node)
        # continue
    # print(list.items())
    """
    for x in range(2):
        node = Node()
        node.initial_state = user_input(node.size[0])
        list.append(node)
    print(list[0].initial_state)
    print(list[1].initial_state)
    # print_matrix(n_node)
    print_matrix(n_node)
    # n_node.distance = h
    """
    # list.append(n_node)
    # print(list[0].distance)
    # print_matrix(goal_state, m, n)
    # val_index = find_index(0, puzzle)
    # move_right(puzzle, val_index)
    # print_matrix(puzzle, m, n)


if __name__ == '__main__':
    main()
