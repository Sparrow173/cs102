import pygame
from life import GameOfLife
from pygame.locals import QUIT
from ui import UI
from typing import List, Tuple


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        # Устанавливаем размер окна
        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.screen_size = self.width, self.height

        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                x = col * self.cell_size
                y = row * self.cell_size
                cell_rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                if self.life.curr_generation[row][col] == 1:
                    pygame.draw.rect(
                        self.screen, pygame.Color('green'), cell_rect)
                else:
                    pygame.draw.rect(
                        self.screen, pygame.Color('white'), cell_rect)

    def mark_cell(self, pos: Tuple[int, int]):
        col = pos[0] // self.cell_size
        row = pos[1] // self.cell_size
        if 0 <= row < self.life.rows and 0 <= col < self.life.cols:
            self.life.curr_generation[row][col] = 1 if self.life.curr_generation[row][col] == 0 else 0

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        # self.screen.fill(pygame.Color("white"))

        running = True
        self.paused = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.mark_cell(pos)

            if not self.paused:
                # Отрисовка списка клеток
                # Выполнение одного шага игры (обновление состояния ячеек)
                print(self.life.curr_generation)
                self.draw_grid()
                self.draw_lines()

                pygame.display.flip()
                clock.tick(self.speed)

                self.life.prev_generation = self.life.curr_generation
                self.life.curr_generation = self.life.get_next_generation()
        pygame.quit()


if __name__ == '__main__':
    life = GameOfLife((5, 5))
    ui = GUI(life, cell_size=40)
    ui.run()
    '''
    while life.is_changing and not life.is_max_generations_exceeded:
        life.step()
    '''
    print(life.generations)
