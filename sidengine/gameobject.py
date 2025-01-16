import pygame


class Empty: # the base game object that is used as the parent to all game objects
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

        self.delete_me = False

    def update(self):
        pass

    def draw(self, window:pygame.Surface):
        pass


class CelestialBody(Empty):
    def __init__(self, x:float, y:float, mass:int, color:tuple[int]):
        super().__init__(x, y)
        self.mass = mass
        self.color = color

        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, window:pygame.Surface):
        pygame.draw.circle(surface=window, color=self.color, center=(self.x, self.y), radius=self.mass)


gameobjects_in_scene = []

def clear_all_gameobjects():
    global gameobjects_in_scene

    gameobjects_in_scene = []