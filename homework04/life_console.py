import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.addstr(0, 0, "-" * (self.life.width + 2))
        for row in range(self.life.height):
            screen.addch(row + 1, 0, "|")
            screen.addch(row + 1, self.life.width + 1, "|")
        screen.addstr(self.life.height + 1, 0, "-" * (self.life.width + 2))

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for row in range(self.life.height):
            for col in range(self.life.width):
                if self.life.grid[row][col] == 1:
                    screen.addch(row + 1, col + 1, "*")

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)

        try:
            while True:
                self.draw_borders(screen)
                self.draw_grid(screen)
                self.life.step()
        except KeyboardInterrupt:
            pass
        finally:
            curses.endwin()


if __name__ == "__main__":
    life = GameOfLife((5, 5))
    ui = Console(life)
    ui.run()
    """
    while life.is_changing and not life.is_max_generations_exceeded:
        life.step()
    """
    print(life.generations)
