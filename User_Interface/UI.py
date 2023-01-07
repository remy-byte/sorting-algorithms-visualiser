import pygame

from Repository.repository_visualiser import Visualiser


class UserInterface(Visualiser):

    def __init__(self, sorting_heights, repository_heights):
        pygame.init()
        Visualiser.__init__(self)
        self.sorting_heights = sorting_heights
        self.repository_heights = repository_heights
        self.run = True
        self.number_of_comparations = 0
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.text = self.font.render("Press 'SPACE' to start visualising the algorithm!", True, (0, 0, 0),
                                     (255, 255, 255))
        self.text_2 = self.font.render("Total number of comparisons :" + str(self.number_of_comparations), True,
                                       (0, 0, 0), (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect2 = self.text_2.get_rect()
        self.textRect.center = (1000 // 2, 600 // 2 - 200)
        self.textRect2.center = (200, 20)

    def give_me_a_random_list(self):
        self.repository_heights.set_random_heights()
        list = self.repository_heights.return_the_list()
        return list

    def run_application(self):
        to_be_sorted = False
        initial_list = self.give_me_a_random_list()
        while self.run:

            pygame.time.delay(20)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        to_be_sorted = True

                self._screen.blit(self.text, self.textRect)

                if not to_be_sorted:

                    self._screen.fill((255, 255, 255))
                    self.sorting_heights.draw_rectangles(initial_list)
                    display_surface = pygame.display.get_surface()
                    display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))
                    self._screen.blit(self.text, self.textRect)
                    self.text_2 = self.font.render(
                        "Total number of comparisons of the previous run: " + str(self.number_of_comparations),
                        True, (0, 0, 0), (255, 255, 255))

                    self._screen.blit(self.text_2, self.textRect2)

                else:
                    self.number_of_comparations = self.sorting_heights.BubbleSort_then_visualise()
                    initial_list = self.give_me_a_random_list()
                    pygame.time.delay(10)
                    to_be_sorted = False

            pygame.display.update()
