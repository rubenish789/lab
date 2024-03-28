import pygame
import os

pygame.init()
screen = pygame.display.set_mode((100, 100))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

music_files = [
    'sounds/Imagine Dragons - Believer.mp3',
    'sounds/Imagine Dragons - Thunder.mp3',
    'sounds/Imagine Dragons - Whatever It Takes.mp3'
]

current_track = 0
pygame.mixer.music.load(music_files[current_track])


def play_music():
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    play_music()


def prev_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    play_music()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:
                    next_track()
            elif event.key == pygame.K_LEFT:
                    prev_track()

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
