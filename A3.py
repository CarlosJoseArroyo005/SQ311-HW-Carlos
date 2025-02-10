import pygame

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Horizontal Movement")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

agent_x = 100
agent_y = HEIGHT // 2
velocity = 0
acceleration = 0.5
friction = 0.1
max_speed = 5
agent_size = 20

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity -= acceleration
    if keys[pygame.K_RIGHT]:
        velocity += acceleration

    if velocity > 0:
        velocity -= friction
    elif velocity < 0:
        velocity += friction

    if abs(velocity) < friction:
        velocity = 0  
    velocity = max(-max_speed, min(max_speed, velocity))

    agent_x += velocity

    if agent_x > WIDTH:
        agent_x = 0
    elif agent_x < 0:
        agent_x = WIDTH

    pygame.draw.rect(screen, BLUE, (agent_x, agent_y, agent_size, agent_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()