import pygame
import os
import random

from Cat import Cat

pygame.init()
screen = pygame.display.set_mode((1920, 1080))

# Assuming the cat directories are structured as 'Cat-1', 'Cat-2', etc., within the 'cats' folder.
cat_folders = [os.path.join('./cats', folder) for folder in os.listdir('./cats') if os.path.isdir(os.path.join('./cats', folder))]

all_cats = pygame.sprite.Group()
for x in range(262):  # Create 10 cat instances for demonstration
    cat = Cat(cat_folders, random.randint(0 + 50, 1920 - 50), random.randint(0+50, 1080-50))
    all_cats.add(cat)

# Game loop would go here
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_cats.update()

    screen.fill((0, 0, 0))
    all_cats.draw(screen)
    pygame.display.flip()

pygame.quit()