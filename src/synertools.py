""" Entry Point, used for testing """
from src.di.app_container import AppContainer
from src.ui.theme.color import GRAY, YELLOW

class Synertools:
    def __init__(self) -> None:
            print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
            self.container = AppContainer()

    def hello(self) -> None:
          print(f"Hello")