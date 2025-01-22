import pygame, player
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    game_start = ["Starting asteroids!",
                   f"Screen width: {SCREEN_WIDTH}",
                   f"Screen height: {SCREEN_HEIGHT}"
                ]
    print("\n".join(game_start))
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    p = player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        ##Render stuff here
        p.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) // 10000
        

if __name__ == "__main__":
    main()