from Repository.height_of_bars import Height
from Repository.repository_visualiser import Visualiser
from Service.Sorting_the_heights import ServiceSorting
from User_Interface.UI import UserInterface

if __name__ == "__main__":
    repository_visualiser = Visualiser()
    heights = Height()
    service_heights = ServiceSorting(heights)
    UI = UserInterface(service_heights, heights)
    UI.run_application()
