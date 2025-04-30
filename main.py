import pygame
from constants import *
from player import Player

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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    p = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt) 
        screen.fill((0,0,0))
        ##Render stuff here
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        ## 60 FPS Limit
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
