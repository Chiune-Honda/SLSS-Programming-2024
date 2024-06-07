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

WIDTH = 1080
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soccer Physics")


class PlayerL(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        # self.image = pg.Surface((25, 120))
        # self.image.fill(BLACK)
        self.image = pg.image.load("./images/crayonshinchanbestversionleft.png")
        self.image = pg.transform.scale(
            self.image, (self.image.get_width() // 2.75, self.image.get_height() // 2.75)
        )

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = 50, HEIGHT // 2 - 50

        self.change_x = 0
        self.change_y = 0

    def go_left(self):
            """ Called when the user hits the left arrow. """
            self.rect.x -= 4        
    
    def go_right(self):
            """ Called when the user hits the right arrow. """
            self.rect.x += 4

    def go_up(self):
            """ Called when the user hits the left arrow. """
            self.rect.y -= 4
    
    def go_down(self):
            """ Called when the user hits the right arrow. """
            self.rect.y += 4
    
    def stop(self):
            """ Called when the user lets off the keyboard. """
            self.change_x = 0

    def update(self):
        """Keep the player in the screen"""
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    def update(self):
        """Keep the player in the screen"""
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH / 2:
            self.rect.right = WIDTH / 2


class PlayerR(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        # # Draw a circle inside of it
        # self.image = pg.Surface((25, 120))
        # self.image.fill(BLACK)

        self.image = pg.image.load("./images/crayon-shin-chan-right.png")
        self.image = pg.transform.scale(
            self.image, (self.image.get_width() // 1.75, self.image.get_height() // 1.75)
        )



        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = WIDTH - 100, HEIGHT // 2 - 50

        self.change_x = 0
        self.change_y = 0

    def go_left(self):
            """ Called when the user hits the left arrow. """
            self.rect.x -= 4
    
    def go_right(self):
            """ Called when the user hits the right arrow. """
            self.rect.x += 4

    def go_up(self):
            """ Called when the user hits the left arrow. """
            self.rect.y -= 4
    
    def go_down(self):
            """ Called when the user hits the right arrow. """
            self.rect.y += 4

    def stop(self):
            """ Called when the user lets off the keyboard. """
            self.change_x = 0

    def update(self):
        """Keep the player in the screen"""
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    def update(self):
        """Keep the player in the screen"""
        if self.rect.left < WIDTH / 2:
            self.rect.left = WIDTH / 2
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH





class Ball(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        # Draw a circle inside of it



        self.radius = 15  # Radius of the ball
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()
        
        # self.rect.x, self.rect.y = WIDTH // 2 - self.radius, HEIGHT // 2 - self.rad
        # self.image = pygame.Surface((30, 30))
        # # TODO: Make a circle
        # pygame.draw.circle(self.image, BLACK, (self.image.get_width() // 2, self.image.get_height() // 2), self.image.get_width() // 10)
        # # ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

        self.ball_speed = [5, 5]

        self.rect = self.image.get_rect()

    def update(self):
        # Move ball
        self.rect.x += self.ball_speed[0]
        self.rect.y += self.ball_speed[1]

    def update(self):
        # Move ball
        self.rect.x += self.ball_speed[0]
        self.rect.y += self.ball_speed[1]

        # Check for collision with walls
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.ball_speed[0] *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.ball_speed[1] *= -1

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

        active_sprite_list = pg.sprite.Group()
        # active_sprite_list.add(playerleft)
        # active_sprite_list.add(playerright)
        
        while not done:
        # --- Event Listener
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_DOWN:
                #         playerright.go_down()
                #     if event.key == pg.K_LEFT:
                #         playerright.go_left()
                #     if event.key == pg.K_RIGHT:
                #         playerright.go_right()
                #     if event.key == pg.K_UP:
                #         playerright.go_up()
 
                #     # if event.key== pg.K_w:
                #     #     playerleft.go_up()
                #     # if event.key == pg.K_a:
                #     #     playerright.go_left()
                #     # if event.key == pg.K_d:
                #     #     playerright.go_right()
                #     # if event.key == pg.K_s:
                #     #     playerright.go_down()

                # if event.type == pg.KEYUP:
                #     if event.key == pg.K_LEFT and playerleft.change_x < 0:
                #         playerleft.stop()
                #     if event.key == pg.K_RIGHT and playerleft.change_x > 0:
                #         playerleft.stop()
                #     if event.key == pg.K_DOWN and playerleft.change_y < 0:
                #         playerleft.stop()
                #     if event.key == pg.K_UP and playerleft.change_y > 0:
                #         playerleft.stop()
                
                # if event.type == pg.KEYUP:
                #     if event.key == pg.K_LEFT and playerright.change_x < 0:
                #         playerright.stop()
                #     if event.key == pg.K_RIGHT and playerright.change_x > 0:
                #         playerright.stop()
                #     if event.key == pg.K_DOWN and playerright.change_y < 0:
                #         playerright.stop()
                #     if event.key == pg.K_UP and playerright.change_y > 0:
                #         playerright.stop()
                    
            # Key and controls
            keys_pressed = pg.key.get_pressed()

            if keys_pressed[pg.K_w]:
                playerleft.go_up()
            if keys_pressed[pg.K_s]:
                playerleft.go_down()
            if keys_pressed[pg.K_a]:
                playerleft.go_left()
            if keys_pressed[pg.K_d]:
                playerleft.go_right()


            if keys_pressed[pg.K_UP]:
                playerright.go_up()
            if keys_pressed[pg.K_DOWN]:
                playerright.go_down()
            if keys_pressed[pg.K_LEFT]:
                playerright.go_left()
            if keys_pressed[pg.K_RIGHT]:
                playerright.go_right()


            if ball.rect.colliderect(playerleft):
                if ball.ball_speed[0] < 0 and ball.rect.left < playerleft.rect.right:
                    ball.rect.left = playerleft.rect.right
                    ball.ball_speed[0] *= -1
                if ball.ball_speed[0] > 0 and ball.rect.right > playerleft.rect.left:
                    ball.rect.right = playerleft.rect.left
                    ball.ball_speed[0] *= -1
                # ball.ball_speed[1] *= -1

            # ball hits the left side of playerleft
            # for y in range(playerleft.rect.top, playerleft.rect.bottom):
            #     if ball.rect.collidepoint(playerleft.rect.left, y):
            #         ball.ball_speed[0] *= -1

            #         print("collided")

            if ball.rect.colliderect(playerright):
                ball.ball_speed[0] *= -1


            all_sprites.update()

            screen.fill(WHITE)

            
            all_sprites.draw(screen)
            #
            # tive_sprite_list.draw(screen)

            # Update the screen with anything new
            pg.display.flip()

            # --- Tick the Clock
            clock.tick(60)  # 60 fps

        pg.quit()

def main():
    start()


if __name__ == "__main__":
    main()