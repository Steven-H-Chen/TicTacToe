from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

Builder.load_file("layout2.kv")

class Layoutsx(FloatLayout):
    pass

class MyTicApp(App):
    def build(self):
        return Layoutsx()
    
    num = 9
    turn = "X"
    def presser(self, btn):
        if self.turn == 'X':
            btn.text ="X"
            btn.disabled = True
            self.root.ids.score.text = "0's Turn"
            self.turn ="O"
            if self.num > 0: 
                self.num -= 1
                if self.root.ids.btn1.text == "X" and self.root.ids.btn2.text == "X" and self.root.ids.btn3.text == "X":
                    self.root.ids.winc.text = "X has won"
                elif self.root.ids.btn4.text == "X" and self.root.ids.btn5.text == "X" and self.root.ids.btn6.text == "X":
                    self.root.ids.winc.text = "X has won"
                elif self.root.ids.btn7.text == "X" and self.root.ids.btn8.text == "X" and self.root.ids.btn9.text == "X":
                    self.root.ids.winc.text = "X has won"
                elif self.root.ids.btn1.text == "X" and self.root.ids.btn4.text == "X" and self.root.ids.btn7.text == "X":
                    self.root.ids.winc.text = "X has won"
                elif self.root.ids.btn2.text == "X" and self.root.ids.btn5.text == "X" and self.root.ids.btn8.text == "X":
                    self.root.ids.winc.text = "X has won"
                elif self.root.ids.btn3.text == "X" and self.root.ids.btn6.text == "X" and self.root.ids.btn9.text == "X":
                    self.root.ids.winc.text = "X has won"
                else:
                    pass
            else:
                pass
        else:
            btn.text ="O"
            btn.disabled = True 
            self.root.ids.score.text = "X's Turn"
            self.turn = "X"
            if self.num > 0: 
                self.num -= 1
                if self.root.ids.btn1.text == "O" and self.root.ids.btn2.text == "O" and self.root.ids.btn3.text == "O":
                    self.root.ids.winc.text = "O has won"
                elif self.root.ids.btn4.text == "O" and self.root.ids.btn5.text == "O" and self.root.ids.btn6.text == "O":
                    self.root.ids.winc.text = "O has won"
                elif self.root.ids.btn7.text == "O" and self.root.ids.btn8.text == "O" and self.root.ids.btn9.text == "O":
                    self.root.ids.winc.text = "O has won"
                elif self.root.ids.btn1.text == "O" and self.root.ids.btn4.text == "O" and self.root.ids.btn7.text == "O":
                    self.root.ids.winc.text = "O has won"
                elif self.root.ids.btn2.text == "O" and self.root.ids.btn5.text == "O" and self.root.ids.btn8.text == "O":
                    self.root.ids.winc.text = "O has won"
                elif self.root.ids.btn3.text == "O" and self.root.ids.btn6.text == "O" and self.root.ids.btn9.text == "O":
                    self.root.ids.winc.text = "O has won"
                else:
                    pass
            else:
                pass
    
    def restart(self):
        #self.turn = "X"
        for i in range(1, 10):
            button = self.root.ids[f"btn{i}"]
            button.disabled = False
            button.text = ""
            self.root.ids.winc.text = "Who will win?"
            self.turn = "X"
            self.root.ids.score.text = "X First"
            self.num = 9


if __name__ == '__main__':
    MyTicApp().run()