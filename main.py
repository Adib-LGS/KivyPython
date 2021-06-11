# First things to do before coding
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty


# 2 import object Widget + Use Kv file
class WidgetsExample(GridLayout):
    count = 0
    activ_counter = BooleanProperty(False)
    my_text = StringProperty("Cool")

    def on_button_click(self):
        if self.activ_counter:
            self.count += 1
            self.my_text = str(self.count)


    def on_toggle_state(self, widget):
        # print(widget.state)
        if widget.state == "down":
            print("Man down")
            widget.text = "ON"
            self.activ_counter = True
        else:
            print("Man normal state is alive")
            widget.text = "OFF"
            self.activ_counter = False






# 3 Create our Object
class LeLabApp(App):
    pass


# 4 run our App
LeLabApp().run()