import pygame

pygame.font.init()

COLORS = ["red", "blue", "green", "black", "purple", "grey", "cyan"]
BUTTON_SIZE = (130, 50)
FONT = pygame.font.SysFont("caskaydiacovenerdfontmono", 20, bold=True)
MATERIALS = {
    "Bronze": "brown",
    "Iron": "darkgrey",
    "Silver": "lightgrey",
    "Gold": "gold",
    "Mithril": "purple",
    "Dragonite": "blue",
}
TOTAL_BUTTONS = len(MATERIALS)


def calculate_y(surface: pygame.Surface, i: int):
    """The math used to calculate how to evenly space y
    position based on height of the surface provided
    """
    total_button_height = BUTTON_SIZE[1] * TOTAL_BUTTONS
    available_space = surface.height - total_button_height
    gap_space = available_space // (TOTAL_BUTTONS + 1)
    return i * (BUTTON_SIZE[1] + gap_space) + gap_space


def generate_coords(surface: pygame.Surface, x_offset: int = 200):
    """Given a number of buttons and their sizes, generate a list
    of coordinates that will evenly distribute them vertically
    """

    x = surface.width - x_offset
    return [(x, calculate_y(surface, i)) for i in range(TOTAL_BUTTONS)]


class Button(pygame.sprite.Sprite):
    def __init__(
        self,
        screen: pygame.Surface,
        material: str,
        pos: tuple[int, int],
        size: tuple[int, int],
    ):
        super().__init__()
        self.screen = screen
        self.material = material
        self.color = MATERIALS[self.material]
        self.pos = pos
        self.rect: pygame.Rect = pygame.Rect(self.pos, BUTTON_SIZE)
        self.trans_surf = pygame.Surface(BUTTON_SIZE, pygame.SRCALPHA)
        self.enabled = True
        self.trans_surf.set_alpha(255)

    def toggle_button(self):
        if self.enabled:
            self.enabled = False
            self.trans_surf.set_alpha(100)
        else:
            self.enabled = True
            self.trans_surf.set_alpha(255)

    def update(self):
        pygame.draw.rect(
            self.trans_surf,
            self.color,
            self.trans_surf.get_rect(),
            border_radius=10,
        )
        pygame.draw.rect(
            self.trans_surf,
            "black",
            self.trans_surf.get_rect(),
            border_radius=10,
            width=5,
        )
        text_surface = FONT.render(self.material, antialias=True, color="black")
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(self.trans_surf, self.pos)
        self.screen.blit(text_surface, text_rect)
