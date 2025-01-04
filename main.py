import pygame
from constants import *

def main():
    pygame.init()
    game_start = ["Starting asteroids!",
                   f"Screen width: {SCREEN_WIDTH}",
                   f"Screen height: {SCREEN_HEIGHT}"
                ]
    print("\n".join(game_start))
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()