import pygame
from constants import SCREEN_HEIGHT as SCREEN_HEIGHT, SCREEN_WIDTH as SCREEN_WIDTH
from logger import log_state


def main():
    #initilization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #print basic settings
    print("Starting Asteroids with pygame version:" + pygame.version.ver)
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

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
        #refresh screen (call last)
        pygame.display.flip()


if __name__ == "__main__":
    main()
