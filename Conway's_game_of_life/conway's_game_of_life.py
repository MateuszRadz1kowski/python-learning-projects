import random
import time


def game_loop():
    alive_sign = "🟩"
    dead_sign = "🟥"
    grid_cols = 10
    grid_rows = 10
    grid = []

    create_grid(grid,grid_rows,grid_cols,dead_sign)
    randomize_starting_cells(grid,alive_sign)
    for i in range(1000000):
        check_cell_requirements(grid,alive_sign,dead_sign)
        time.sleep(1)
        print_grid(grid)
        print("\n")

def create_grid(grid,grid_rows,grid_cols,dead_sign):
    for i in range(grid_rows):
        temp_grid_row = []
        for j in range(grid_cols):
            temp_grid_row.append(dead_sign)
        grid.append(temp_grid_row)


def randomize_starting_cells(grid,alive_sign):
    for x,row in enumerate(grid):
        for y,cell in enumerate(row):
            populate_random = random.randint(0, 5)
            if populate_random == 0:
                grid[x][y] = alive_sign

def print_grid(grid):
    for i in range(len(grid)):
        print(" ".join(grid[i]))

def check_cell_requirements(grid,alive_sign,dead_sign):
    grid_copy = [row[:] for row in grid]
    for x,row in enumerate(grid_copy):
        for y,cell in enumerate(row):
            cells_alive = 0

            try:
                if grid_copy[x - 1][y - 1] == alive_sign:
                    cells_alive += 1
            except IndexError:
                pass

            try:
                if grid_copy[x - 1][y] == alive_sign:
                    cells_alive += 1
            except IndexError:
                pass

            try:
                if grid_copy[x - 1][y + 1] == alive_sign:
                    cells_alive += 1
            except IndexError:
                pass

            try:
                if grid_copy[x][y - 1] == alive_sign:
                    cells_alive += 1
            except IndexError:
                pass

            try:
                if grid_copy[x][y + 1] == alive_sign:
                    cells_alive += 1
            except IndexError:
                pass

            try:
                if grid_copy[x + 1][y - 1] == alive_sign:
                    cells_alive += 1
            except IndexError:
                pass

            try:
                if grid_copy[x + 1][y] == alive_sign:
                    cells_alive += 1
            except IndexError:
                pass

            try:
                if grid_copy[x + 1][y + 1] == alive_sign:
                    cells_alive += 1
            except IndexError:
                pass

            if grid_copy[x][y] == alive_sign and cells_alive < 2:
                grid_copy[x][y] = dead_sign
            elif grid_copy[x][y] == alive_sign and (cells_alive == 2 or cells_alive == 3):
                grid_copy[x][y] = alive_sign
            elif grid_copy[x][y] == alive_sign and cells_alive > 3:
                grid_copy[x][y] = dead_sign
            elif grid_copy[x][y] == dead_sign and cells_alive == 3:
                grid_copy[x][y] = alive_sign

    for i in range(len(grid)):
        grid[i] = grid_copy[i][:]


game_loop()