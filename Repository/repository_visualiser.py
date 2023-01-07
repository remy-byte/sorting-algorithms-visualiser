import pygame


class Visualiser:

    def __init__(self):
        """
        Initialising the main components of the package.
        """
        pygame.init()
        self.window_display_size = (1000, 600)
        self.color_of_rectangles = (41, 36, 33)
        self.width_of_each_bar = 40
        self._screen = pygame.display.set_mode(self.window_display_size)
        pygame.display.set_caption("Sorting Algorithm Visualiser")
        self.initial_pos_y = 40
        self.initial_pos_x = 42



