from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from cbutton import Layoutsx, Myfunc

class MyTicApp(App):
    classob = Myfunc()

    def build(self):
        # Load the .kv file
        layout = FloatLayout()

        glayout = Layoutsx()

        layout.add_widget(glayout)

        return Layoutsx()

    # Variables
    turn = "X"
    rcds = []
    itm = 2

    def presser(self, btn):
        if self.turn == 'X':
            btn.text = "X"
            btn.disabled = True
            self.root.ids.score.text = "O's Turn"
            self.turn = "O"
            self.rcds.append((btn.custom_attr, btn.text))
            if self.itm < len(self.rcds) - 1:
                self.rcds[self.itm], self.rcds[self.itm + 1] = self.rcds[self.itm + 1], self.rcds[self.itm]
            else:
                pass
        else:
            btn.text = "O"
            self.rcds.append((btn.custom_attr, btn.text))
            btn.disabled = True
            self.root.ids.score.text = "X's Turn"
            self.turn = "X"
            if self.itm < len(self.rcds) - 1:
                self.rcds[self.itm], self.rcds[self.itm + 1] = self.rcds[self.itm + 1], self.rcds[self.itm]
            else:
                pass

    def sortwin(self, rcds):
        for (custom_attr, text) in enumerate(rcds):
            if custom_attr == 'u1' and text == 'X':
                if custom_attr == 'u2' and text == 'X':
                    if custom_attr =='u3' and text =='X':
                        self.root.ids.winc.text = "X has won"
            else:
                self.root.ids.winc.text = "No one has yet to win"

    def restart(self):
        #self.turn = "X"
        for i in range(1, 10):
            button = self.root.ids[f"btn{i}"]
            button.disabled = False
            button.text = ""

if __name__ == '__main__':
    MyTicApp().run()
