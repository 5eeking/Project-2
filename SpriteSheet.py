import pygame as py

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale):

        image = py.Surface((width, height))
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = py.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0, 0, 0))

        return image