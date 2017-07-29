# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player
    x_dir, y_dir = direction

    if (x + x_dir) > 9 or (x + x_dir) < 0:
        hp -= 5
    elif (y + y_dir) > 9 or (y + y_dir) < 0:
        hp -= 5
    else:
        x += x_dir
        y += y_dir
    return x, y, hp


move((0, 9, 5), (0, 1))

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
         )

for tile in TILES:
    if tile == '||':
        tile = ""
        line_end = "\n"
    else:
        line_end = ""
    print(tile, end=line_end)
