from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

Builder.load_file("layout2.kv")


class Layoutsx(FloatLayout):
    def do_while_action(self):
        self.result_label.text = 'Action started...'
        
        # Simulate a do-while loop with Clock.schedule_interval
        self.counter = 0
        self.max_iterations = 5
        
        def do_while_callback(dt):
            self.counter += 1
            if self.counter <= self.max_iterations:
                self.result_label.text = f'Action running... Iteration {self.counter}'
            else:
                self.result_label.text = 'Action finished'
                # Stop the loop
                Clock.unschedule(do_while_callback)
        
        # Start the loop immediately and repeat every second
        Clock.schedule_interval(do_while_callback, 1.0)


class MyTicApp(App):
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
        #self.turn = "X"
        for i in range(1, 10):
            button = self.root.ids[f"btn{i}"]
            button.disabled = False
            button.text = ""

if __name__ == '__main__':
    MyTicApp().run()