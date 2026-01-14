import pygame
from .ui import Button, FONT


class FloatScore(pygame.sprite.Sprite):
    """Floaty bois when you clicky da buttons"""

    def __init__(self, text: str, pos: tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = FONT.render(text, True, "white")
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.y -= 4
        self.image.set_alpha(self.image.get_alpha() - 7)
        if self.image.get_alpha() <= 0:
            self.kill()


class ButtonCollider(pygame.sprite.Sprite):
    """Helper class that is intended to be temporarily created
    at the position the mouse was clicked. The collision area
    is a 1x1 rect to the as precise a collision detection as possible"""

    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((1, 1))
        self.rect = pygame.Rect(pos, (1, 1))


def check_click_collision(buttons: pygame.sprite.Group, event: pygame.Event):
    """Should only return a single button as a match for collision.
    Access the lone item with [0] or next()"""
    click_pos = ButtonCollider(event.pos)
    collisions: list[Button] = pygame.sprite.spritecollide(
        click_pos,
        buttons,
        False,
    )
    return collisions
