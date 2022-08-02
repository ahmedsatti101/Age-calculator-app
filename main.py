from cgitb import text
from datetime import datetime
from imp import source_from_cache
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class AgeCalculator(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        #Collecting input
        self.agerequest = Label(
            text = "Enter your date of birth: ",
            font_size = 50,
            color = "ffffff",
            bold = True
            )
        self.window.add_widget(self.agerequest)
        self.date = TextInput(
            multiline = False,
            padding_y = (30, 39),
            size_hint = (1, 0.7),
            font_size = 30
        )
        self.window.add_widget(self.date)
        #Button
        self.button = Button(
            text = "Calculate age",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
            )
        self.button.bind(on_press = self.getAge)
        self.window.add_widget(self.button)
        return self.window
    
    def getAge(self, event):
        today = datetime.today().year
        dob = self.date.text
        age = int(today) - int(dob)
        self.agerequest.text = "You are " + str(int(age)) + " years old."
    
if __name__ == "__main__":
    AgeCalculator().run()