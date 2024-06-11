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
        # self.image = pg.image.load("./images/crayonshinchanbestversionleft.png")
        # self.image = pg.transform.scale(
        #     self.image, (self.image.get_width() // 2.75, self.image.get_height() // 2.75)
        # )

        self.radius = 20  # Radius of the ball
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, BLUE, (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = WIDTH * 1/8, HEIGHT // 2

        self.change_x = 0
        self.change_y = 0

    def go_left(self):
            """ Called when the user hits the left arrow. """
            if self.change_x >= 0:
                self.change_x = -1
            self.rect.x += self.change_x   
    
    def go_right(self):
            """ Called when the user hits the right arrow. """
            if self.change_x <= 0:
                self.change_x = 1
            self.rect.x += self.change_x

    def go_up(self):
            """ Called when the user hits the left arrow. """
            if self.change_y >= 0:
                self.change_y = -1
            self.rect.y += self.change_y
    
    def go_down(self):
            """ Called when the user hits the right arrow. """
            if self.change_y <= 0:
                self.change_y = 1
            self.rect.y += self.change_y   

    def update(self):
        """Keep the player in the screen"""
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        """Keep the player in the screen"""
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH / 2:
            self.rect.right = WIDTH / 2

        if self.change_x > 0:
                # self.change_x = max(self.change_x + 2, 50)
            if self.change_x < 7:
                self.change_x += 0.1
        if self.change_x < 0:
                # self.change_x = min(self.change_x - 2, -50)
            if self.change_x > -7:
                self.change_x -= 0.1
        
        if self.change_y < 0:
                # self.change_x = min(self.change_x - 2, -50)
            if self.change_y > -7:
                self.change_y -= 0.1
        if self.change_y > 0:
                # self.change_x = max(self.change_x + 2, 50)
            if self.change_y < 7:
                self.change_y += 0.1
        
        print(self.change_x, self.change_y)
        
        

class PlayerR(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        # # Draw a circle inside of it
        # self.image = pg.Surface((25, 120))
        # self.image.fill(BLACK)

        # self.image = pg.image.load("./images/crayon-shin-chan-right.png")
        # self.image = pg.transform.scale(
        #     self.image, (self.image.get_width() // 1.75, self.image.get_height() // 1.75)
        # )

        self.radius = 20  # Radius of the ball
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = WIDTH * 7/8, HEIGHT // 2

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
        """Keep the player in the screen"""
        if self.rect.left < WIDTH / 2:
            self.rect.left = WIDTH / 2
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class GoalR(pg.sprite.Sprite):
     def __init__(self):
        super().__init__()

        self.image = pg.Surface((15, 130))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

        # Place goal in the middle of the side of the screen

        self.rect.right = WIDTH
        self.rect.centery = HEIGHT // 2

class GoalL(pg.sprite.Sprite):
     def __init__(self):
        super().__init__()

        self.image = pg.Surface((15, 130))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

        # Place goal in the middle of the side of the screen

        self.rect.left = 0
        self.rect.centery = HEIGHT // 2




class Ball(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        self.radius = 15  # Radius of the ball
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)

        self.ball_speed_x = 0
        self.ball_speed_y = 0

        # Always spawn ball on playerleft's side

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 4
        self.rect.centery = HEIGHT // 2


    def update(self):
        # Move ball

        # self.calc_grav()

        self.rect.x += self.ball_speed_x
        self.rect.y += self.ball_speed_y

        # Check for collision with walls
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.ball_speed[0] *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.ball_speed[1] *= -1

    # def calc_grav(self):
    #     if self.ball_speed_x == 0:
    #         self.ball_speed_x = 1
    #     else:
    #         self.ball_speed_x += .35

    #     if self.ball_speed_y == 0:
    #         self.ball_speed_y = 1
    #     else:
    #         self.ball_speed_y += .35

      

def reset_positions(playerleft: PlayerL, playerright: PlayerR, goalright: GoalR, goalleft: GoalL, ball: Ball):
    playerleft.rect.x, playerleft.rect.y = 50, HEIGHT // 2 - 50
    playerright.rect.x, playerright.rect.y = WIDTH - 100, HEIGHT // 2 - 50
    goalright.rect.right, goalright.rect.y = WIDTH, HEIGHT // 2 - 50
    goalleft.rect.left, goalleft.rect.y = 0, HEIGHT // 2 - 50




# Game loop
def start():
    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    font = pg.font.SysFont("Futura", 24)
    score = 0

    playerleft = PlayerL()
    playerright = PlayerR()
    goalright = GoalR()
    goalleft = GoalL()
    ball = Ball()

    all_sprites = pg.sprite.Group()
    ball_sprites = pg.sprite.Group()
    goalleft_sprites = pg.sprite.Group()
    goalright_sprites = pg.sprite.Group()

    all_sprites.add(playerleft)
    all_sprites.add(playerright)
    all_sprites.add(goalright)
    all_sprites.add(goalleft)
    all_sprites.add(ball)

    goalleft_sprites.add(goalleft)
    goalright_sprites.add(goalright)

    ball_sprites.add(ball)

    
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        all_sprites.update()

        goalleft_collided = pg.sprite.spritecollide(ball, goalleft_sprites, True)
        goalright_collided = pg.sprite.spritecollide(ball, goalright_sprites, True)


        for goalleft in goalleft_collided:
        # Increase the score by 10
            score += 1
            print(f"Score: {score}")
    

        for goalright in goalright_collided:
        # Increase the score by 10
            score += 1
            print(f"Score: {score}")

        
                        
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
            ball.ball_speed[0] *= -1

        if ball.rect.colliderect(playerright):
            ball.ball_speed[0] *= -1

        screen.fill(WHITE)

        score_image = font.render(f"Score: {score}", True, BLACK)
        all_sprites.draw(screen)

        # "Blit" the surface on the screen
        screen.blit(score_image, (5, 5))

        all_sprites.draw(screen)
           
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(75)  # 75 fps

def main():
    start()


if __name__ == "__main__":
    main()