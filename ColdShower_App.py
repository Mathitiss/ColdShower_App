import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label

kivy.require('1.9.0')

Builder.load_string("""
<Start>: ############################################################################################## START SCREEN
    canvas:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
        
    Label:
        markup: True
        text: 'WATER'
        font_size: 64
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 250
        
    Label:
        markup: True
        text: '0'
        font_size: 124
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 15        
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: 300
        height: 300
        center_x: root.width / 2
        y: 185
        Widget:
            canvas:
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    circle: (self.center_x, self.center_y, self.height / 2)
                    width: 2
                                             
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Start_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Start_Button.png'
        size_hint: None, None
        size: 300, 65
        center_x: root.width / 2
        y: 50
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 1
            root.manager.current = 'Hot'
            
<Hot>: ############################################################################################## HOT WATER SCREEN
    canvas:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
            
    Label:
        markup: True
        text: 'HOT'
        color: 0.803, 0.42, 0.204, 1
        font_size: 64
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 250
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: 300
        height: 300
        center_x: root.width / 2
        y: 185
        Widget:
            canvas:
                Color:
                    rgba: 0.803, 0.42, 0.204, 1
                Line:
                    circle: (self.center_x, self.center_y, self.height / 2)
                    width: 2
        
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        size_hint: None, None
        size: 300, 65
        center_x: root.width / 2
        y: 50
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.transition.duration = 1
            root.manager.current = 'Start'
        
<Cold>: ############################################################################################## COLD WATER SCREEN
    canvas:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
            
    Label:
        markup: True
        text: 'COLD'
        color: 0.22, 0.51, 0.71, 1
        font_size: 64
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 250
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: 300
        height: 300
        center_x: root.width / 2
        y: 185
        Widget:
            canvas:
                Color:
                    rgba: 0.22, 0.51, 0.71, 1
                Line:
                    circle: (self.center_x, self.center_y, self.height / 2)
                    width: 2
        
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        size_hint: None, None
        size: 300, 65
        center_x: root.width / 2
        y: 50
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 0
            root.manager.current = 'Start'
            
<Hot2>: ############################################################################################## HOT WATER SCREEN
    canvas:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
            
    Label:
        markup: True
        text: 'HOT'
        color: 0.803, 0.42, 0.204, 1
        font_size: 64
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 250
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: 300
        height: 300
        center_x: root.width / 2
        y: 185
        Widget:
            canvas:
                Color:
                    rgba: 0.803, 0.42, 0.204, 1
                Line:
                    circle: (self.center_x, self.center_y, self.height / 2)
                    width: 2
        
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        size_hint: None, None
        size: 300, 65
        center_x: root.width / 2
        y: 50
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.transition.duration = 1
            root.manager.current = 'Start'
        
<Cold2>: ############################################################################################## COLD WATER SCREEN
    canvas:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
            
    Label:
        markup: True
        text: 'COLD'
        color: 0.22, 0.51, 0.71, 1
        font_size: 64
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 250
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: 300
        height: 300
        center_x: root.width / 2
        y: 185
        Widget:
            canvas:
                Color:
                    rgba: 0.22, 0.51, 0.71, 1
                Line:
                    circle: (self.center_x, self.center_y, self.height / 2)
                    width: 2
        
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        size_hint: None, None
        size: 300, 65
        center_x: root.width / 2
        y: 50
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 0
            root.manager.current = 'Start'

<Hot3>: ############################################################################################## HOT WATER SCREEN
    canvas:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
            
    Label:
        markup: True
        text: 'HOT'
        color: 0.803, 0.42, 0.204, 1
        font_size: 64
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 250
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: 300
        height: 300
        center_x: root.width / 2
        y: 185
        Widget:
            canvas:
                Color:
                    rgba: 0.803, 0.42, 0.204, 1
                Line:
                    circle: (self.center_x, self.center_y, self.height / 2)
                    width: 2
        
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        size_hint: None, None
        size: 300, 65
        center_x: root.width / 2
        y: 50
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.transition.duration = 1
            root.manager.current = 'Start'
        
<Cold3>: ############################################################################################## COLD WATER SCREEN
    canvas:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
            
    Label:
        markup: True
        text: 'COLD'
        color: 0.22, 0.51, 0.71, 1
        font_size: 64
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 250
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: 300
        height: 300
        center_x: root.width / 2
        y: 185
        Widget:
            canvas:
                Color:
                    rgba: 0.22, 0.51, 0.71, 1
                Line:
                    circle: (self.center_x, self.center_y, self.height / 2)
                    width: 2
        
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        size_hint: None, None
        size: 300, 65
        center_x: root.width / 2
        y: 50
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 0
            root.manager.current = 'Start'

<Hot4>: ############################################################################################## HOT WATER SCREEN
    canvas:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
            
    Label:
        markup: True
        text: 'HOT'
        color: 0.803, 0.42, 0.204, 1
        font_size: 64
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf'
        pos: 0, 250
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: 300
        height: 300
        center_x: root.width / 2
        y: 185
        Widget:
            canvas:
                Color:
                    rgba: 0.803, 0.42, 0.204, 1
                Line:
                    circle: (self.center_x, self.center_y, self.height / 2)
                    width: 2
        
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Images\\Stop_Button.png'
        size_hint: None, None
        size: 300, 65
        center_x: root.width / 2
        y: 50
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.transition.duration = 1
            root.manager.current = 'Start'
""")

class Start(Screen):
    pass

class Hot(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='10', font_size='124', pos=(0, 15), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        self.add_widget(self.label)

    def on_enter(self, *args):
        self.counter = 10
        self.label.text = str(self.counter)
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        self.schedule.cancel()

    def update_timer(self, dt):
        self.counter -= 1
        self.label.text = str(self.counter)
        if self.counter == 0:
            self.manager.current = 'Cold'

class Cold(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='10', font_size='124', pos=(0, 15), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        self.add_widget(self.label)

    def on_enter(self, *args):
        self.counter = 10
        self.label.text = str(self.counter)
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        self.schedule.cancel()

    def update_timer(self, dt):
        self.counter -= 1
        self.label.text = str(self.counter)
        if self.counter == 0:
            self.manager.current = 'Hot2'

class Hot2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='10', font_size='124', pos=(0, 15), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        self.add_widget(self.label)

    def on_enter(self, *args):
        self.counter = 10
        self.label.text = str(self.counter)
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        self.schedule.cancel()

    def update_timer(self, dt):
        self.counter -= 1
        self.label.text = str(self.counter)
        if self.counter == 0:
            self.manager.current = 'Cold2'

class Cold2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='10', font_size='124', pos=(0, 15), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        self.add_widget(self.label)

    def on_enter(self, *args):
        self.counter = 10
        self.label.text = str(self.counter)
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        self.schedule.cancel()

    def update_timer(self, dt):
        self.counter -= 1
        self.label.text = str(self.counter)
        if self.counter == 0:
            self.manager.current = 'Hot3'

class Hot3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='10', font_size='124', pos=(0, 15), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        self.add_widget(self.label)

    def on_enter(self, *args):
        self.counter = 10
        self.label.text = str(self.counter)
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        self.schedule.cancel()

    def update_timer(self, dt):
        self.counter -= 1
        self.label.text = str(self.counter)
        if self.counter == 0:
            self.manager.current = 'Cold3'

class Cold3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='10', font_size='124', pos=(0, 15), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        self.add_widget(self.label)

    def on_enter(self, *args):
        self.counter = 10
        self.label.text = str(self.counter)
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        self.schedule.cancel()

    def update_timer(self, dt):
        self.counter -= 1
        self.label.text = str(self.counter)
        if self.counter == 0:
            self.manager.current = 'Hot4'

class Hot4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='10', font_size='124', pos=(0, 15), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        self.add_widget(self.label)

    def on_enter(self, *args):
        self.counter = 10
        self.label.text = str(self.counter)
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        self.schedule.cancel()

    def update_timer(self, dt):
        self.counter -= 1
        self.label.text = str(self.counter)
        if self.counter == 0:
            self.manager.current = 'Start'

screen_manager = ScreenManager()
screen_manager.add_widget(Start(name="Start"))
screen_manager.add_widget(Hot(name="Hot"))        # 60 sec
screen_manager.add_widget(Cold(name="Cold"))      # 30 sec
screen_manager.add_widget(Hot2(name="Hot2"))      # 30 sec
screen_manager.add_widget(Cold2(name="Cold2"))    # 60 sec
screen_manager.add_widget(Hot3(name="Hot3"))      # 60 sec
screen_manager.add_widget(Cold3(name="Cold3"))    # 60 sec
screen_manager.add_widget(Hot4(name="Hot4"))      # 30 sec


class ColdShower(App):
    def build(self):
        Window.size = (375, 645)
        return screen_manager

ColdShower_App = ColdShower()
ColdShower_App.run()