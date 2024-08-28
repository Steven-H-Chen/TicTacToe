from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

# Define the MainScreen
class MainScreen(Screen):
    pass

# Define the ScoreboardScreen
class GameScreen(Screen):
    pass

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
    MyApp().run()



