import pygame
 
pygame.init()
 
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill((255, 0, 255))  # Background color
 
    # Draw patterns
    pygame.draw.rect(screen, (200, 0, 200), (300, 200, 400, 300))  # Central rectangle
    pygame.draw.circle(screen, (255, 100, 200), (640, 360), 150)  # Overlapping circle
    pygame.draw.line(screen, (255, 200, 200), (300, 200), (700, 500), 10)  # Diagonal line
 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()