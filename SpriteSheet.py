
# NOTE: Import Section
# Imports required modules for the file
import pygame as py

class SpriteSheet:
    def __init__(self, image) -> None:
        """
        Initializes the image for the sprite sheet.
        Parameters:
            image: Sprite sheet image used to get sprites/animations.
        """

        # NOTE: Image Initializer
        # Initializes the image.
        self.sheet = image

    def get_image(self, frame = 0, columns = 0, width = 128, height = 128, scale = 1, color = (0, 255, 0)) -> pygame.Surface:
        """
        Gets the image from the sprite sheet for an animation or sprite.
        Parameters:
            frame: Frame number for the frame of the image needed.
            columns: Number of columns in the image needed.
            width: Width of the image needed.
            height: Height of the image needed.
            scale: Scale of the image needed.
            color: Color of the image to get rid of the background.
        Returns:
            pygame.Surface: The image from the sprite sheet on a surface.
        """

        # NOTE: Column and Row Initializer
        # Initializes the column and row needed for the sprite images.
        column = frame
        row = 0
        if frame >=  columns:
            column = 0 + (frame - columns)
            row += 1

        # NOTE: Image Creator (Puts the image on a surface)
        # Creates a surface for the image and returns the image on it.
        image = py.Surface(size = (width, height))
        image.fill(color)
        image.blit(self.sheet, (0, 0), ((column * width), (row * height), width, height))
        image = py.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image