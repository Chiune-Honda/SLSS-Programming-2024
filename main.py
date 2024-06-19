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

WIDTH = 1920
HEIGHT = 1080
SCREEN_SIZE = (WIDTH, HEIGHT)
# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("O₂ Hockey")

class PlayerL(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        self.radius = 40  # Radius of the ball
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, BLUE, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = WIDTH * 1/8, HEIGHT // 2

        self.max_speed = 6  # Maximum speed
        self.acceleration = 0.5  # Acceleration rate
        self.deceleration = 0.2  # Deceleration rate

        self.change_x = 0
        self.change_y = 0

        self.score = 0

    def go_left(self):
        if self.change_x > -self.max_speed:
            self.change_x -= self.acceleration
    
    def go_right(self):
        if self.change_x < self.max_speed:
            self.change_x += self.acceleration

    def go_up(self):
        if self.change_y > -self.max_speed:
            self.change_y -= self.acceleration
    
    def go_down(self):
        if self.change_y < self.max_speed:
            self.change_y += self.acceleration

    def stop(self):
        if self.change_x > 0:
            self.change_x = max(self.change_x - self.deceleration, 0)
        elif self.change_x < 0:
            self.change_x = min(self.change_x + self.deceleration, 0)
            
        if self.change_y > 0:
            self.change_y = max(self.change_y - self.deceleration, 0)
        elif self.change_y < 0:
            self.change_y = min(self.change_y + self.deceleration, 0)

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        """Keep the player in the screen"""
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH / 2:
            self.rect.right = WIDTH / 2

       
class PlayerR(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        self.radius = 40  # Radius of the ball
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = WIDTH * 7/8, HEIGHT // 2

        self.max_speed = 6  # Maximum speed
        self.acceleration = 0.5  # Acceleration rate
        self.deceleration = 0.2  # Deceleration rate

        self.change_x = 0
        self.change_y = 0

        self.score = 0

    def go_left(self):
        if self.change_x > -self.max_speed:
            self.change_x -= self.acceleration
    
    def go_right(self):
        if self.change_x < self.max_speed:
            self.change_x += self.acceleration

    def go_up(self):
        if self.change_y > -self.max_speed:
            self.change_y -= self.acceleration
    
    def go_down(self):
        if self.change_y < self.max_speed:
            self.change_y += self.acceleration

    def stop(self):
        if self.change_x > 0:
            self.change_x = max(self.change_x - self.deceleration, 0)
        elif self.change_x < 0:
            self.change_x = min(self.change_x + self.deceleration, 0)
            
        if self.change_y > 0:
            self.change_y = max(self.change_y - self.deceleration, 0)
        elif self.change_y < 0:
            self.change_y = min(self.change_y + self.deceleration, 0)

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
     
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

class CircleinMiddle(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        self.radius = 50  # Radius of the ball
        self.diameter = self.radius * 2
        # BLACK_TRANSPARENT = (0, 0, 0, 100)  # Black with alpha = 150 (semi-transparent)

        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)

        pg.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)
        # pg.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

class CircleinMiddleInside(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        self.radius = 40  # Radius of the ball
        self.diameter = self.radius * 2
          # Black with alpha = 150 (semi-transparent)

        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)

        pg.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)
        # pg.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2


class MiddleLine(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        # BLACK_TRANSPARENT = (0, 0, 0, 100)

        self.image = pg.Surface((15, 1080), pg.SRCALPHA)
        self.image.fill(BLACK)

        
        self.rect = self.image.get_rect()

        # Place goal in the middle of the side of the screen

        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2




class Ball(pg.sprite.Sprite):
    def __init__(self):
        # Super class constructor
        super().__init__()

        self.radius = 17  # Radius of the ball
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)

        self.ball_speed_x = 0
        self.ball_speed_y = 0

        # Always spawn ball on playerleft's side

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 4
        self.rect.centery = HEIGHT // 2
        self.deceleration = 0.01  # Deceleration rate

    def update(self):
        # Move ball

        # self.calc_grav()

        # if self.ball_speed_x:
        if self.ball_speed_x < 0:  # right to left
            self.ball_speed_x = min(self.ball_speed_x + self.deceleration, 0)
        if self.ball_speed_x > 0:  # right to left
            self.ball_speed_x = max(self.ball_speed_x - self.deceleration, 0)

        self.rect.x += self.ball_speed_x
        self.rect.y += self.ball_speed_y
 
        # Check for collision with walls
        if self.rect.left <= 0:
            self.rect.left = 0
            self.ball_speed_x *= -1
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.ball_speed_x *= -1

        if self.rect.top <= 0:
            self.rect.top = 0
            self.ball_speed_y *= -1
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.ball_speed_y *= -1

    def hitright(self, player):
    # Called when the ball is hit by a player
    # Change the ball's speed based on the player's direction and speed
        self.rect.left = player.rect.right
        # self.ball_speed_x = 3
        # self.ball_speed_y = 3
        if self.ball_speed_x == 0:
            self.ball_speed_x = player.change_x + 3
        else:
            self.ball_speed_x = player.change_x + 3
        self.ball_speed_y = player.change_y

    def hittop(self, player):

        self.rect.bottom = player.rect.top

        if self.ball_speed_y == 0:
            self.ball_speed_y = player.change_y  - 3
        else:
            self.ball_speed_y = player.change_y - 3
        self.ball_speed_x = player.change_x

    def hitbottom(self, player):
        
        self.rect.top = player.rect.bottom

        if self.ball_speed_y == 0:
            self.ball_speed_y = player.change_y + 3
        else: 
            self.ball_speed_y = player.change_y + 3
        self.ball_speed_x = player.change_x

            
    def hitleft(self, player):
        self.rect.right = player.rect.left

        if self.ball_speed_x == 0:
            self.ball_speed_x = player.change_x  - 3
        else:
            self.ball_speed_x = player.change_x - 3
        self.ball_speed_y = player.change_y
 
def reset_mainpositions(playerleft: PlayerL, playerright: PlayerR, goalright: GoalR, goalleft: GoalL):
    playerleft.rect.centerx, playerleft.rect.centery = WIDTH * 1/8, HEIGHT // 2
    playerleft.change_x, playerleft.change_y = 0, 0

    playerright.rect.centerx, playerright.rect.centery = WIDTH * 7/8, HEIGHT // 2
    playerright.change_x, playerright.change_y = 0, 0
    
    goalright.rect.right, goalright.rect.centery = WIDTH, HEIGHT // 2
    goalleft.rect.left, goalleft.rect.centery = 0, HEIGHT // 2
    
def reset_ballpositionrightscore(ball: Ball):
    ball.rect.centerx = WIDTH // 4
    ball.rect.centery = HEIGHT // 2
    ball.ball_speed_x, ball.ball_speed_y = 0, 0

def reset_ballpositionleftscore(ball: Ball):
    ball.rect.centerx = WIDTH * 0.75
    ball.rect.centery = HEIGHT // 2
    ball.ball_speed_x, ball.ball_speed_y = 0, 0

# Game loop
def start():
    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    font = pg.font.SysFont("Futura", 1000)

    playerleft = PlayerL()
    playerright = PlayerR()
    goalright = GoalR()
    goalleft = GoalL()
    ball = Ball()
    circleinmiddle = CircleinMiddle()
    middleline = MiddleLine()
    circleinmiddleinside = CircleinMiddleInside()

    all_sprites = pg.sprite.Group()
    ball_sprites = pg.sprite.Group()
    goalleft_sprites = pg.sprite.Group()
    goalright_sprites = pg.sprite.Group()


    all_sprites.add(middleline)
    all_sprites.add(circleinmiddle)
    all_sprites.add(circleinmiddleinside)
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

        goalleft_collided = pg.sprite.spritecollide(ball, goalleft_sprites, False)
        goalright_collided = pg.sprite.spritecollide(ball, goalright_sprites, False)

        if goalleft_collided:
            playerright.score += 1
            reset_mainpositions(playerleft, playerright, goalright, goalleft)
            reset_ballpositionrightscore(ball)

        if goalright_collided:
            playerleft.score += 1
            reset_mainpositions(playerleft, playerright, goalright, goalleft)
            reset_ballpositionleftscore(ball)

        #Key and controol
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
        
        if pygame.sprite.collide_circle(playerleft, ball):
            if playerleft.rect.right>ball.rect.left and playerleft.rect.centerx <ball.rect.left:
                ball.hitright(playerleft)
            if playerleft.rect.left<ball.rect.right and playerleft.rect.centerx > ball.rect.right:
                ball.hitleft(playerleft)
            if playerleft.rect.bottom > ball.rect.top and playerleft.rect.centery < ball.rect.top:
                ball.hitbottom(playerleft)
            if playerleft.rect.top < ball.rect.bottom and playerleft.rect.centery > ball.rect.bottom:
                ball.hittop(playerleft)
            
        if pygame.sprite.collide_circle(playerright, ball):
            if playerright.rect.right>ball.rect.left and playerright.rect.centerx <ball.rect.left:
                ball.hitright(playerright)
            if playerright.rect.left<ball.rect.right and playerright.rect.centerx > ball.rect.right:
                ball.hitleft(playerright)
            if playerright.rect.bottom > ball.rect.top and playerright.rect.centery < ball.rect.top:
                ball.hitbottom(playerright)
            if playerright.rect.top < ball.rect.bottom and playerright.rect.centery > ball.rect.bottom:
                ball.hittop(playerright)

        screen.fill(WHITE)

        scorel = font.render(f"{playerright.score}", True, (0, 0, 255))
        scorer = font.render(f"{playerleft.score}", True, (255, 0, 0))

        scorel.set_alpha(127)
        scorer.set_alpha(127)
        
        all_sprites.draw(screen)


        scorel_rect = scorel.get_rect()
        scorer_rect = scorer.get_rect()

        scorel_pos = (WIDTH * 0.22 - scorel_rect.width // 2, HEIGHT // 2 - scorel_rect.height // 2)
        scorer_pos = (WIDTH * 0.78 - scorer_rect.width // 2, HEIGHT // 2 - scorer_rect.height // 2)

        screen.blit(scorel, scorel_pos)
        screen.blit(scorer, scorer_pos)
        # # "Blit" the surface on the screen
        # screen.blit(scorel, (200, 540))
        # screen.blit(scorer, (1720, 540))

        all_sprites.draw(screen)
           
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(75)  # 75 fps

def main():
    start()


if __name__ == "__main__":
    main()