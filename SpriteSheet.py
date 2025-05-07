import pygame as py

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, collumns, width, height, scale, color):

        collumn = frame
        row = 0

        if frame >=  collumns:
            collumn = 0 + (frame - collumns)
            row += 1

        image = py.Surface(size = (width, height))
        image.fill(color)
        image.blit(self.sheet, (0, 0), ((collumn * width), (row * height), width, height))
        image = py.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image