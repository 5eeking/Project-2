### File that runs the game and connects all required files ###

# NOTE: Import Section
# Imports required modules for the file
from Player import *
from Enemy import *
from Logic import *
from Upgrades import *
from SaveLoadSystem import SaveLoadSystem
import pygame as py
import random as rand

# Game class that creates the game and runs it.
class Game:
    def __init__(self, name, data) -> None:
        """
        Initializes the game and all the variables needed for the game.
        Parameters:
            name: Name of the game.
            data: Data of the game.
        """

        # NOTE: Game Initializer
        # Initializes the game.
        py.init()
        py.font.init()
        self.flags = py.RESIZABLE | py.SCALED
        self.screen = py.display.set_mode(size = (1550, 800), flags = self.flags)
        py.display.set_caption(name)
        self.clock = py.time.Clock()

        # Initializes game variables.
        self.running = True
        self.restart = False
        self.x = 0
        self.y = 0
        self.width = 1550
        self.height = 800

        # Initializes the save/load system.
        self.save_load_system = SaveLoadSystem(".txt", "gameData")

        # NOTE: Element Initializer (Player, Bullets, Enemies, Gun, etc.)
        # Initializes more game elements and sprites.
        self.display_scroll = [0, 0]
        self.counter1 = 0
        self.counter2 = 0
        self.round = 0
        self.round_start = True
        self.bullets = []
        self.enemies = []
        self.upgrades = []
        self.player = Player(x = self.width / 2, y = self.height / 2, width = 128, height = 128,
                             health = 100, damage = 5, points = 0)
        self.gun = Gun(x = 100, y = 100, width = 128, height = 128, shot = True)
        self.font = py.font.SysFont('Arial', 36)
        self.background = py.image.load(f"sprites{os.sep}grass.png").convert_alpha()
        self.background = py.transform.scale(self.background, (self.width, self.height))

        # Sets up the previous game data if there is any.
        if len(data[0]) > 0 and len(data[1]) > 0:
            self.set_up(data)

    def run(self) -> None:
        """
        Runs the game while running is True and uses all the logic and classes to make the game work correctly.
        Returns:
            None
        """

        # Runs the game until running is False.
        while self.running:

            # NOTE: Event Handler
            # Stops the game if the window is closed and saves game data.
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.save_load_system.save_game_data([[self.player.points, self.player.damage, self.player.health, self.player.health_max, self.player.protection], [self.round]], ["player_data", "game_data"])
                    self.running = False

            # NOTE: Background Display Section
            # Resets the background position at the right time.
            if self.y >= self.height or self.y <= -self.height:
                self.y = 0
            if self.x >= self.width or self.x <= -self.width:
                self.x = 0

            # Displays the background in a 3x3 grid.
            self.screen.blit(self.background, (self.x, self.y))
            self.screen.blit(self.background, (self.x - self.width, self.y))
            self.screen.blit(self.background, (self.x + self.width, self.y))
            self.screen.blit(self.background, (self.x, self.y - self.height))
            self.screen.blit(self.background, (self.x, self.y + self.height))
            self.screen.blit(self.background, (self.x - self.width, self.y - self.height))
            self.screen.blit(self.background, (self.x + self.width, self.y + self.height))
            self.screen.blit(self.background, (self.x + self.width, self.y - self.height))
            self.screen.blit(self.background, (self.x - self.width, self.y + self.height))


            # NOTE: Player Movement Section
            # Initializes the movement variables.
            keys = py.key.get_pressed()
            mouse_pos = py.mouse.get_pos()
            self.player.action = get_direction(self.player.get_player_pos(), mouse_pos)
            diagonal_speed = 0.8
            default_speed = 1

            # Moves the "Player" when the WASD keys are pressed.
            if keys[py.K_a] and keys[py.K_s]:
                self.move(x_move = -diagonal_speed * (self.round / 3), y_move = diagonal_speed * (self.round / 3))
            elif keys[py.K_a] and keys[py.K_w]:
                self.move(x_move = -diagonal_speed * (self.round / 3), y_move = -diagonal_speed * (self.round / 3))
            elif keys[py.K_d] and keys[py.K_s]:
                self.move(x_move = diagonal_speed * (self.round / 3), y_move = diagonal_speed * (self.round / 3))
            elif keys[py.K_d] and keys[py.K_w]:
                self.move(x_move = diagonal_speed * (self.round / 3), y_move = -diagonal_speed * (self.round / 3))
            else:
                if keys[py.K_a]:
                    self.move(x_move = -default_speed * (self.round / 3))
                if keys[py.K_d]:
                    self.move(x_move = default_speed * (self.round / 3))
                if keys[py.K_w]:
                    self.move(y_move = -default_speed * (self.round / 3))
                if keys[py.K_s]:
                    self.move(y_move = default_speed * (self.round / 3))

            # NOTE: Bullet Spawn Section
            # Creates a bullet when the mouse button is pressed and appends it to bullets list, and stops it from shooting a ton of bullets
            if py.mouse.get_pressed()[0] and self.gun.shot:
                self.gun.shot = False
                temp_bullet = Bullet(self.gun.x, self.gun.y, 'black', 5,
                                     get_unit_vector(self.player.get_player_pos(), py.mouse.get_pos()))
                self.bullets.append(temp_bullet)

            # Makes it able to shoot again
            elif not py.mouse.get_pressed()[0]:
                self.gun.shot = True

            # NOTE: Bullet Movement and Enemy Collide Section
            # Loops through all the bullets and moves them, Removing them from the list when they leave the screen or touch an enemy
            for bullet in self.bullets:
                bullet.update(self.screen)

                # Checks collision and removes enemies based on damage and enemy health, also adds points for the player
                for enemy in self.enemies:
                    if check_collide((enemy.x - self.display_scroll[0], enemy.y - self.display_scroll[1]),
                                     get_circular_position(bullet.get_bullet_pos(), (enemy.x - self.display_scroll[0], enemy.y - self.display_scroll[1]), 10),
                                    30):
                        if enemy.enemy_damage(self.player.damage):
                            try:
                                self.enemies.remove(enemy)
                            except ValueError:
                                print("Could not remove enemy.")
                            self.player.points += enemy.point_amount
                        try:
                            self.bullets.remove(bullet)
                        except ValueError:
                            print('Could not remove bullet.')

                if (bullet.x + 64 < 0 or bullet.x > self.width) or (bullet.y + 64 < 0 or bullet.y > self.height):
                    try:
                        self.bullets.remove(bullet)
                    except ValueError:
                        print('Could not remove bullet.')

            # NOTE: Enemy Spawning Section
            # Spawns enemies based on the round getting incrementally more difficult.
            if len(self.enemies) < self.round * 3 and self.round_start:

                # Spawns an enemy every 1.5 seconds
                self.counter1 += 1
                if self.counter1 >= 150:
                    # Chooses a random enemy to spawn and creates an object for it
                    rand_num = rand.randint(1, 3)
                    temp_enemy = None
                    if rand_num == 1: temp_enemy = Enemy(0, 0, 1 * (self.round / 3), 128, 128, "Monster", 40 * (self.round / 3), 16 * (self.round / 3), 10 * self.round, self.display_scroll,
                                                        self.screen)
                    if rand_num == 2: temp_enemy = Enemy(0, 0, 1.2 * (self.round / 3), 128, 128, "Skeleton", 30 * (self.round / 3), 10 * (self.round / 3), 12 * self.round, self.display_scroll,
                                                        self.screen)
                    if rand_num == 3: temp_enemy = Enemy(0, 0, 0.7 * (self.round / 3), 128, 128, "Hero", 60 * (self.round / 3), 24 * (self.round / 3), 20 * self.round, self.display_scroll,
                                                        self.screen)
                    self.enemies.append(temp_enemy)
                    self.counter1 = 0
            else:
                self.round_start = False

            # Increments the round when all enemies are killed.
            if len(self.enemies) == 0 and not self.round_start:
                self.round += 1
                self.round_start = True

            # NOTE: Enemy Update and Damaging Section
            # Checks a collision of the enemy and player and deducts health and points
            if len(self.enemies) > 0:
                for enemy in self.enemies:
                    enemy.update(self.screen, self.display_scroll)
                    enemy.move(get_unit_vector(enemy.get_enemy_pos(), (self.player.x + self.display_scroll[0], self.player.y + self.display_scroll[1])), (self.player.x + self.display_scroll[0], self.player.y + self.display_scroll[1]))
                    if check_collide((self.player.x + self.display_scroll[0], self.player.y + self.display_scroll[1]),
                                    get_circular_position(enemy.get_enemy_pos(), (self.player.x + self.display_scroll[0], self.player.y + self.display_scroll[1]), 30),
                                    30):
                        self.enemies.remove(enemy)
                        self.player.points = self.player.points - 10 if self.player.points >= 10 else 0
                        self.running = self.player.player_damage(enemy.damage)
                        if not self.running:
                            self.restart = True
                            try:
                                os.remove(f"gameData{os.sep}player_data.txt")
                                os.remove(f"gameData{os.sep}game_data.txt")
                            except FileNotFoundError:
                                print("Files do not exist.")

            # NOTE: Upgrade Spawning Section
            # Spawns upgrades for the player around the map every 10 seconds.
            self.counter2 += 1
            if self.counter2 >= 1000:

                rand_upg = rand.randint(0, 100)
                temp_upgrade = None
                if rand_upg < 50:
                    temp_upgrade = Upgrades(rand.randint(-150, self.width + 150), rand.randint(-150, self.height + 150),
                                            32, 32, "Rand")
                elif rand_upg < 66:
                    temp_upgrade = Upgrades(rand.randint(-150, self.width + 150), rand.randint(-150, self.height + 150),
                                            32, 32, "Damage")
                elif rand_upg < 83:
                    temp_upgrade = Upgrades(rand.randint(-150, self.width + 150), rand.randint(-150, self.height + 150),
                                            32, 32, "Health")
                else:
                    temp_upgrade = Upgrades(rand.randint(-150, self.width + 150), rand.randint(-150, self.height + 150),
                                            32, 32, "Protection")

                self.upgrades.append(temp_upgrade)
                self.counter2 = 0

            # NOTE: Upgrade Update and Displaying Section
            # Updates and checks upgrade collision to collect the upgrade and remove it from the list.
            if len(self.upgrades) > 0:
                for upgrade in self.upgrades:
                    upgrade.update(self.screen, self.display_scroll)
                    if check_collide((self.player.x + self.display_scroll[0], self.player.y + self.display_scroll[1]),
                                    get_circular_position((upgrade.x, upgrade.y), (
                                    self.player.x + self.display_scroll[0], self.player.y + self.display_scroll[1]), 30),
                                    30):
                        self.upgrades.remove(upgrade)
                        upgrade.collect(self.player)

            # NOTE: Player and Gun Update Section
            # Displays the player, gun, enemy counter, round counter, and moves the gun.
            self.player.update(self.screen)
            self.gun.update(self.screen, self.player.get_player_pos())
            enemy_counter_surface = self.font.render(f'Enemies Left: {len(self.enemies)}', True, 'black')
            self.screen.blit(enemy_counter_surface, (20, 40))
            round_counter_surface = self.font.render(f'Round: {self.round}', True, 'black')
            self.screen.blit(round_counter_surface, (20, 5))
            # Moves the gun around the player.
            self.gun.x, self.gun.y = get_circular_position((self.player.x, self.player.y),
                                                           py.mouse.get_pos(), 60)

            # Displays everything on the screen.
            py.display.flip()

    def set_up(self, data) -> None:
        """
        Sets up the previous game data for the player so they can continue playing.
        Parameters:
            data: Contains all the game data.
        Returns:
             None
        """

        player_data = data[0]
        game_data = data[1]

        self.player.points = player_data[0]
        self.player.damage = player_data[1]
        self.player.health = player_data[2]
        self.player.health_max = player_data[3]
        self.player.protection = player_data[4]

        self.round = game_data[0]

    def move(self, x_move = None, y_move = None) -> None:
        """
        Moves the "Player" by changing the display scroll which moves all other sprites other than the player to make
        it look like it is moving.
        Parameters:
            x_move: x coordinate of the movement.
            y_move: y coordinate of the movement.
        Returns:
             None
        """

        # NOTE: Player Movement Section
        # Changes the display scroll, background, and bullets x values.
        if x_move is not None:
            self.display_scroll[0] += x_move
            self.x -= x_move
            for bullet in self.bullets:
                bullet.x -= x_move

        # Changes the display scroll, background, and bullets y values.
        if y_move is not None:
            self.display_scroll[1] += y_move
            self.y -= y_move
            for bullet in self.bullets:
                bullet.y -= y_move