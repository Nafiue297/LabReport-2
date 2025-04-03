class IDDFS:
    def __init__(self):
        self.maxD = 0
        self.found = False
        self.path = []

    def search(self, maze, start, goal):
        maxD = len(maze) * len(maze[0])
        while self.maxD <= maxD:
            self.path = []
            if self.dls(maze, start, goal, 0, set()):
                print(f"Path found at depth {self.maxD} using IDDFS")
                print("Traversal Order:", self.path)
                return
            self.maxD += 1
        print(f"Path not found at max depth {self.maxD} using IDDFS")

    def dls(self, maze, cur, goal, depth, vis):
        if depth > self.maxD or cur in vis:
            return False

        vis.add(cur)
        self.path.append(cur)

        if cur == goal:
            self.found = True
            return True

        x, y = cur
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                if self.dls(maze, (nx, ny), goal, depth + 1, vis):
                    return True
        
        vis.remove(cur)
        self.path.pop()
        return False

if __name__ == "__main__":
    r, c = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(r)]
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    iddfs = IDDFS()
    iddfs.search(maze, (sx, sy), (tx, ty))
