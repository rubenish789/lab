import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
x = 250
y = 250
r = 25
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if y + 20 + r <= screen_height:
                    y += 20
            elif event.key == pygame.K_UP:
                if y - 20 - r >= 0:
                    y -= 20 
            elif event.key == pygame.K_LEFT:
                if x - 20 - r >= 0:
                    x -= 20
            elif event.key == pygame.K_RIGHT:
                if x + 20 + r <= screen_width:
                    x += 20
    
    screen.fill((0, 0, 0))
    
    pygame.draw.circle(screen, (255, 0, 0),(x,y),r)
    
    
    pygame.display.update()
    clock.tick(60)