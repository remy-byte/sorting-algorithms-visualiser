"""
This class mainly contains the principal method in which the blocks will be sorted and drawing_function.
In this example, I'll select bubble sort as the main sorting method for the blocks.
"""
import pygame

from Repository.repository_visualiser import Visualiser


class ServiceSorting(Visualiser):

    def __init__(self, heights_values):
        Visualiser.__init__(self)
        self.heights_values = heights_values
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.text = self.font.render("Sorting...", True, (0, 0, 0), (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (1000 // 2, 600 // 2 - 200)

    def BubbleSort_then_visualise(self):
        list_to_be_sorted = self.heights_values.return_the_list()
        list_length = len(list_to_be_sorted)
        number_of_comparasions = 0

        '''
        You can paste here any sort method you'd like to visualise. Also depending on the sorting method you may 
        change the delay setting in order to have a more detailed visualisation. 
        '''
        for i in range(list_length):
            for j in range(0, list_length - i - 1):
                if list_to_be_sorted[j] > list_to_be_sorted[j + 1]:
                    number_of_comparasions += 1
                    list_to_be_sorted[j], list_to_be_sorted[j + 1] = list_to_be_sorted[j + 1], list_to_be_sorted[j]

                self._screen.fill((255, 255, 255))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                self.draw_rectangles(list_to_be_sorted)
                display_surface = pygame.display.get_surface()
                display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))
                self._screen.blit(self.text, self.textRect)
                pygame.time.delay(15)
                pygame.display.update()
        return number_of_comparasions

    def draw_rectangles(self, list_of_heights):
        for i in range(0, len(list_of_heights)):
            pygame.draw.rect(self._screen, self.color_of_rectangles,
                             pygame.Rect(self.initial_pos_x + 31 * i, self.initial_pos_y, self.width_of_each_bar - 10,
                                         list_of_heights[i]))
