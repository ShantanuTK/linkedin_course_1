# read maze file challenge_maze.txt

offset = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (-1, 0)
}

def read_maze(path):
    try:
        with open(path) as file:
            maze = [[char for char in fLine.strip('\n')] for fLine in file]
            numOfcolumnsTopRow = len(maze[0])
            for row in maze:
                if len(row) != numOfcolumnsTopRow:
                    print("Maze is not rectangular.")
                    raise SystemExit
            
            return maze
    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit

def is_legal_pos(maze, pos):
    i, j = pos

    numOfRow = len(maze)
    numOfColumn = len(maze[0])

    return 0 <= i < numOfRow and 0 <= j < numOfColumn and maze[i][j] != '*'

def get_path(predecessor, start, goal):
    current_pos = goal
    path = []
    path.append(goal)

    while current_pos != start:
        path.append(predecessor[current_pos])
        current_pos = predecessor[current_pos]
    path.append(start)
    path.reverse()

    return path


if __name__ == '__main__':
    maze = read_maze('mazes/challenge_maze.txt')
    for row in maze:
        print(row)