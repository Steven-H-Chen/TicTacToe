import os, sys
from kivy.resources import resource_add_path, resource_find
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout


# Define the MainScreen
class MainScreen(Screen):
    pass

# Define the ScoreboardScreen
class GameScreen(Screen):
    num = 9
    turn = "X"
    def presser(self, btn):
        if self.turn == 'X':
            btn.text ="X"
            btn.disabled = True
            self.ids.score.text = "0's Turn"
            self.turn ="O"
            if self.num > 0: 
                self.num -= 1
                if self.ids.btn1.text == "X" and self.ids.btn2.text == "X" and self.ids.btn3.text == "X":
                    self.ids.winc.text = "X has won"
                elif self.ids.btn4.text == "X" and self.ids.btn5.text == "X" and self.ids.btn6.text == "X":
                    self.ids.winc.text = "X has won"
                elif self.ids.btn7.text == "X" and self.ids.btn8.text == "X" and self.ids.btn9.text == "X":
                    self.ids.winc.text = "X has won"
                elif self.ids.btn1.text == "X" and self.ids.btn4.text == "X" and self.ids.btn7.text == "X":
                    self.ids.winc.text = "X has won"
                elif self.ids.btn2.text == "X" and self.ids.btn5.text == "X" and self.ids.btn8.text == "X":
                    self.ids.winc.text = "X has won"
                elif self.ids.btn3.text == "X" and self.ids.btn6.text == "X" and self.ids.btn9.text == "X":
                    self.ids.winc.text = "X has won"
                else:
                    pass
            else:
                pass
        else:
            btn.text ="O"
            btn.disabled = True 
            self.ids.score.text = "X's Turn"
            self.turn = "X"
            if self.num > 0: 
                self.num -= 1
                if self.ids.btn1.text == "O" and self.ids.btn2.text == "O" and self.ids.btn3.text == "O":
                    self.ids.winc.text = "O has won"
                elif self.ids.btn4.text == "O" and self.ids.btn5.text == "O" and self.ids.btn6.text == "O":
                    self.ids.winc.text = "O has won"
                elif self.ids.btn7.text == "O" and self.ids.btn8.text == "O" and self.ids.btn9.text == "O":
                    self.ids.winc.text = "O has won"
                elif self.ids.btn1.text == "O" and self.ids.btn4.text == "O" and self.ids.btn7.text == "O":
                    self.ids.winc.text = "O has won"
                elif self.ids.btn2.text == "O" and self.ids.btn5.text == "O" and self.ids.btn8.text == "O":
                    self.ids.winc.text = "O has won"
                elif self.ids.btn3.text == "O" and self.ids.btn6.text == "O" and self.ids.btn9.text == "O":
                    self.ids.winc.text = "O has won"
                else:
                    pass
            else:
                pass
    
    def restart(self):
        #self.turn = "X"
        for i in range(1, 10):
            button = self.ids[f"btn{i}"]
            button.disabled = False
            button.text = ""
            self.ids.winc.text = "Who will win?"
            self.turn = "X"
            self.ids.score.text = "X First"
            self.num = 9


class ScoreScreen(Screen):
    pass

# Define the ScreenManager and the main App class
class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # Add the screens to the ScreenManager
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(ScoreScreen(name='score'))

        return sm

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MyApp().run()


