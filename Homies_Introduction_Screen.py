#:kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from tkinter import Widget



#class Touch(Widget):
    #def on_touch_move(self, touch):
    #return Touch()
        

class Homies(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #add widgets to window


        #image widget
        self.window.add_widget(Image(source="logo.png"))
        #Lable Widget
        self.greeting = Label(text="The App for Gifting our Less Fortunate Friends")
        self.window.add_widget(self.greeting)
        self.getstarted = Label(text="Swipe up to Begin")
        self.window.add_widget(self.getstarted)
        #text input user
        self.user=TextInput(multiline=False)
        self.window.add_widget(self.user)
        #button widget
        self.button=Button(text="")
        self.window.add_widget(self.button)

        
        return self.window

class Homies(MDApp):
    def buil(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "White"
        return Builder.load_file("intro_swiper.kv")










if __name__ == "__main__":
    Homies().run()
