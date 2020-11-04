from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
#from kivy.core.window import window

#Window.size = (400,854)
from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')
#from kivymd.theming import ThemeManager

def get_ing(m):
    salt = str(14530*m/1000)
    return {'salt': salt}

class Container(GridLayout):

    def calculate(self):
        m = int(self.text_input.text)
        self.salt.text = get_ing(m).get('salt')


class MyApp(App):
    #theme_cls = ThemeManager
    #title = 'Coppa app'
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()
