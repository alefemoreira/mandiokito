from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.app import App

class TelaInicial(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class Registrar(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current='Tela_Inicial'
            return True
    
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)


class Apagar(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current='Tela_Inicial'
            return True
    
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

class Atualizar(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current='Tela_Inicial'
            return True
    
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)