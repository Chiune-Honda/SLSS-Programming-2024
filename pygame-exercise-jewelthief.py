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

NUM_COINS = 50

NUM_TYLER = 5

BURGER_IMAGE =  pg.image.load("./Images/image-removebg-preview.png")
BURGER_IMAGE = pg.transform.scale(BURGER_IMAGE, (BURGER_IMAGE.get_width() // 3, BURGER_IMAGE.get_width() // 3))

TYLER_IMAGE = pg.image.load("./Images/1068776.jpg")
TYLER_IMAGE = pg.transform.scale(TYLER_IMAGE, (TYLER_IMAGE.get_width() // 5, TYLER_IMAGE.get_height() // 5))

TYLERL_IMAGE = pg.image.load("./Images/Screenshot 2024-05-06 at 12.32.09 PM.png")
TYLERL_IMAGE = pg.transform.scale(TYLERL_IMAGE, (TYLERL_IMAGE.get_width() // 2.75, TYLERL_IMAGE.get_height() // 2.75))




class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = TYLERL_IMAGE

        self.rect = self.image.get_rect()

        self.lives = 10
        self.rect = self.image.get_rect() 

    def update(self):
        """Update the location of Mario with the mouse"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]

    def update(self):
        """Update the location of Mario with the mouse"""
        next_pos = pg.mouse.get_pos()

        self.rect.center = next_pos



class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = BURGER_IMAGE
        self.rect = self.image.get_rect()


        # Randomize initial location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

class Tylerlogo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
                
        # set the image to a scaled version
        self.image = TYLER_IMAGE

        self.rect = self.image.get_rect()

        # Spawn in a random location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        self.vel_x = random.choice([-6, -5, -4, 4, 5, 6])
        self.vel_y = random.choice([-6, -5, -4, 4, 5, 6])

        self.max_speed = 9

    def update(self):
        """Make the goomba move and bounce"""
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce off the edge of the screen
        if self.rect.top < 0:
            self.rect.top = 0  # keep it inside the screen
            self.vel_y *= -1
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x *= -1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x *= -1

    def increase_speed(self):
        """Increase speed to a limit"""

        if abs(self.vel_x) < self.max_speed:
            if self.vel_x > 0:
                self.vel_x += 0.25
            else:
                self.vel_x -= 0.25
        if abs(self.vel_y) < self.max_speed:
            if self.vel_y > 0:
                self.vel_y += 0.25
            else:
                self.vel_y -= 0.25

def start():
    pg.init()

    # Hide the mouse
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    font = pg.font.SysFont("Futura", 24)

    # Sprite Groups
    all_sprites = pg.sprite.Group()
    coin_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()

    # Create Player object
    player = Player()
    
    
    for  _ in range(NUM_TYLER):
        tylerlogo = Tylerlogo()
        all_sprites.add(tylerlogo)
        enemy_sprites.add(tylerlogo)
        
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

            for sprite in enemy_sprites:
                sprite.increase_speed()

        enemies_collided = pg.sprite.spritecollide(player, enemy_sprites, False)

        for enemy in enemies_collided:
            player.lives -= 0.1

            print(int(player.lives))


        # --- Draw items
        screen.fill(WHITE)

        # Create a surface for the score
        score_image = font.render(f"Score: {score}", True, BLACK)
        lives_image = font.render(f"Lives: {int(player.lives)}", True, BLACK)
        all_sprites.draw(screen)
        # "Blit" the surface on the screen
        screen.blit(score_image, (5, 5))
        screen.blit(lives_image, (5, 25))

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(75)  # 75 fps


def main():
    start()


if __name__ == "__main__":
    main()


