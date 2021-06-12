# First things to do before coding
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty


# 2 import object Widget + Use Kv file
class WidgetsExample(GridLayout):
    count = 0
    active_counter = BooleanProperty(False)
    my_text = StringProperty("Cool")
    slider_value_txt = StringProperty("Value")
    txt_input_str = StringProperty()

    def on_button_click(self):
        if self.active_counter:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_state(self, widget):
        # print(widget.state)
        if widget.state == "down":
            print("Man down")
            widget.text = "ON"
            self.active_counter = True
        else:
            print("Man normal state is alive")
            widget.text = "OFF"
            self.active_counter = False

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    def slider_value(self, widget):
        final_slider_value = str(int(widget.value))
        print("Slider: " + final_slider_value)
        # self.slider_value_txt = final_slider_value

    def on_txt_validate(self, widget):
        self.txt_input_str = widget.text


# 3 Create our Object
class LeLabApp(App):
    pass


# 4 run our App
LeLabApp().run()