
# NOTE: Import Section
# Imports required modules for the file
import pygame as py

# Health bar class to create health bars for each entity.
class HealthBar:

    def __init__(self, x1, x2, y1, y2, color) -> None:
        """
        Initializes the health bar values.
        Parameters:
             x1: X start of the bar.
             x2: X end of the bar.
             y1: Y start of the bar.
             y2: Y end of the bar.
             color: Color of the bar.
        """

        # NOTE: Health Bar Initializer
        # Initializes all the required values to create the health bar.
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color

    def update(self, display, object_pos, health, health_max) -> None:
        """
        Updates the health bar and displays it.
        Parameters:
            display: Screen display.
            object_pos: Position of the entity.
            health: Health value.
            health_max: Max health value.
        Returns:
            None
        """

        # NOTE: Health Bar Display Section
        # Displays the health bar onto the screen using the health values provided.
        self.x1, self.y1, self.x2, self.y2 = object_pos[0] - 25, object_pos[1] - 35, (
                    ((object_pos[0] + 25) - (object_pos[0] - 25)) * (health / health_max)) + (object_pos[0] - 25), \
                                             object_pos[1] - 35
        py.draw.line(display, 'black', (self.x1 - 1, self.y1), (object_pos[0] + 26, object_pos[1] - 35), width=10)
        py.draw.line(display, self.color, (self.x1, self.y1), (self.x2, self.y2), width=6)