from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen    
from telas import *

class Gerenciador(ScreenManager):
    def __init__(self, **kw):
        super().__init__(**kw)

class Mandiokito(App):
    def build (self):
        return Gerenciador()

if __name__ == '__main__':
    Mandiokito().run()