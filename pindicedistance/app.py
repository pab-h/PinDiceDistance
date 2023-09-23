import pygame
import random
import json

from pivots import Pivots

class App:
    instance = None

    def __init__(self, config) -> None:
        if App.instance:
            raise PermissionError()

        pygame.init()

        self.pivots = Pivots(config.get("pivot"))

        self.last_pivot = None
        self.last_dot = None

        dot_config = config.get("dot")

        self.dot_size = dot_config.get("size")
        self.dot_colors = dot_config.get("colors")

        self.factor = config.get("factor")

        self.auto = False

        self.display = pygame.display.set_mode(config.get("display"))

        self.clock = pygame.time.Clock()
        self.fps = config.get("fps")

        self.runnig = False

    @classmethod
    def load_config(cls, path):
        if not cls.instance:
            with open(path) as file:
                config = json.load(file)

                return cls(config)

        return cls.instance

    def draw_dot(self):
        if len(self.pivots) == 0:
            return 
        
        if not self.last_pivot:
            self.last_pivot = self.pivots[0]

        if not self.last_dot:
            self.last_dot = (self.last_pivot.x, self.last_pivot.y)

        pivots_choosable = [ p for p in self.pivots if p != self.last_pivot ]

        choiced_pivot = random.choice(pivots_choosable)

        dx = self.factor * (choiced_pivot.x - self.last_dot[0]) 
        dy = self.factor * (choiced_pivot.y - self.last_dot[1])

        dot_position = (
            self.last_dot[0] + dx, 
            self.last_dot[1] + dy
        )

        pygame.draw.circle(
            self.display, 
            random.choice(self.dot_colors), 
            dot_position,
            self.dot_size
        )

        self.last_pivot = choiced_pivot
        self.last_dot = dot_position

    def run(self):
        self.runnig = True 

        while self.runnig:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runnig = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pivots.update()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.draw_dot()

                    if event.key == pygame.K_a:
                        self.auto = True 

                    if event.key == pygame.K_s:
                        self.auto = False

            self.pivots.draw(self.display)

            if self.auto:
                self.draw_dot()

            pygame.display.update()

            self.clock.tick(self.fps)

    def __del__(self):
        pygame.quit()