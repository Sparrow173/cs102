import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = []
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        row, col = cell
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbour_row = row + i
                neighbour_col = col + j
                if 0 <= neighbour_row < self.rows and 0 <= neighbour_col < self.cols:
                    neighbours.append(self.curr_generation[neighbour_row][neighbour_col])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = [[0] * self.cols for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                alive_neighbours = sum(
                    self.curr_generation[row + i][col + j]
                    for i in range(-1, 2)
                    for j in range(-1, 2)
                    if (i != 0 or j != 0) and 0 <= row + i < self.rows and 0 <= col + j < self.cols
                )

                if self.curr_generation[row][col] == 1 and (alive_neighbours < 2 or alive_neighbours > 3):
                    new_grid[row][col] = 0
                elif self.curr_generation[row][col] == 0 and alive_neighbours == 3:
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = self.curr_generation[row][col]

        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations is None:
            return False
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        grid = []
        with open(filename) as file:
            for line in file:
                row = [int(cell) for cell in line.strip()]
                grid.append(row)
        rows = len(grid)
        cols = len(grid[0])
        game = GameOfLife((rows, cols), randomize=False)
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as file:
            for row in self.curr_generation:
                line = "".join(str(cell) for cell in row)
                file.write(line + "")


if __name__ == "__main__":
    random.seed(1234)
    life = GameOfLife((5, 5))
    while life.is_changing and not life.is_max_generations_exceeded:
        life.step()
    print(life.generations)
