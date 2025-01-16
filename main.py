# Code by: Sidharth S (aka. SidTheLoser)
# I'll add comments and document this code later...

from sidengine.gameobject import CelestialBody, gameobjects_in_scene
from sidengine.app import App
from sidengine import colors
import pygame


GRAV_CONST = 1


class MyCelest(CelestialBody):
    def __init__(self, x: float, y: float, mass: int, color: tuple[int]):
        super().__init__(x, y, mass, color)

    def update(self):
        global myapp

        total_dx = total_dy = 0

        other:MyCelest
        for other in gameobjects_in_scene:
            if other != self and self.mass < 10 and other.mass >= self.mass:
                dist_x = other.x - self.x
                dist_y = other.y - self.y

                dist = (dist_x**2) + (dist_y**2) - ((self.mass+other.mass)**2)

                if dist != 0:
                    if dist_x != 0:
                        dir_x = dist_x / abs(dist_x)

                        total_dx += ((GRAV_CONST * other.mass) / dist) * dir_x

                    if dist_y != 0:
                        dir_y = dist_y / abs(dist_y)

                        total_dy += ((GRAV_CONST * other.mass) / dist) * dir_y

                if dist < (self.mass+other.mass)**2:
                    self.delete_me = True
                    if self.mass == other.mass:
                        other.delete_me = True

        if not self.delete_me:

            self.dx += total_dx
            self.dy += total_dy

            # if self.x < 0 or self.x > myapp.window_size[0]:
            #     self.dx *= -1
            #
            # if self.y < 0 or self.y > myapp.window_size[1]:
            #     self.dy *= -1

            self.x += self.dx
            self.y += self.dy


class MyApp(App):
    def __init__(self, flags=0):
        super().__init__(window_flags=flags)
        self.update_paused = True
        self.object_size = 1
        self.background = (10, 10, 10)

    def late_extra_functions(self):
        pygame.display.set_caption(
            f"Gravity Testing in Pygame | Paused: {
            int(self.update_paused)} | Obj c: {
            len(gameobjects_in_scene)} s:{self.object_size if self.object_size < 10 else 'Static'} | FPS: {
            round(self.clock.get_fps())}"
        )

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if self.object_size < 10:
                        gameobjects_in_scene.append(
                            MyCelest(x=mouse_x, y=mouse_y, mass=self.object_size, color=colors.RED)
                        )

                    else:
                        gameobjects_in_scene.append(
                            MyCelest(x=mouse_x, y=mouse_y, mass=self.object_size, color=colors.WHITE)
                        )

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.screen_drawover = not self.screen_drawover

                if event.key == pygame.K_ESCAPE:
                    self.update_paused = not self.update_paused

                if event.key == pygame.K_DELETE:
                    gameobjects_in_scene.clear()

                if event.key == pygame.K_0:
                    self.object_size = 10

                elif event.key == pygame.K_1:
                    self.object_size = 1

                elif event.key == pygame.K_2:
                    self.object_size = 2

                elif event.key == pygame.K_3:
                    self.object_size = 3

                elif event.key == pygame.K_4:
                    self.object_size = 4

                elif event.key == pygame.K_5:
                    self.object_size = 5

                elif event.key == pygame.K_6:
                    self.object_size = 6

                elif event.key == pygame.K_7:
                    self.object_size = 7

                elif event.key == pygame.K_8:
                    self.object_size = 8

                elif event.key == pygame.K_9:
                    self.object_size = 9


myapp = MyApp(flags=pygame.SCALED | pygame.RESIZABLE)

myapp.init()

myapp.run()