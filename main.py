import pygame
from data.ui import Button, MATERIALS, BUTTON_SIZE, generate_coords
from data.collisions import FloatScore, check_click_collision


WIDTH = 1200
HEIGHT = 800
BG_COLOR = "#505050"
GAME_TITLE = "Incremental"
BASE_BG_PATH = "./data/sprites/parallax_forest_pack web/v2/"


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load(f"{BASE_BG_PATH}preview.png").convert_alpha()
        self.scaled_bg = pygame.transform.scale(
            self.bg,
            (WIDTH, HEIGHT),
            self.screen,
        ).convert_alpha()

        self.button_coords = generate_coords(self.screen)
        self.buttons = pygame.sprite.Group()
        for (x, y), material in zip(self.button_coords, MATERIALS):
            button = Button(self.screen, material, (x, y), BUTTON_SIZE)
            if material != "Bronze":
                button.toggle_button()
            self.buttons.add(button)

        self.mining_power = 1
        self.scores = pygame.sprite.Group()

    def run(self):
        while True:
            self.screen.blit(self.scaled_bg, (0, 0))
            self.clock.tick(60)
            self.buttons.update()
            self.scores.update()
            self.scores.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    collisions = check_click_collision(self.buttons, event)
                    if collisions and collisions[0].enabled:
                        self.scores.add(FloatScore(f"+{self.mining_power}", event.pos))

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
