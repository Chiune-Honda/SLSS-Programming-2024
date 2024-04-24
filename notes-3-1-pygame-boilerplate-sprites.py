# April 23 2024
# Chiune Honda
# Pygame Boilerplate Sprites

import pygame
import random

class Tylerlogo(pygame.sprite.Sprite):
    '''Represents the DVD Logo'''
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/1068776.jpg")
        self.rect = self.image.get_rect() 
                
        self.image = pygame.transform.scale(self.image, (self.rect.width // 2.5, self.rect.height // 2.5))
        self.rect = self.image.get_rect() 

        self.rect.centerx = random.randrange(100,1000)
        self.rect.centery = random.randrange(120,580)

        # How much position changes over time
        #   - pixels per tick
        
        self.vel_x = random.randrange(1,10)
        self.vel_y = random.randrange(1,10)

    def update(self):
        # Update position of Dvdlogo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep the Dvdlogo in the scren
        # Right side of the screen
        #      - if the right edge of dvdlogo > WIDTH
        #               - switch the direction (+vel-x -> -vel-x)
        if self.rect.right >= 1280:
            self.vel_x = -self.vel_x

        # Left side

        if self.rect.left <= 0:
            self.vel_x = -self.vel_x

        print(self.rect.x, self.rect.y)

        # Top

        if self.rect.top >= 0:
            self.vel_y = -self.vel_y
        
        # Down

        if self.rect.bottom <= 720:
            self.vel_y = -self.vel_y

class Travislogo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/whats-the-weirdest-hot-take-on-travis-scott-youve-ever-heard-v0-5ahr4mtmx1ob1.webp")
        self.rect = self.image.get_rect() 
                
        self.image = pygame.transform.scale(self.image, (self.rect.width // 5, self.rect.height // 5))
        self.rect = self.image.get_rect() 

        self.rect.centerx = random.randrange(100,1000)
        self.rect.centery = random.randrange(100,600)

        # How much position changes over time
        #   - pixels per tick
        
        self.vel_x = random.randrange(1,10)
        self.vel_y = random.randrange(1,10)

    def update(self):
        # Update position of Dvdlogo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep the Dvdlogo in the scren
        # Right side of the screen
        #      - if the right edge of dvdlogo > WIDTH
        #               - switch the direction (+vel-x -> -vel-x)
        if self.rect.right >= 1280:
            self.vel_x = -self.vel_x

        # Left side

        if self.rect.left <= 0:
            self.vel_x = -self.vel_x

        print(self.rect.x, self.rect.y)

        # Top

        if self.rect.top >= 0:
            self.vel_y = -self.vel_y
        
        # Down

        if self.rect.bottom <= 720:
            self.vel_y = -self.vel_y

class Kanyelogo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/8743a10b2b1958f8541af429ecf7e03e.jpg")
        self.rect = self.image.get_rect() 
                
        self.image = pygame.transform.scale(self.image, (self.rect.width // 2.5, self.rect.height // 2.5))
        self.rect = self.image.get_rect() 

        self.rect.centerx = random.randrange(100,1000)
        self.rect.centery = random.randrange(100,600)

        # How much position changes over time
        #   - pixels per tick
        
        self.vel_x = random.randrange(1,10)
        self.vel_y = random.randrange(1,10)

    def update(self):
        # Update position of Dvdlogo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep the Dvdlogo in the scren
        # Right side of the screen
        #      - if the right edge of dvdlogo > WIDTH
        #               - switch the direction (+vel-x -> -vel-x)
        if self.rect.right >= 1280:
            self.vel_x = -self.vel_x

        # Left side

        if self.rect.left <= 0:
            self.vel_x = -self.vel_x

        print(self.rect.x, self.rect.y)

        # Top

        if self.rect.top >= 0:
            self.vel_y = -self.vel_y
        
        # Down

        if self.rect.bottom <= 720:
            self.vel_y = -self.vel_y


class Tylerdoralogo(pygame.sprite.Sprite):
    '''Represents the DVD Logo'''
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/images.jpeg")
        self.rect = self.image.get_rect() 
                
        self.image = pygame.transform.scale(self.image, (self.rect.width // 1, self.rect.height // 1))
        self.rect = self.image.get_rect() 

        self.rect.centerx = random.randrange(100,1000)
        self.rect.centery = random.randrange(120,580)

        # How much position changes over time
        #   - pixels per tick
        
        self.vel_x = random.randrange(1,10)
        self.vel_y = random.randrange(1,10)

    def update(self):
        # Update position of Dvdlogo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep the Dvdlogo in the scren
        # Right side of the screen
        #      - if the right edge of dvdlogo > WIDTH
        #               - switch the direction (+vel-x -> -vel-x)
        if self.rect.right >= 1280:
            self.vel_x = -self.vel_x

        # Left side

        if self.rect.left <= 0:
            self.vel_x = -self.vel_x

        print(self.rect.x, self.rect.y)

        # Top

        if self.rect.top >= 0:
            self.vel_y = -self.vel_y
        
        # Down

        if self.rect.bottom <= 720:
            self.vel_y = -self.vel_y

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
    kanyelogo = Kanyelogo()
    travislogo = Travislogo()
    tylerdoralogo = Tylerdoralogo()
    # Move the tyler logo to the middle-ish


    all_sprites = pygame.sprite.Group()
    all_sprites.add(tylerlogo)
    all_sprites.add(kanyelogo)
    all_sprites.add(travislogo)
    all_sprites.add(tylerdoralogo)

    pygame.display.set_caption("Funny black people screen saver")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

		# --- Update the world state
        all_sprites.update()


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