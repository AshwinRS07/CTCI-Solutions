# Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.

# Colors are just ints
# Screen is an int matrix
# x,y is the point

def paint_fill(screen, x, y, color):
    def helper(screen, x,y, og_color, new_color):
        screen[x][y] = new_color
        if x-1 >= 0 and screen[x-1][y] == og_color:
            helper(screen, x-1, y, og_color, new_color)
        if y-1 >= 0 and screen[x][y-1] == og_color:
            helper(screen, x, y-1, og_color, new_color)
        if x+1 >= 0 and screen[x+1][y] == og_color:
            helper(screen, x+1, y, og_color, new_color)
        if y+1 >= 0 and screen[x][y+1] == og_color:
            helper(screen, x, y+1, og_color, new_color)
        return screen
    if screen[x][y] == color:
        return screen
    return helper(screen, x, y, screen[x][y], color)


tests = [
        [[1,1,1,2,2],
        [1,1,2,2,3],
        [1,2,2,3,3],
        [2,2,3,3,4]],
        [[1,2,3],
        [1,2,3],
        [2,2,3]]
]

for test in tests:
    print(paint_fill(test,0,0,3))