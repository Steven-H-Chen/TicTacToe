from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder 

Builder.load_file("layouts.kv")

class Layoutsx(FloatLayout):
    def sizing (self, **kwargs):
        super(Layoutsx, self).sizing(**kwargs)
        pass


class Myfunc(App):
    def build(self):
        
        layout = FloatLayout()
        glayout = Layoutsx()
        layout.add_widget(glayout)

        return Layoutsx()


