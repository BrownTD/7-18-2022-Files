#:kivy
from kivy.lang import Builder
from kivymd.app import MDApp

#<MySwiper@MDSwiperItem>
FitImage:
    source: "logo.png"
    radius: [20,]
    
MDScreen:

    MDToolbar:
    id: toolbar
    elevation: 10
    pos_hint: {"top": 1}

MDSwiper:
    size_hint_y: None
    height: root.height - toolbar.height - dp(40)
    y: root.height - self.height - toolbar.height - dp(20)

    MySwiper:
    MySwiper:
    MySwiper:
    MySwiper:
    MySwiper:


class Homies(MDApp):
    def buil(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "White"
        return Builder.load_file("intro_swiper.kv")
<undefined@FitImage>:
    source:"logo.png"
    radius:[20,]

