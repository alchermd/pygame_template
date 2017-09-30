import pygame
import colors as c
from models import Game

def main():
    # Initialize the pygame engine.
    pygame.init()

    # Setup the main screen.
    main_screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("hello, pygame")
    
    # Create a Game instance.
    game = Game(main_screen, c.white)

    # Meta variables.
    fps = 30
    clock = pygame.time.Clock()

    # Main game loop.
    while game.handle_events():
        clock.tick(fps)

        game.run_game_logic()

        game.display_frame()

    # Exit the Pygame engine.
    pygame.quit()

if __name__ == '__main__':
    main()