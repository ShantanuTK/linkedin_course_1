offsets = {
   "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (-1, 0)
}

def read_maze(fileName):
    try:
        with open(fileName) as file:
            maze = [[char for char in fLine.strip("\n")]for fLine in file]
            numOfColumnsTopRow = len(maze[0])
            for row in maze:
                if len(row) != numOfColumnsTopRow:
                    print("Maze is not a square.")
                    raise SystemExit

            return maze
    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit

def is_legal_pos(maze, pos):
    i, j = pos

    numOfRows = len(maze)
    numOfColumns = len(maze[0])

    return 0 <= i < numOfRows and 0 <= j < numOfColumns and maze[i][j] != '*'

def get_path(predecessor, start, goal):
    path = []
    currentPoint = goal
    path.append(currentPoint)

    while currentPoint != start:
        path.append(predecessor[currentPoint])
        currentPoint = predecessor[currentPoint]
    
    path.append(start)
    path.reverse()

    return path










if __name__ == '__main__':
    maze = read_maze('mazes/challenge_maze.txt')
    for row in maze:
        print(row)
