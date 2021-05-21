from helper import offset, read_maze, get_path, is_legal_pos
from stack import Stack


def dfs(maze, start, goal):
    stack = Stack() # The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
    stack.push(start)

    predecessor = {start: None}

    while not stack.is_empty():
        current = stack.pop()
        # print(current)
        if current == goal:
            return get_path(predecessor, start, goal)
        for direction in ["up", "right", "down", "left"]:
            rowOffset, columnOffset = offset[direction]
            neighbour = (current[0] + rowOffset, current[1] + columnOffset)
            # print(neighbour)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessor: # WHY neighbour not in predecessor NECESSARY?
                stack.push(neighbour)
                predecessor[neighbour] = current
    
    return None

if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    startPos = (0, 0)
    goalPos = (2, 2)
    result = dfs(maze, startPos, goalPos)
    # print(result)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    print("Done with test 1")

    # Test 2
    maze = read_maze("mazes/mini_maze_dfs.txt")
    # for row in maze:
    #     print(row)
    startPos = (0, 0)
    goalPos = (2, 2)
    result = dfs(maze, startPos, goalPos)
    # print(result)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    print("Done with test 2")


    # Test 3
    maze = read_maze("mazes/mini_maze_dfs.txt")
    startPos = (0, 0)
    goalPos = (3, 3)
    result = dfs(maze, startPos, goalPos)
    assert result is None
    print("Done with test 3")