from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def print_grid(grid):
    for row in grid:
        for item in row:
            print(f"{str(item):2}", end=" ")
        print()

    print("======")


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    x_point, y_point = coord
    grid[x_point][y_point] = " "
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

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки
    if not random_exit:
        input_x_in = int(input("Введите координату x для входа: "))
        input_y_in = int(input("Введите координату y для входа: "))
        input_x_out = int(input("Введите координату x для выхода: "))
        input_y_out = int(input("Введите координату y для выхода: "))
    else:
        input_x_in = randint(1, rows - 2)
        input_y_in = 0
        input_x_out = randint(1, rows - 2)
        input_y_out = cols - 1

    for cell in empty_cells:
        x, y = cell
        directions = []
        if x > 1:
            directions.append((-2, 0))
        if y > 1:
            directions.append((0, -2))

        if not directions:
            continue

        dx, dy = choice(directions)
        grid[x + dx // 2][y + dy // 2] = " "

    grid[input_x_in][input_y_in] = "X"
    grid[input_x_out][input_y_out] = "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """
    exits = []

    for index, row in enumerate(grid):
        if row[0] == "X":
            exits.append((index, 0))
        if row[-1] == "X":
            exits.append((index, len(grid[0]) - 1))

    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """

    moved = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == k:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = row + dx, col + dy
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = k + 1
                        moved = True
    if not moved:
        print("Лабиринт непроходим")
        exit()
    print_grid(grid)
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    path = []
    i, j = exit_coord
    k = grid[i][j]
    path.append(exit_coord)

    while grid[i][j] != 1:
        if i > 0 and grid[i - 1][j] != "■" and grid[i - 1][j] == k - 1:
            path.append((i - 1, j))
            i -= 1
            k -= 1
        elif j > 0 and grid[i][j - 1] == k - 1:
            path.append((i, j - 1))
            j -= 1
            k -= 1
        elif i < len(grid) - 1 and grid[i + 1][j] == k - 1:
            path.append((i + 1, j))
            i += 1
            k -= 1
        elif j < len(grid[0]) - 1 and grid[i][j + 1] == k - 1:
            path.append((i, j + 1))
            j += 1
            k -= 1

    if len(path) != grid[exit_coord[0]][exit_coord[1]]:
        for i in range(len(path) - 2, -1, -1):
            if grid[path[i][0]][path[i][1]] != "X":
                grid[path[i][0]][path[i][1]] = " "
                new_exit_coord = path[i + 1]
                temp_grid = deepcopy(grid)
                return shortest_path(temp_grid, new_exit_coord)

    return path[::-1]


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """
    i, j = coord
    if grid[i][j] != "X":
        return False

    count = 0
    if i > 0 and grid[i - 1][j] in ["X", " "]:
        count += 1
    if j > 0 and grid[i][j - 1] in ["X", " "]:
        count += 1
    if i < len(grid) - 1 and grid[i + 1][j] in ["X", " "]:
        count += 1
    if j < len(grid[0]) - 1 and grid[i][j + 1] in ["X", " "]:
        count += 1

    if count == 3:
        return True

    if (i == 0 or i == len(grid) - 1) and (j == 0 or j == len(grid[0]) - 1):
        return count == 2

    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
    exit_coordinations = list(get_exits(grid))
    exits = set(exit_coordinations)
    if len(exits) == 1:
        return grid, exit_coordinations

    enter = exit_coordinations[0]
    if encircled_exit(grid, (enter[0], enter[1])):
        return grid, None

    grid[enter[0]][enter[1]] = 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == " " or grid[i][j] == "X":
                grid[i][j] = 0

    k = 0
    x_point, y_point = exit_coordinations[1]
    new_grid = deepcopy(grid)
    while new_grid[x_point][y_point] == 0:
        k += 1
        another_step = make_step(new_grid, k)
        if encircled_exit(another_step, (x_point, y_point)):
            break

    result = shortest_path(new_grid, (x_point, y_point))
    if not result:
        result = [another_step[1], another_step[0]]

    return new_grid, result


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
    GRID = bin_tree_maze(15, 15, False)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
