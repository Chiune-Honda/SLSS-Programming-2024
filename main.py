# Final Computer Progamming Level 1 Project
# Chiune Honda
# June 20 2024

import pygame as pg

# --CONSTANTS--
# COLOURS
# Define various color constants using RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Set screen dimensions
WIDTH = 1920
HEIGHT = 1080
SCREEN_SIZE = (WIDTH, HEIGHT)

# Set up the game screen using Pygame
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("O₂ Hockey")

# PlayerL class definition
# Represents the left player object and its behavior
class PlayerL(pg.sprite.Sprite):
    # Initialize the player attributes
    def __init__(self):
        super().__init__()  # Call the superclass constructor

        # Initialize player visuals (circle with color and position)
        self.radius = 40
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, BLUE, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()

        # Set initial position and movement attributes
        self.rect.centerx, self.rect.centery = WIDTH * 1/8, HEIGHT // 2
        self.max_speed = 6
        self.acceleration = 0.5
        self.deceleration = 0.2
        self.change_x = 0
        self.change_y = 0

        # Initialize player score
        self.score = 0

    # Methods to control player movement and behavior
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
        # Decelerate the player gradually to a stop
        if self.change_x > 0:
            self.change_x = max(self.change_x - self.deceleration, 0)
        elif self.change_x < 0:
            self.change_x = min(self.change_x + self.deceleration, 0)
            
        if self.change_y > 0:
            self.change_y = max(self.change_y - self.deceleration, 0)
        elif self.change_y < 0:
            self.change_y = min(self.change_y + self.deceleration, 0)

    def update(self):
        # Update player position based on current speed
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Keep the player within the screen boundaries
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH / 2:
            self.rect.right = WIDTH / 2

# PlayerR class definition (similar structure as PlayerL)
# Represents the right player object and its behavior
class PlayerR(pg.sprite.Sprite):
    # Initialize the player attributes
    def __init__(self):
        super().__init__()  # Call the superclass constructor

        # Initialize player visuals (circle with color and position)
        self.radius = 40
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()

        # Set initial position and movement attributes
        self.rect.centerx, self.rect.centery = WIDTH * 7/8, HEIGHT // 2
        self.max_speed = 6
        self.acceleration = 0.5
        self.deceleration = 0.2
        self.change_x = 0
        self.change_y = 0

        # Initialize player score
        self.score = 0

    # Methods to control player movement and behavior
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
        # Decelerate the player gradually to a stop
        if self.change_x > 0:
            self.change_x = max(self.change_x - self.deceleration, 0)
        elif self.change_x < 0:
            self.change_x = min(self.change_x + self.deceleration, 0)
            
        if self.change_y > 0:
            self.change_y = max(self.change_y - self.deceleration, 0)
        elif self.change_y < 0:
            self.change_y = min(self.change_y + self.deceleration, 0)

    def update(self):
        # Update player position based on current speed
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Keep the player within the screen boundaries
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < WIDTH / 2:
            self.rect.left = WIDTH / 2
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# GoalR class definition
# Represents the goal on the right side of the screen
class GoalR(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Create a visual representation for the goal (black rectangle)
        self.image = pg.Surface((15, 130))
        self.image.fill(BLACK)

        # Set the position of the goal on the right side of the screen
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.centery = HEIGHT // 2

# GoalL class definition (similar structure as GoalR)
# Represents the goal on the left side of the screen
class GoalL(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Create a visual representation for the goal (black rectangle)
        self.image = pg.Surface((15, 130))
        self.image.fill(BLACK)

        # Set the position of the goal on the left side of the screen
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.centery = HEIGHT // 2

# CircleinMiddle class definition
# Represents a circle in the middle of the screen
class CircleinMiddle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Create a visual representation for the circle (black circle)
        self.radius = 50
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)

        # Set the position of the circle in the center of the screen
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

# CircleinMiddleInside class definition (similar structure as CircleinMiddle)
# Represents a smaller circle inside the middle circle
class CircleinMiddleInside(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Create a visual representation for the circle (white circle)
        self.radius = 40
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)

        # Set the position of the circle in the center of the screen
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

# MiddleLine class definition
# Represents the middle line dividing the screen
class MiddleLine(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Create a visual representation for the middle line (black line)
        self.image = pg.Surface((15, 1080), pg.SRCALPHA)
        self.image.fill(BLACK)

        # Set the position of the middle line in the center of the screen
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

# Ball class definition
# Represents the ball object and its behavior
class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Create a visual representation for the ball (black circle)
        self.radius = 17
        self.diameter = self.radius * 2
        self.image = pg.Surface((self.diameter, self.diameter), pg.SRCALPHA)
        pg.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)

        # Initial speed and position
        self.ball_speed_x = 0
        self.ball_speed_y = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 4
        self.rect.centery = HEIGHT // 2
        self.deceleration = 0.01  # Deceleration rate

    def update(self):
        # Update ball position based on current speed
        if self.ball_speed_x < 0:  # moving left
            self.ball_speed_x = min(self.ball_speed_x + self.deceleration, 0)
        if self.ball_speed_x > 0:  # moving right
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
        # Adjust the ball speed whenever it collides with the player so that it simulates bouncing off the player with energy transfer from player
        self.rect.left = player.rect.right
        if self.ball_speed_x == 0:
            self.ball_speed_x = player.change_x + 3
        else:
            self.ball_speed_x = player.change_x + 3
        self.ball_speed_y = player.change_y

    def hittop(self, player):
        # Adjust the ball speed whenever it collides with the player so that it simulates bouncing off the player with energy transfer from player
        self.rect.bottom = player.rect.top
        if self.ball_speed_y == 0:
            self.ball_speed_y = player.change_y - 3
        else:
            self.ball_speed_y = player.change_y - 3
        self.ball_speed_x = player.change_x

    def hitbottom(self, player):
        # Adjust the ball speed whenever it collides with the player so that it simulates bouncing off the player with energy transfer from player
        self.rect.top = player.rect.bottom
        if self.ball_speed_y == 0:
            self.ball_speed_y = player.change_y + 3
        else:
            self.ball_speed_y = player.change_y + 3
        self.ball_speed_x = player.change_x

    def hitleft(self, player):
        # Adjust the ball speed whenever it collides with the player so that it simulates bouncing off the player with energy transfer from player
        self.rect.right = player.rect.left
        if self.ball_speed_x == 0:
            self.ball_speed_x = player.change_x - 3
        else:
            self.ball_speed_x = player.change_x - 3
        self.ball_speed_y = player.change_y

# Reset functions for positions and scores once someone scores
def reset_mainpositions(playerleft, playerright, goalright, goalleft):
    playerleft.rect.centerx, playerleft.rect.centery = WIDTH * 1/8, HEIGHT // 2
    playerleft.change_x, playerleft.change_y = 0, 0

    playerright.rect.centerx, playerright.rect.centery = WIDTH * 7/8, HEIGHT // 2
    playerright.change_x, playerright.change_y = 0, 0
    
    goalright.rect.right, goalright.rect.centery = WIDTH, HEIGHT // 2
    goalleft.rect.left, goalleft.rect.centery = 0, HEIGHT // 2
    
def reset_ballpositionrightscore(ball):
    ball.rect.centerx = WIDTH // 4
    ball.rect.centery = HEIGHT // 2
    ball.ball_speed_x, ball.ball_speed_y = 0, 0

def reset_ballpositionleftscore(ball):
    ball.rect.centerx = WIDTH * 0.75
    ball.rect.centery = HEIGHT // 2
    ball.ball_speed_x, ball.ball_speed_y = 0, 0


def start():
    pg.init()

    # Game state variables
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # Font definitions for text display
    font = pg.font.SysFont("Futura", 56)
    font2 = pg.font.SysFont("Futura", 150)
    font3 = pg.font.SysFont("Futura", 45)
    font4 = pg.font.SysFont("Futura", 70)

    # Render texts for game start instructions
    title = font2.render("Chiune's O2 Hockey", True, BLACK)
    playerleftcontrols = font.render("PLAYER LEFT (BLUE) CONTROLS - MOVE LEFT: 'A', MOVE RIGHT: 'D', MOVE DOWN: 'S', MOVE UP: 'W'", True, BLACK)
    playerrightcontrols = font3.render("PLAYER RIGHT (RED) CONTROLS - MOVE LEFT: 'left' key, MOVE RIGHT: 'right' key, MOVE DOWN: 'down' key, MOVE UP: 'up' key", True, BLACK)
    startcommand = font4.render("Press SPACEBAR to begin!", True, BLACK)

    # Font for displaying scores
    scorefont = pg.font.SysFont("Futura", 1100)

    # Initialize game objects
    playerleft = PlayerL()
    playerright = PlayerR()
    goalright = GoalR()
    goalleft = GoalL()
    ball = Ball()
    circleinmiddle = CircleinMiddle()
    middleline = MiddleLine()
    circleinmiddleinside = CircleinMiddleInside()

    # Create sprite groups for rendering and collision detection
    all_sprites = pg.sprite.Group()
    ball_sprites = pg.sprite.Group()
    goalleft_sprites = pg.sprite.Group()
    goalright_sprites = pg.sprite.Group()

    # Add objects to sprite groups
    all_sprites.add(middleline, circleinmiddle, circleinmiddleinside, playerleft, playerright, goalright, goalleft, ball)
    goalleft_sprites.add(goalleft)
    goalright_sprites.add(goalright)
    ball_sprites.add(ball)

    # Display game start instructions until SPACEBAR is pressed
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    waiting = False

        # Display start screen elements
        screen.fill(WHITE)
        screen.blit(title, (450, 300))
        screen.blit(playerleftcontrols, (20, 500))
        screen.blit(playerrightcontrols, (30, 600 ))
        screen.blit(startcommand, (630, 800))
        pg.display.flip()

    # Main game loop
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # Player controls
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
        
        # Check for collisions with goals
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

        # Check for collisions with players and ball
        if pg.sprite.collide_circle(playerleft, ball):
            if playerleft.rect.right > ball.rect.left and playerleft.rect.centerx < ball.rect.left:
                ball.hitright(playerleft)
            if playerleft.rect.left < ball.rect.right and playerleft.rect.centerx > ball.rect.right:
                ball.hitleft(playerleft)
            if playerleft.rect.bottom > ball.rect.top and playerleft.rect.centery < ball.rect.top:
                ball.hitbottom(playerleft)
            if playerleft.rect.top < ball.rect.bottom and playerleft.rect.centery > ball.rect.bottom:
                ball.hittop(playerleft)
            
        if pg.sprite.collide_circle(playerright, ball):
                if playerright.rect.right>ball.rect.left and playerright.rect.centerx <ball.rect.left:
                    ball.hitright(playerright)
                if playerright.rect.left<ball.rect.right and playerright.rect.centerx > ball.rect.right:
                    ball.hitleft(playerright)
                if playerright.rect.bottom > ball.rect.top and playerright.rect.centery < ball.rect.top:
                    ball.hitbottom(playerright)
                if playerright.rect.top < ball.rect.bottom and playerright.rect.centery > ball.rect.bottom:
                    ball.hittop(playerright)

        screen.fill(WHITE)

        scorel = scorefont.render(f"{playerright.score}", True, (0, 0, 255))
        scorer = scorefont.render(f"{playerleft.score}", True, (255, 0, 0))

        scorel.set_alpha(127)
        scorer.set_alpha(127)
        
        all_sprites.draw(screen)

        scorel_rect = scorel.get_rect()
        scorer_rect = scorer.get_rect()

        scorel_pos = (WIDTH * 0.22 - scorel_rect.width // 2, HEIGHT // 2 - scorel_rect.height // 2)
        scorer_pos = (WIDTH * 0.78 - scorer_rect.width // 2, HEIGHT // 2 - scorer_rect.height // 2)

        screen.blit(scorel, scorel_pos)
        screen.blit(scorer, scorer_pos)
    
        all_sprites.draw(screen)

        pg.display.flip()

        # --- Tick the Clock
        clock.tick(75)  # 75 fps

def main():
    start()


if __name__ == "__main__":
    main()