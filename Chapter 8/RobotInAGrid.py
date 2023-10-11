# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

# We use -1 as off limits cells.

def robot_in_a_grid(grid):
    rows,cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = 1
    for r in range(rows):
        for c in range(cols):
            if r-1 >= 0 and grid[r-1][c] != -1:
                print("row",r,c, dp[r-1][c])
                dp[r][c] += dp[r-1][c]
            if c-1 >= 0 and grid[r][c-1] != -1:
                print("col",r,c, dp[r][c-1])
                dp[r][c] += dp[r][c-1]
        print(dp)
    return dp[-1][-1]


test = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

print(robot_in_a_grid(test))