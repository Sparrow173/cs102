"""лабиринт"""
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    """ставим ■ вместо стен"""
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    x_point, y_point = coord
    direction = choice([[1, 0], [0, 1]])

    if 0 < x_point - 2 * direction[0] < len(grid) - 1 and 0 < y_point + 2 * direction[1] < len(grid) - 1:
        grid[x_point - direction[0]][y_point + direction[1]] = " "
    else:
        direction[0], direction[1] = direction[1], direction[0]
        if 0 < x_point - 2 * direction[0] < len(grid) - 1 and 0 < y_point + 2 * direction[1] < len(grid) - 1:
            grid[x_point - direction[0]][y_point + direction[1]] = " "
    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    for cell in empty_cells:
        x, y = cell
        remove_wall(grid, (x, y))

    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"
    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """
    exits = []

    for index, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "X":
                exits.append((index, j))

    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == k:
                if i < len(grid) - 1 and grid[i + 1][j] == 0:
                    grid[i + 1][j] = k + 1
                if i > 0 and grid[i - 1][j] == 0:
                    grid[i - 1][j] = k + 1
                if j < len(row) - 1 and grid[i][j + 1] == 0:
                    grid[i][j + 1] = k + 1
                if j > 0 and grid[i][j - 1] == 0:
                    grid[i][j - 1] = k + 1
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    i: tuple[int, int] = exit_coord
    k = int(grid[i[0]][i[1]])
    path = [i]
    while k != 0:
        if i[0] < len(grid) - 1 and grid[i[0] + 1][i[1]] == k - 1:
            i = (i[0] + 1, i[1])
            path.append(i)
        elif i[1] < len(grid) - 1 and grid[i[0]][i[1] + 1] == k - 1:
            i = (i[0], i[1] + 1)
            path.append(i)
        elif i[0] > 0 and grid[i[0] - 1][i[1]] == k - 1:
            i = (i[0] - 1, i[1])
            path.append(i)
        elif i[1] > 0 and grid[i[0]][i[1] - 1] == k - 1:
            i = (i[0], i[1] - 1)
            path.append(i)
        if type(k) is int:
            k -= 1
    for a, grid_a in enumerate(grid):
        for b, grid_b in enumerate(grid_a):
            if (a, b) not in path and grid_b != "■":
                grid[a][b] = " "
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    exit_x, exit_y = coord
    if exit_x == 0:
        if exit_y == 0 or exit_y == len(grid) - 1 or grid[exit_x + 1][exit_y] == "■":
            return True
    if exit_y == 0:
        if exit_x == 0 or exit_x == len(grid) - 1 or grid[exit_x][exit_y + 1] == "■":
            return True
    if exit_x == len(grid) - 1:
        if exit_y == 0 or exit_y == len(grid) - 1 or grid[exit_x - 1][exit_y] == "■":
            return True
    if exit_y == len(grid) - 1:
        if exit_x == 0 or exit_x == len(grid) - 1 or grid[exit_x][exit_y - 1] == "■":
            return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
    if len(get_exits(grid)) == 1:
        exit_coordinations: list[tuple[int, int]] = get_exits(grid)
        return grid, exit_coordinations
    exits: list[tuple[int, int]] = get_exits(grid)
    exit1, exit2 = exits[0], exits[1]

    if encircled_exit(grid, exit1) or encircled_exit(grid, exit2):
        return grid, None
    grid[exit1[0]][exit1[1]] = 1
    for i, grid_i in enumerate(grid):
        for j, grid_j in enumerate(grid_i):
            if grid_j == " ":
                grid[i][j] = 0
    grid[exit2[0]][exit2[1]] = 0
    k = 0
    while grid[exit2[0]][exit2[1]] == 0:
        k += 1
        make_step(grid, k)
    return grid, shortest_path(grid, exit2)


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
