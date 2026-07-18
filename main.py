from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import time
import random

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50)
        self.pwd = TextInput(hint_text="Enter Password", password=True)
        btn = Button(text="Login", on_press=self.check_pwd)
        layout.add_widget(self.pwd)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def check_pwd(self, instance):
        if self.pwd.text == "S5X018189":
            self.manager.current = 'game'

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.info = Label(text="Initializing...", font_size='18sp')
        layout.add_widget(self.info)
        self.add_widget(layout)
        Clock.schedule_interval(self.update_ui, 1.0)

    def update_ui(self, dt):
        ts = int(time.time())
        period = 20260718100050000 + (ts // 60)
        num = random.randint(0, 9)
        size = "BIG" if num >= 5 else "SMALL"
        self.info.text = f"PERIOD: {period}\nPREDICTION: {size} ({num})"

class S5XApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    S5XApp().run()
  
