from helper import offsets, get_path, is_legal_pos, read_maze
from priority_que import PriorityQue

def heuristic(current, goal):
    x1, y1 = current
    x2, y2, = goal

    return abs(x2 - x1) + abs(y2 - y1)

def a_star(maze, start, goal):
    pQue = PriorityQue()
    gValues = {start: 0}
    predecessors = {start: None}

    pQue.put(start, 0)       #(start -> (i, j), fValues)

    while not pQue.is_empty():
        current = pQue.get()
        if current == goal:
            return get_path(predecessors, start, goal)
        for direction in ['up', 'right', 'down', 'left']:
            rowOffset, columnOffset = offsets[direction]
            neighbour = (current[0] + rowOffset, current[1] + columnOffset)
            if is_legal_pos(maze, neighbour) and neighbour not in gValues:
                newCost = gValues[current] + 1
                gValues[neighbour] = newCost
                fValues = newCost + heuristic(neighbour, goal)
                pQue.put(neighbour, fValues)
                predecessors[neighbour] = current

    return None

if __name__ == '__main__':
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    print("Done 1")

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
    print("Done 2")

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
    print("Done 3")

    # Exercise
    maze = read_maze("mazes/exercise_maze.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    print(result)
    print("Done 4")

