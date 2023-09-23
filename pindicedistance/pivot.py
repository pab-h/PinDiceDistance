class Pivot:
    def __init__(self, x, y, image) -> None:
        self.x = x
        self.y = y
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, surface):
        surface.blit(
            self.image, 
            (
                self.x - self.width / 2, 
                self.y - self.height
            )
        )