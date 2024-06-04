import random
import pygame as pg
import pygame

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)
# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soccer Physics")


class PlayerL(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        self.image = pg.Surface((30, 70))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = 50, HEIGHT // 2 - 50

        # playerleft = pygame.Rect(50, HEIGHT // 2 - 50, 50, 100)

        # self.rect = playerleft.get_rect()


class PlayerR(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        # Draw a circle inside of it
        self.image = pg.Surface((30, 70))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = WIDTH - 100, HEIGHT // 2 - 50

        # Draw a circle inside of it
        # playerright = pygame.Rect(WIDTH - 100, HEIGHT // 2 - 50, 50, 100)

        # self.rect = playerright.get_rect()



class Ball(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        # Draw a circle inside of it
        self.image = pygame.Surface((30, 30))
        # TODO: Make a circle
        pygame.draw.circle(self.image, BLACK, (self.image.get_width() // 2, self.image.get_height() // 2), self.image.get_width() // 10)
        # ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

        self.ball_speed = [5, 5]

        self.rect = self.image.get_rect()

    def update(self):
        # Move ball
        self.rect.x += self.ball_speed[0]
        self.rect.y += self.ball_speed[1]
    
    # # Ball collision with players
    #     ball_collided = pg.sprite.spritecollide(playerleft, ball_sprites, True)

    #     if ball_collided:
    #         ball_speed[0] *= -1

        # Ball collision with walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.ball_speed[1] *= -1
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.ball_speed[0] *= -1


        playerleft = PlayerL()
        playerright = PlayerR()

        all_sprites = pg.sprite.Group()
        ball_sprites = pg.sprite.Group()

        all_sprites.add(playerleft)
        all_sprites.add(playerright)

        ball = Ball()

        all_sprites.add(ball)
        ball_sprites.add(ball)

# Game loop
def start():
    
        pg.init()

        # --Game State Variables--
        screen = pg.display.set_mode(SCREEN_SIZE)
        done = False
        clock = pg.time.Clock()

        playerleft = PlayerL()
        playerright = PlayerR()

        all_sprites = pg.sprite.Group()
        ball_sprites = pg.sprite.Group()

        all_sprites.add(playerleft)
        all_sprites.add(playerright)

        ball = Ball()

        all_sprites.add(ball)
        ball_sprites.add(ball)

        while not done:
        # --- Event Listener
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

                    if event.type == pg.K_DOWN:
                        playerright.go_down()
                    if event.key == pg.K_LEFT:
                        playerright.go_left()
                    if event.key == pg.K_RIGHT:
                        playerright.go_right()
                    if event.key == pg.K_UP:
                        playerright.go_up()
 
                    if event.type == pg.K_w:
                        playerleft.go_up()
                    if event.key == pg.K_a:
                        playerright.go_left()
                    if event.key == pg.K_RIGHT:
                        playerright.go_right()
                    if event.key == pg.K_UP:
                        playerright.jump()

                if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pg.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Move players
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            playerleft.rect.y -= 5
        if keys[pygame.K_s]:
            playerleft.rect.y += 5
        if keys[pygame.K_UP]:
            playerright.rect.y -= 5
        if keys[pygame.K_DOWN]:
            playerright.rect.y += 5
        
        all_sprites.update()

        # Ball collision with players    
        ball_collided = pg.sprite.spritecollide(playerleft, ball_sprites, False)
        ball_collided = pg.sprite.spritecollide(playerright, ball_sprites, False)

        screen.fill(WHITE)


     
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

        pg.quit()

def main():
    start()


if __name__ == "__main__":
    main()