offsets = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}

def read_maze(fileName):
    try:
        with open(fileName) as file:
            maze = [[char for char in fLine.strip("\n") ] for fLine in file]
            numOfColumnTopRow = len(maze[0])
            for row in maze:
                if len(row) != numOfColumnTopRow:
                    print("Maze is not a square")
                    raise SystemExit
            return maze

    except OSError:
        print("Couldn't not open the file. ")
        raise SystemExit

def is_legal_pos(maze, pos):
    i, j, = pos     #tuple unpacking
    numOfRows = len(maze)
    numOfColumns = len(maze[0])

    return 0 <= i < numOfRows and 0 <= j < numOfColumns and maze[i][j] != '*'

def get_path(predecessors, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()

    return path

if __name__ == '__main__':
    maze = read_maze('mazes/exercise_maze.txt')
    for row in maze:
        print(row)


    maze = read_maze('mazes/mini_maze_bfs.txt')
    for row in maze:
        print(row)


