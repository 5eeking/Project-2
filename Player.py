### File to create the player ###

### Sprites obtained from, https://rgsdev.itch.io/hand-drawn-square-characters-animated-8-directions-top-down-free-cc0 ###

# NOTE: Import Section
# Imports required modules for the file
import pygame as py
from SpriteSheet import SpriteSheet
from HealthBar import HealthBar
import math
import os

# Player class to create player entities.
class Player:
    ANIMATION_COOLDOWN = 175
    def __init__(self, x, y, width, height, health, damage, points) -> None:
        """
        Initializes the required variables and sprites for the player.
        Parameters:
            x: x position of the player.
            y: y position of the player.
            width: width of the player.
            height: height of the player.
            health: health of the player.
            damage: damage the player does.
            points: points for the player.
        """

        # NOTE: Player/Animation Initializer
        # Initializes the variables for the player that let it interact in the game.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.health_max = health
        self.damage = damage
        self.protection = 0
        self.points = points
        self.playerBar = HealthBar(0, 0, 0, 0, 'green')
        py.font.init()
        self.font = py.font.SysFont('Arial', 36)

        # Initializes the animation of the player sprite.
        self.sprite_sheet_image = py.image.load(f"sprites{os.sep}base_character.png").convert_alpha()
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)
        self.animation_list = []
        self.animation_steps = [2, 2, 2, 2, 2, 2, 2, 1, 2]
        # 0 or 1 = s, 2 = s+d, 4 or 5 or 6 = a or d or w, 8 = w+d or w+a, 3 = s+a
        self.action = 0
        self.last_update = py.time.get_ticks()
        self.frame = 0
        step_counter = 0
        for animation in self.animation_steps:
            temp_list = []
            for _ in range(animation):
                temp_list.append(self.sprite_sheet.get_image(step_counter, 8, self.width, self.height, 1, (0, 255, 0)))
                step_counter += 1
            self.animation_list.append(temp_list)
        self.animation_list[3] = [py.transform.flip(self.animation_list[2][x], True, False) for x in range(len(self.animation_list[2]))]

    def player_damage(self, amount) -> bool:
        """
        Decreases the player health depending on the enemy and the players protection stat.
        Parameters:
            amount: amount of damage the player takes.
        Returns:
             bool: True or false depending on the players death.
        """

        # NOTE: Player Damaging and Death Section
        # Damages the player and determines the death of the player.
        self.health = self.health - (amount - self.protection) if amount - self.protection > 0 else self.health
        if self.health <= 0:
            print(f'\nYOU DIED WITH A SCORE OF {self.points}')
            return False
        else:
            return True

    def get_player_pos(self) -> tuple:
        """
        Returns the current position of the player.
        Returns:
            tuple: The position of the player.
        """

        # NOTE: Player Position Return Section
        # Returns the players position.
        return self.x, self.y

    def update(self, display) -> None:
        """
        Updates the players animation and displays it.
        Parameters:
            display: pygame display object.
        Returns:
            None
        """

        # NOTE: Cycles and Displays Animation Section
        # Displays the player, health bar, and point text on the screen.
        current_time = py.time.get_ticks()
        if current_time - self.last_update > self.ANIMATION_COOLDOWN:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0
        display.blit(self.animation_list[self.action][self.frame], (self.x - 64, self.y - 64))
        self.playerBar.update(display, self.get_player_pos(), self.health, self.health_max)
        counter_surface = self.font.render(f'Score: {self.points}', True, 'black')
        display.blit(counter_surface, (display.get_width() / 2, 5))

# Gun class to create the gun object.
class Gun:
    def __init__(self, x, y, width, height, shot) -> None:
        """
        Initializes the guns required variables and sprite.
        Parameters:
            x: x position of the gun.
            y: y position of the gun.
            width: width of the gun.
            height: height of the gun.
            shot: whether the gun was shot or not.
        """

        # NOTE: Gun Initializer
        # Initializes the gun variables and the sprite of the gun.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shot = shot
        self.gun_sprite = SpriteSheet(py.image.load(f"sprites{os.sep}gun.png").convert_alpha()).get_image(0, 1, self.width, self.height, 1, (0, 255, 0))

    def update(self, display, player_pos) -> None:
        """
        Updates the guns position around the player and displays it.
        Parameters:
            display: pygame display object.
            player_pos: the players position.
        Returns:
            None
        """

        # NOTE: Gun Rotation and Display Section
        # Updates the guns position and displays it.
        mouse_pos = py.mouse.get_pos()
        x_pos, y_pos = mouse_pos[0] - player_pos[0], -(mouse_pos[1] - player_pos[1])
        angle = math.degrees(math.atan2(y_pos, x_pos))
        gun = py.transform.rotate(self.gun_sprite, angle)
        gun_rect = gun.get_rect(center = (self.x, self.y))
        display.blit(gun, gun_rect)

# Bullet class to create bullet objects.
class Bullet:
    def __init__(self, x, y, width, height, unit_vector) -> None:
        """
        Initializes the bullets required variables and sprite.
        Parameters:
            x: x position of the bullet.
            y: y position of the bullet.
            width: width of the bullet.
            height: height of the bullet.
            unit_vector: unit vector of the bullet (Also known as speed and direction).
        """

        # NOTE: Bullet Initializer
        # Initializes the bullets variables and sprite.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.unit_vector = unit_vector
        self.bullet_sprite = SpriteSheet(py.image.load(f"sprites{os.sep}bullet.png").convert_alpha()).get_image(0, 1, 128,
                                                                                                           128, 1,
                                                                                                           (0, 255, 0))

    def get_bullet_pos(self) -> tuple:
        """
        Returns the current position of the bullet.
        Returns:
            tuple: The position of the bullet.
        """

        # NOTE: Bullet Position Return Section
        # Returns the current position of the bullet.
        return self.x, self.y

    def update(self, display) -> None:
        """
        Updates the bullet position and displays it.
        Parameters:
            display: pygame display object.
        Returns:
            None
        """

        # NOTE: Bullet Movement and Display Section
        # Updates the bullet position and displays it.
        display.blit(self.bullet_sprite, (self.x - 64, self.y - 64))
        self.x, self.y = self.x + self.unit_vector[0] * 3, self.y + self.unit_vector[1] * 3
