from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import kivy

Builder.load_file("layout.kv")

class Layoutsx(GridLayout):
    pass



class MyTicApp(App):
    def build(self):
        return Layoutsx()
    
if __name__ == '__main__':
    MyTicApp().run()