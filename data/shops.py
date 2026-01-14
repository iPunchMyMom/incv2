import pygame
from .ui import FONT


class ShopButton(pygame.sprite.Sprite):
    def __init__(
        self,
        screen: pygame.Surface,
        text: str,
        color: str,
        pos: tuple[int, int],
        size: tuple[int, int],
    ):
        super().__init__()
        self.screen = screen
        self.text = text
        self.size = size
        self.color = color
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = FONT.render(self.text, True, "black")

    def update(self):
        pygame.draw.rect(self.screen, "red", self.rect, border_radius=10)
        self.screen.blit(self.image, self.image.get_rect(center=self.rect.center))
