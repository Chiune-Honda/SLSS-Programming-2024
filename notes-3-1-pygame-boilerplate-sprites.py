# April 23 2024
# Chiune Honda
# Pygame Boilerplate Sprites

import pygame

class Tylerlogo(pygame.sprite.Sprite):
    '''Represents the DVD Logo'''
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/1068776.jpg")
        self.rect = self.image.get_rect() 
        
        self.image = pygame.transform.scale(self.image, (self.rect.width // 2, self.rect.height // 2))
        self.rect = self.image.get_rect() 


        # sets the x and y to 0
        #   first positionof the image is in the top right


def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS
    WHITE   = (255, 255, 255)
    BLACK   = (  0,   0,   0)
    EMERALD = ( 21, 219, 147)
    RED     = (255,   0,   0)
    GREEN   = (  0, 255,   0)
    BLUE    = (  0,   0, 255)
    GRAY    = (128, 128, 128)

    WIDTH   = 1280    # Pixels
    HEIGHT  =  720
    SCREEN_SIZE = (WIDTH, HEIGHT)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    tylerlogo = Tylerlogo()
    # Move the tyler logo to the middle-ish

    tylerlogo.rect.centerx = WIDTH // 2
    tylerlogo.rect.centery = HEIGHT // 2

    all_sprites = pygame.sprite.Group()
    all_sprites.add(tylerlogo)

    pygame.display.set_caption("Tyler the Creator screen saver")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

		# --- Update the world state

        # --- Draw items
        screen.fill(BLUE)

        all_sprites.draw(screen)
      
        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)    # 60 fps


def main():
    start()

if __name__ == "__main__":
    main()