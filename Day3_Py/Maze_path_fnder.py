def is_path_possible(maze) :
    rows = len(maze)
    cols = len(maze[0])
    
    if(maze[0][0]==1 or maze[rows-1][cols-1] ==1):
        return False
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = [(0,0)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True
    
    while queue:
        x,y = queue.pop(0)
        
        if x== rows -1 and y == cols-1:
            return True
        
        for dx, dy in directions:
            nx = x+dx
            ny = y+dy
            
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and not visited[nx][ny]:
            queue.append(nx,ny)
            visited[nx][ny] = True
            
    return False
def shortest_path_length(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    if(maze[0][0]==1 or maze[rows-1][cols-1] ==1):
        return False
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = [(0,0,0)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True
    
    while queue:
        x,y, steps = queue.pop(0)
        
        if x== rows -1 and y == cols-1:
            return steps
        
        for dx, dy in directions:
            nx = x+dx
            ny = y+dy
            
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx,ny, steps+1))
                visited[nx][ny] = True
    return False
        

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

print("Is there a valid path?")
print(is_path_possible(maze))

print("Length of the shortest path:")
print(shortest_path_length(maze))