import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.addstr(0, 0, "-" * (self.life.cols + 2))
        for row in range(self.life.rows):
            screen.addch(row + 1, 0, "|")
            screen.addstr(row + 1, self.life.cols + 1, "|")
        screen.addstr(self.life.rows + 1, 0, "-" * (self.life.cols + 2))

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                if self.life.curr_generation[row][col] == 1:
                    screen.addch(row + 1, col + 1, "*")

    def run(self) -> None:
        try:
            screen = curses.initscr()
            curses.curs_set(0)
            screen.clear()

            while True:
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()
                self.life.step()
                curses.napms(500)
        except KeyboardInterrupt:
            pass
        finally:
            curses.endwin()


if __name__ == "__main__":
    life = GameOfLife((80, 40), max_generations=50)
    ui = Console(life)
    ui.run()
    print(life.generations)
