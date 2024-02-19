import os
import random
import pygame

class Cat(pygame.sprite.Sprite):
    def __init__(self, cat_folders, x, y):
        super().__init__()
        self.cat_type = random.choice(cat_folders)
        self.animations = self.load_animations(self.cat_type)
        self.current_animation = 'idle'
        self.image = self.animations[self.current_animation][0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.animation_index = 0
        self.animation_speed = 0.2
        self.frame_count = 0

    def load_animations(self, cat_type):
        animations = {'idle': [], 'itch': [], 'laying': [], 'licking': [], 'meow': [],
                      'run': [], 'sitting': [], 'sleeping': [], 'stretching': [], 'walk': []}
        for animation_name in animations.keys():
            full_path = os.path.join(cat_type)
            for file_name in os.listdir(full_path):
                if animation_name in file_name.lower():
                    image_path = os.path.join(full_path, file_name)
                    sprite_sheet = pygame.image.load(image_path).convert_alpha()
                    animations[animation_name] = self.load_frames_from_sheet(sprite_sheet)
        return animations

    def load_frames_from_sheet(self, sprite_sheet):
        frame_width, frame_height = 50, 50
        sheet_width, sheet_height = sprite_sheet.get_size()
        frames = []
        for y in range(0, sheet_height, frame_height):
            for x in range(0, sheet_width, frame_width):
                frame = sprite_sheet.subsurface((x, y, frame_width, frame_height))
                frames.append(frame)
        return frames

    def change_animation(self, animation):
        if animation in self.animations and self.animations[animation]:
            self.current_animation = animation
            self.animation_index = 0
            self.frame_count = 0

    def update(self):
        self.frame_count += self.animation_speed
        if self.frame_count >= len(self.animations[self.current_animation]):
            self.frame_count = 0
        self.animation_index = int(self.frame_count)
        self.image = self.animations[self.current_animation][self.animation_index]