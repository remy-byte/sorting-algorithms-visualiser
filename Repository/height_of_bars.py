import random


class Height:

    def __init__(self):
        self.storing_heights = [random.randint(1, 400) for x in range(0, 29)]

    def set_random_heights(self):
        """
        Function that sets a randomized set of blocks.
        This can be changed at any time.
        """
        self.storing_heights = [random.randint(1, 400) for x in range(0, 29)]

    def return_the_list(self):
        """
        This function returns the list from the class 'Height'.
        """
        list = []
        for x in self.storing_heights:
            list.append(x)
        return list

    def __len__(self):
        """
        This function returns the length of the list.
        """
        return len(self.storing_heights)
