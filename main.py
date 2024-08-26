from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Define the MainScreen
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        # Add a button to switch to the scoreboard screen
        switch_to_scoreboard_btn = Button(text="Go to Scoreboard")
        switch_to_scoreboard_btn.bind(on_press=self.go_to_scoreboard)
        layout.add_widget(switch_to_scoreboard_btn)

    def go_to_scoreboard(self, instance):
        self.manager.current = 'scoreboard'

# Define the ScoreboardScreen
class ScoreboardScreen(Screen):
    def __init__(self, **kwargs):
        super(ScoreboardScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        # Add a button to switch back to the main screen
        switch_to_main_btn = Button(text="Back to Main Screen")
        switch_to_main_btn.bind(on_press=self.go_to_main)
        layout.add_widget(switch_to_main_btn)

    def go_to_main(self, instance):
        self.manager.current = 'main'

# Define the ScreenManager
class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # Add the screens to the ScreenManager
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ScoreboardScreen(name='scoreboard'))

        return sm

if __name__ == '__main__':
    MyApp().run()


