def txt_to_input(file_path):
    with open(file_path, "r") as file:
        return [line.replace("\n", "") for line in file]
    
def path_search(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_index = 0  # Start facing up
    rows = len(grid)
    cols = len(grid[0])
    # Find the initial position of the guard
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                x, y = i, j
                break
    
    visited = set()
    visited.add((x, y))
    while 0 <= x < rows and 0 <= y < cols:
        
        next_x, next_y = x + directions[direction_index][0], y + directions[direction_index][1]

        if 0 <= next_x < rows and 0 <= next_y < cols and (grid[next_x][next_y] == "." or grid[next_x][next_y] == "^"):
            x, y = next_x, next_y      
            visited.add((x, y))  
        elif not (0 <= next_x < rows and 0 <= next_y < cols):            
            break
        else:
            direction_index = (direction_index + 1) % 4

    return len(visited)

def path_is_loop(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_index = 0  # Start facing up
    rows = len(grid)
    cols = len(grid[0])
    # Find the initial position of the guard
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                x, y = i, j
                break
    
    visited = set()
    visited.add((x, y, direction_index))
    while 0 <= x < rows and 0 <= y < cols:
        
        next_x, next_y = x + directions[direction_index][0], y + directions[direction_index][1]

        if 0 <= next_x < rows and 0 <= next_y < cols and (grid[next_x][next_y] == "." or grid[next_x][next_y] == "^"):
            x, y = next_x, next_y      
            if (x, y, direction_index) in visited:
                return True                
            visited.add((x, y, direction_index)) 
        elif not (0 <= next_x < rows and 0 <= next_y < cols):            
            break
        else:
            direction_index = (direction_index + 1) % 4

    return False

def find_loop(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows = len(grid)
    cols = len(grid[0])
    # Find the initial position of the guard
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_x, start_y = i, j
                break

    loop_pos = set()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and (i, j) != (start_x, start_y):
                grid[i] = grid[i][:j] + "#" + grid[i][j+1:]

                is_loop = path_is_loop(grid)

                if is_loop:
                    loop_pos.add((i, j))

                grid[i] = grid[i][:j] + "." + grid[i][j+1:]

    return loop_pos

def main():
    input = txt_to_input("input.txt")
    result = find_loop(input)
    print(len(result))


if __name__ == '__main__':
    main()