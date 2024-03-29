from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import re
#from kivy.config import Config
from telas import *
#from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.textinput import TextInput

from kivy.clock import Clock, mainthread
from kivy.uix.popup import Popup
#from plyer import gps
from kivy.uix.label import Label
from kivy.metrics import sp
#import openssl

#For buildoze spec
# (list) Permissions
#android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION
# (list) Application requirements
#requirements = kivy,plyer

#Config.read('config.ini')
class LabelAdap(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)

    def on_size(self,*args):
        # vamos colocar um espaço de 10 sp
        self.text_size = (self.width - sp(10), None)
    
    def on_texture_size(self,*args):
        self.size = self.texture_size
        self.height += sp(20)

class FloatInput(TextInput):
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class Gerenciador(ScreenManager):
    def __init__(self, **kw):
        super().__init__(**kw)

    #def current_location(self):
    #    try:
    #        gps.configure(on_location=self.on_location)
    #        gps.start()
    #    except NotImplementedError:
    #        popup = Popup(title="GPS Error",
    #            content=Label(text="GPS support is not implemented on your platform")
    #                ).open()
    #        Clock.schedule_once(lambda d: popup.dismiss(), 3)
    #
    #@mainthread
    #def on_location(self, **kwargs):
    #    print(kwargs)


class Mandiokito(App):
    def build (self):
        return Gerenciador()

if __name__ == '__main__':
    Mandiokito().run()

'''map = MapView(zoom=11, lon=50.6394, lat=3.057)
        m1 = MapMarker(lon=-34.977078, lat=-7.138594)
        map.add_marker(m1)
        return map'''