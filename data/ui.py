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


def _calculate_y(surface: pygame.Surface, i: int):
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
    return [(x, _calculate_y(surface, i)) for i in range(TOTAL_BUTTONS)]


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


class Inventory(pygame.sprite.Sprite):
    def __init__(
        self,
        screen: pygame.Surface,
        color: str,
    ):
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((500, 100))
        self.rect = self.image.get_rect(topleft=(350, 0))
        self.image.fill(color)
        self.stock = {material: 0 for material in MATERIALS}

    def update(self):
        bronze = FONT.render(f"Bronze: {self.stock['Bronze']}", True, "black")
        iron = FONT.render(f"Iron: {self.stock['Iron']}", True, "black")
        silver = FONT.render(f"Silver: {self.stock['Silver']}", True, "black")
        gold = FONT.render(f"Gold: {self.stock['Gold']}", True, "black")
        mithril = FONT.render(f"Mithril: {self.stock['Mithril']}", True, "black")
        dragonite = FONT.render(f"Dragonite: {self.stock['Dragonite']}", True, "black")

        bronze_rect = bronze.get_rect(topleft=self.rect.topleft)
        iron_rect = iron.get_rect(topleft=bronze_rect.bottomleft)
        silver_rect = silver.get_rect(topleft=iron_rect.bottomleft)
        gold_rect = gold.get_rect(topleft=silver_rect.bottomleft)
        mithril_rect = mithril.get_rect(topleft=(bronze_rect.topright[0] + 20, 0))
        dragonite_rect = dragonite.get_rect(topleft=mithril_rect.bottomleft)

        pygame.draw.rect(self.screen, "purple", self.rect, border_radius=10)
        self.screen.blit(bronze, bronze_rect)
        self.screen.blit(iron, iron_rect)
        self.screen.blit(silver, silver_rect)
        self.screen.blit(gold, gold_rect)
        self.screen.blit(mithril, mithril_rect)
        self.screen.blit(dragonite, dragonite_rect)


def match_buttons(shop_button: ShopButton, buttons: pygame.sprite.Group):
    button = next(filter(lambda b: b.material in shop_button.text.split(), buttons))
    button.toggle_button()
    shop_button.kill()
