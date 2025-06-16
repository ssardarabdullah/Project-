#2d car racing game in phyton 
#import paygame 
import random

# Initialize Pygame
#pygame.init()

 #Screen dimensions
WIDTH, HEIGHT = 400, 600
#win = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("2D Car Racing")

# Load images
#player_car = pygame.image.load("player.png")
#enemy_car = pygame.image.load("enemy.png")
#road = pygame.image.load("road.png")

# Resize images
#player_car = pygame.transform.scale(player_car, (50, 100))
#enemy_car = pygame.transform.scale(enemy_car, (50, 100))
#road = pygame.transform.scale(road, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)

# Clock
#clock = pygame.time.Clock()

# Player initial position
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120
player_speed = 5

# Enemy car
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_speed = 5

# Score
score = 0
#font = pygame.font.SysFont(None, 36)

def draw_window():
    win.blit(road, (0, 0))
    win.blit(player_car, (player_x, player_y))
    win.blit(enemy_car, (enemy_x, enemy_y))
    text = font.render(f"Score: {score}", True, WHITE)
    win.blit(text, (10, 10))
   # pygame.display.update()

# Main loop
run = True
while run:
    #clock.tick(60)  # 60 FPS

    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
          #  run = False

    # Key controls
    #keys = pygame.key.get_pressed()
   # if keys[pygame.K_LEFT] and player_x > 0:
       # player_x -= player_speed
    #if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
       # player_x += player_speed

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)
        score += 1
        enemy_speed += 0.2  # Increase difficulty

    # Collision detection
    #player_rect = pygame.Rect(player_x, player_y, 50, 100)
    #enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 100)

    #if player_rect.colliderect(enemy_rect)
        print("Game Over!")
        run = False

   # draw_window()

#pygame.quit()