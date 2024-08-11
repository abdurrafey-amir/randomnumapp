import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
import time as tm


class Root(BoxLayout):

    def __init__(self):
        super(Root, self).__init__()

    def generate_number(self):
        self.random_button.disabled = True
        self.random_button.text = "Generating..."
        num = random.randint(0, 1000)
        self.random_label.text = str(num)
        self.random_button.disabled = False
        self.random_button.text = 'Generate'


class Random1(App):

    def build(self):
        return Root()
    


random1 = Random1()
random1.run()