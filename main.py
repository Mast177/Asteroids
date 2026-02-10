import pygame
import sys
from constants import SCREEN_HEIGHT as SCREEN_HEIGHT, SCREEN_WIDTH as SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    #initilization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #print basic settings
    print("Starting Asteroids with pygame version:" + pygame.version.ver)
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    #create game groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    #instantiate asteroid field
    AsteroidField()

    #instantiate player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    #game clock
    clock = pygame.time.Clock()
    dt = 0


    #game loop
    while True:
        log_state()
        #handle events
        for event in pygame.event.get():
            #close the game if the user closes the window
            if event.type == pygame.QUIT:
                return
        
        #update display
        screen.fill("black")

        #handle input
        for asset in updatable:
            asset.update(dt)

        #check for collision
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()


        #draw sprites
        for sprite in drawable:
            sprite.draw(screen)
        

        #refresh screen (call last)
        pygame.display.flip()

        #update delta time (keep game running at smooth fps and reduce system resource use)
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
