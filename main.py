# First things to do before coding
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty


# 2 import object Widget + Use Kv file
class WidgetsExemple(GridLayout):
    my_text = StringProperty("Cool")
    def on_button_click(self):
        print('Cool Up')
        self.my_text = "Test Cool"


# 3 Create our Object
class LeLabApp(App):
    pass


# 4 run our App
LeLabApp().run()