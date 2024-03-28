import pygame
import datetime

pygame.init()

screen= pygame.display.set_mode((500,400))
clock = pygame.time.Clock()

main = pygame.image.load('images/mainclock.png').convert_alpha()
left = pygame.image.load('images/leftarm.png').convert_alpha()
right = pygame.image.load('images/rightarm.png').convert_alpha()

running = True

main = pygame.transform.scale(main,(500,400))
left = pygame.transform.scale(left,(50,480))
right = pygame.transform.scale(right,(500,450))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill('White')
    current_time = datetime.datetime.now()
    minute = current_time.minute*6*-1
    second = current_time.second*6*-1

    rotate_left = pygame.transform.rotate(left,second)
    rotate_right = pygame.transform.rotate(right,minute)

    screen.blit(main,main.get_rect(center = screen.get_rect().center))
    screen.blit(rotate_left,rotate_left.get_rect(center = screen.get_rect().center))
    screen.blit(rotate_right,rotate_right.get_rect(center = screen.get_rect().center))
    
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
