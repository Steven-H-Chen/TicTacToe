from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from cbutton import Layoutsx, Myfunc

class MyTicApp(App):
    classob = Myfunc()

    def build(self):
        # Load the .kv file
        layout = FloatLayout()
        glayout = Layoutsx()
        layout.add_widget(glayout)
        return Layoutsx()

    turn = "X"

    def presser(self, btn):
        
        if self.turn == 'X':
            btn.text = "X"
            btn.disabled = True
            self.root.ids.score.text = "O's Turn"
            self.turn = "O"
        else:
            btn.text = "O"
            btn.disabled = True
            self.root.ids.score.text = "X's Turn"
            self.turn = "X"



    def restart(self):
        #self.turn = "X"
        for i in range(1, 10):
            button = self.root.ids[f"btn{i}"]
            button.disabled = False
            button.text = ""

if __name__ == '__main__':
    MyTicApp().run()
