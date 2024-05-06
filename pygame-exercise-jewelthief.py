# pygame-exercise-jewelthief.py

# A Jewel Thief Clone

import random

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_COINS = 100

NUM_TYLER = 5


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/Screenshot 2024-05-06 at 12.32.09 PM.png")
        self.rect = self.image.get_rect() 
        self.image = pg.transform.scale(self.image, (self.rect.width // 1.5, self.rect.height // 1.5))

        self.rect = self.image.get_rect()

    def update(self):
        """Update the location of Mario with the mouse"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/image-removebg-preview.png")
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (self.rect.width // 3, self.rect.height // 3))
        self.rect = self.image.get_rect()


        # Randomize initial location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

class Tylerlogo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/1068776.jpg")
        self.rect = self.image.get_rect() 
                
        self.image = pg.transform.scale(self.image, (self.rect.width // 3.25, self.rect.height // 3.25))
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

    pg.init()

    # Hide the mouse
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    # Sprite Groups
    all_sprites = pg.sprite.Group()
    coin_sprites = pg.sprite.Group()

    # Create Player object
    player = Player()
    tylerlogo = Tylerlogo
    

    for  _ in range(NUM_TYLER):
        tylerlogo = Tylerlogo()
        all_sprites.add(tylerlogo)
        
    all_sprites.add(player)
    # Create Coin objects
    for _ in range(NUM_COINS):
        coin = Coin()

        all_sprites.add(coin)
        coin_sprites.add(coin)

    pg.display.set_caption("Jewel Thief Clone (Nintendo Don't Sue Us)")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # Get a list of ALL COINS Mario has collided with
        coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)

        for coin in coins_collided:
            # Increase the score by 10
            score += 10

            print(f"Score: {score}")

        # If the coin_sprites group is empty, respawn all coins
        if len(coin_sprites) <= 0:
            for _ in range(NUM_COINS):
                coin = Coin()

                all_sprites.add(coin)
                coin_sprites.add(coin)

        # --- Draw items
        screen.fill(WHITE)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()


