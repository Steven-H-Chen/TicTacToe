from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder 

Builder.load_file("layouts.kv")

class Layoutsx(FloatLayout):
    def sizing (self, **kwargs):
        super(Layoutsx, self).sizing(**kwargs)
    pass

class MyButton(App):
    def build(self):
        return Layoutsx()
    
    counters = []
    turn = "X"
    def presser(self, btn):
        if self.turn == 'X':
            btn.text ="X"
            btn.disabled = True
            self.root.ids.score.text = "0's Turn"
            self.turn ="O"
        else:
            btn.text ="O"
            btn.disabled = True 
            self.root.ids.score.text = "X's Turn"
            self.turn = "X"
        
    def restart(self):
        self.turn = "X"

        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""
    pass