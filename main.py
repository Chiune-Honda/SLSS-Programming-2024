import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soccer Physics")

# Players
player1 = pygame.Rect(50, HEIGHT // 2 - 50, 50, 100)
player2 = pygame.Rect(WIDTH - 100, HEIGHT // 2 - 50, 50, 100)

# Ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed = [5, 5]

# Game loop
while True:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= 5
    if keys[pygame.K_s]:
        player1.y += 5
    if keys[pygame.K_UP]:
        player2.y -= 5
    if keys[pygame.K_DOWN]:
        player2.y += 5
    
    # Move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    
    # Ball collision with players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] *= -1
    
    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1

    # Draw players and ball
    pygame.draw.rect(screen, BLACK, player1)
    pygame.draw.rect(screen, BLACK, player2)
    pygame.draw.ellipse(screen, BLACK, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
