import pygame

from pivot import Pivot

class Pivots:
    def __init__(self, path) -> None:
        self.pivots = []

        self.pivot_image = pygame.image.load(path)
        self.pivot_image = pygame.transform.smoothscale(
            self.pivot_image, 
            (30, 30)
        )

    def __repr__(self) -> str:
        return str(self.pivots)

    def __getitem__(self, index):
        return self.pivots[index]

    def __len__(self):
        return len(self.pivots)

    def add(self, x, y):
        self.pivots.append(Pivot(x, y, self.pivot_image))

    def draw(self, surface):
        for pivot in self.pivots:
            pivot.draw(surface)

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            (x, y) = pygame.mouse.get_pos()

            self.add(x, y)
