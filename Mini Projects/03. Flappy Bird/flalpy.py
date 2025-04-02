import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)

# Load Images
BACKGROUND_IMG = pygame.image.load(r"c:\Users\pc\Downloads\bg_5.png")
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))
BIRD_IMG = pygame.image.load(r"c:\Users\pc\Downloads\flappy-bird-character-0l5qb71pe8ktfoa9.png")
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (40, 30))
PIPE_IMG = pygame.image.load(r"c:\Users\pc\Downloads\Mario_pipe.png")
PIPE_IMG = pygame.transform.scale(PIPE_IMG, (PIPE_WIDTH, HEIGHT))

# Setup Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Bird Class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.image = BIRD_IMG
    
    def flap(self):
        self.velocity = FLAP_STRENGTH
    
    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT
    
    def draw(self):
        screen.blit(self.image, (self.x, int(self.y)))

# Pipe Class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.image = PIPE_IMG
    
    def move(self):
        self.x -= PIPE_SPEED
    
    def draw(self):
        screen.blit(self.image, (self.x, self.height - HEIGHT))
        screen.blit(pygame.transform.flip(self.image, False, True), (self.x, self.height + PIPE_GAP))
    
    def collide(self, bird):
        if (bird.x + 40 > self.x and bird.x < self.x + PIPE_WIDTH):
            if bird.y < self.height or bird.y + 30 > self.height + PIPE_GAP:
                return True
        return False

# Game Loop
bird = Bird()
pipes = [Pipe(WIDTH + i * 200) for i in range(3)]
score = 0
running = True

while running:
    screen.blit(BACKGROUND_IMG, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.flap()
    
    bird.move()
    bird.draw()
    
    for pipe in pipes:
        pipe.move()
        pipe.draw()
        if pipe.collide(bird):
            running = False
        if pipe.x < -PIPE_WIDTH:
            pipes.remove(pipe)
            pipes.append(Pipe(WIDTH))
            score += 1
    
    # Display Score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
