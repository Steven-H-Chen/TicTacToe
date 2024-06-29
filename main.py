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
    rcds = [['' for _ in range(3)] for _ in range(3)]
     

    def presser(self, btn):
        if self.turn == 'X':
            btn.text = "X"
            self.rcds(btn.custom_attr, btn.text)
            btn.disabled = True
            self.root.ids.score.text = "O's Turn"
            self.turn = "O"
            #self.rcds.append((btn.custom_attr, btn.text))
            for i in range(3):
                for p in range(3):
                    self.rcds.append(i,p)
        else:
            btn.text = "O"
            self.rcds(btn.custom_attr, btn.text)
            #self.rcds.append((btn.custom_attr, btn.text))
            btn.disabled = True
            self.root.ids.score.text = "X's Turn"
            self.turn = "X"
            for i in range(3):
                for p in range(3):
                    self.rcds.append(i,p)
        
        winner = self.check_winner()
        if winner:
            self.root.ids.score.text = "Game Over"
            self.root.ids.testing.text = f"{winner} wins!"
            # Disable all buttons after a win
            for i in range(1, 10):
                self.root.ids[f"btn{i}"].disabled = True


        

    def restart(self):
        #self.turn = "X"
        for i in range(1, 10):
            button = self.root.ids[f"btn{i}"]
            button.disabled = False
            button.text = ""

if __name__ == '__main__':
    MyTicApp().run()
