
from helper import offsets, get_path, read_maze, is_legal_pos
from que import Que

def bfs(maze, start, goal):
    que = Que()
    que.enque(start)
    predecessor = {start: None}

    while not que.is_empty():
        currentPoint = que.deque()
        if currentPoint == goal:
            return get_path(predecessor, start, goal)
        for direction in ['up', 'right', 'down', 'left']:
            rowOffset, columnOffset = offsets[direction]
            neighbour = (currentPoint[0] + rowOffset, currentPoint[1] + columnOffset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessor:
                que.enque(neighbour)
                predecessor[neighbour] = currentPoint

    return None
    pass



if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    print("Done with test 1")

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    print(result)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
    print("Done with test 2")

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    # print(result)
    assert result is None
    print("Done with test 3")

    #test 4
    maze = read_maze("mazes/exercise_maze.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    print("Exercis result: " +str(result))
    print("Done with test 4")