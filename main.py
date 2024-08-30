from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen ,FadeTransition
import sqlite3

# Define the KV layout string
Builder.load_string("""
<Screen1>:
    FloatLayout:
        MDLabel:
            text: "Welcome"
            font_style: 'Display'
            role: 'small'
            pos_hint: {'center_x': .5, 'center_y': .85}
            halign: 'center'
        
        MDTextField:
            id: playeri
            mode: "outlined"
            pos_hint: {'center_x': .2, 'center_y':.6}
            size_hint: None, None
            size: 275, 50
            
            MDTextFieldHintText:
                text: 'Player I' 
        
        MDTextField:
            id: playerii
            mode: "outlined"
            pos_hint: {'center_x': .8, 'center_y':.6}
            size_hint: None, None
            size: 275, 50
            
            MDTextFieldHintText:
                text: 'Player II'
        
        MDTextField:
            id: total
            mode: "outlined"
            pos_hint: {'center_x': .5, 'center_y':.35}
            size_hint: None, None
            size: 275, 50
            
            MDTextFieldHintText:
                text: 'Total Points'
        
        MDButton:
            style: "outlined"
            pos_hint: {'center_x': .5, 'center_y': .2}
            theme_width: "Custom"
            size_hint_x: .365
            height: "50dp" 
            on_release:
                app.submit()

            MDButtonText:
                text: 'Submit'   
                pos_hint: {"center_x": .5, "center_y": .5}         
                theme_font_size: "Custom"
                font_size: 18
        
<Screen2>:
    FloatLayout:
        MDLabel:
            id: wel_lbl
            text: "Welcome"
            font_style: 'Display'
            role: 'small'
            pos_hint: {'center_x': .5, 'center_y': .85}
            halign: 'center'
            valign: 'center'
        
        MDLabel:
            id: play1
            text: "Play1"
            font_style: 'Headline'
            role: 'small'
            pos_hint: {'center_x': .26, 'center_y': .65}
            halign: 'center'
            valign: 'center'
            
        MDLabel:
            id: play2
            text: "Play2"
            font_style: 'Headline'
            role: 'small'
            pos_hint: {'center_x': .72, 'center_y': .65}
            halign: 'center'
            valign: 'center'    
            
        MDButton:
            id: play1_plus
            style: "outlined"
            pos_hint: {'center_x': .2, 'center_y': .5}
            theme_width: "Custom"
            width: "90dp"
            height: "90dp"
            on_release: app.plus('x')
            MDButtonText:
                theme_font_size: "Custom"
                font_size: 33
                pos_hint: {'center_y': .5, 'center_x': .5}
                text: "+"
               
        MDButton:
            id: play1_minus
            style: "outlined"
            pos_hint: {'center_x': .32, 'center_y': .5}
            theme_width: "Custom"
            width: "90dp"
            height: "90dp"
            on_release: app.minus('a')
            MDButtonText:
                theme_font_size: "Custom"
                font_size: 45
                pos_hint: {'center_y': .5, 'center_x': .5}
                text: "-"
                
        MDButton:
            id: play2_plus
            style: "outlined"
            pos_hint: {'center_x': .65, 'center_y': .5}
            theme_width: "Custom"
            width: "90dp"
            height: "90dp"
            on_release: app.plus('y')
            MDButtonText:
                theme_font_size: "Custom"
                font_size: 33
                pos_hint: {'center_y': .5, 'center_x': .5}
                text: "+"
                
        MDButton:
            id: play2_minus
            style: "outlined"
            pos_hint: {'center_x': .77, 'center_y': .5}
            theme_width: "Custom"
            width: "90dp"
            height: "90dp"
            on_release: app.minus("b")
            MDButtonText:
                theme_font_size: "Custom"
                font_size: 45
                pos_hint: {'center_y': .5, 'center_x': .5}
                text: "-"
                
        MDLabel:
            id: score
            text: "0 | 0"
            font_style: "Display"
            role: 'small'
            pos_hint: {'center_x': .485, "center_y": .5}
            halign: 'center'
            
        MDLabel:
            id: declare
            text: ""
            font_style: "Display"
            role: 'small'
            pos_hint: {'center_x': .485, "center_y": .15}
            halign: 'center'
            
        MDButton:
            pos_hint: {'center_x': .065, 'center_y': .05}
            style: "outlined"
            on_release: app.back()
            MDButtonText:
                text: 'Back'
            
            
""")


class Screen1(Screen):
    pass


class Screen2(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.x = 0
        self.y = 0
        self.total = 0
        self.playeri = ""
        self.playerii = ""
        self.game_over = False  # Add a flag to track game state

        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Screen1(name='Screen1'))
        sm.add_widget(Screen2(name='Screen2'))
        return sm

    def disable_buttons(self):
        screen2 = self.root.get_screen('Screen2')
        screen2.ids.play1_plus.disabled = True
        screen2.ids.play1_minus.disabled = True
        screen2.ids.play2_plus.disabled = True
        screen2.ids.play2_minus.disabled = True

    def undisable_buttons(self):
        screen2 = self.root.get_screen('Screen2')
        screen2.ids.play1_plus.disabled = False
        screen2.ids.play1_minus.disabled = False
        screen2.ids.play2_plus.disabled = False
        screen2.ids.play2_minus.disabled = False

    def back(self):
        screen = self.root.get_screen('Screen1')
        screen2 = self.root.get_screen('Screen2')

        self.x = 0
        self.y = 0
        self.game_over = False  # Reset the game state

        screen2.ids.score.text = f"{self.x} | {self.y}"

        self.root.current = 'Screen1'
        self.undisable_buttons()

    def submit(self):
        screen = self.root.get_screen('Screen1')

        self.playeri = screen.ids.playeri.text
        self.playerii = screen.ids.playerii.text
        total = screen.ids.total.text

        if not self.playeri.strip() or not self.playerii.strip() or not total.strip():
            screen.ids.playeri.text = "Invalid Entry" if not self.playeri.strip() else self.playeri
            screen.ids.playerii.text = "Invalid Entry" if not self.playerii.strip() else self.playerii
            if not total.strip():
                screen.ids.total.text = "Invalid Total"
            return

        try:
            self.total = int(total)
        except ValueError:
            screen.ids.total.text = "Invalid Total"
            return

        if self.playeri == self.playerii:
            screen.ids.playeri.text = "Enter Player 1"
            screen.ids.playerii.text = "Enter Player 2"
            return

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (playeri, playerii, total, winner) VALUES (?, ?, ?, ?)",
                  (self.playeri, self.playerii, self.total, None))
        conn.commit()
        conn.close()

        self.root.current = "Screen2"
        screen1 = self.root.get_screen('Screen2')
        screen1.ids.wel_lbl.text = f"{self.playeri} vs {self.playerii}"
        screen1.ids.play1.text = self.playeri
        screen1.ids.play2.text = self.playerii

        screen.ids.playeri.text = ""
        screen.ids.playerii.text = ""
        screen.ids.total.text = ""

    def plus(self, obj):
        if self.game_over:
            return  # Do nothing if the game is over

        screen2 = self.root.get_screen('Screen2')

        if obj == 'x':
            if self.x < self.total:
                self.x += 1
        elif obj == 'y':
            if self.y < self.total:
                self.y += 1

        screen2.ids.score.text = f"{self.x} | {self.y}"

        if self.x == self.total:
            screen2.ids.declare.text = f"{self.playeri} Won!"
            self.update_winner(self.playeri)
            self.game_over = True
            self.disable_buttons()
        elif self.y == self.total:
            screen2.ids.declare.text = f"{self.playerii} Won!"
            self.update_winner(self.playerii)
            self.game_over = True
            self.disable_buttons()

    def minus(self, player):
        if self.game_over:
            return  # Do nothing if the game is over

        screen2 = self.root.get_screen('Screen2')

        if player == 'x' and self.x > 0:
            self.x -= 1
        elif player == 'y' and self.y > 0:
            self.y -= 1

        screen2.ids.score.text = f"{self.x} | {self.y}"

        if self.x == self.total:
            screen2.ids.declare.text = f"{self.playeri} Won!"
            self.update_winner(self.playeri)
            self.game_over = True
            self.disable_buttons()
        elif self.y == self.total:
            screen2.ids.declare.text = f"{self.playerii} Won!"
            self.update_winner(self.playerii)
            self.game_over = True
            self.disable_buttons()

    def update_winner(self, winner):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("UPDATE users SET winner = ?, total = ? WHERE playeri = ? AND playerii = ? AND winner IS NULL",
                  (winner, self.total, self.playeri, self.playerii))
        conn.commit()
        conn.close()

    def on_start(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        playeri TEXT NOT NULL,
                        playerii TEXT NOT NULL,
                        total INTEGER NOT NULL,
                        winner TEXT
                    )
                """)
        conn.commit()
        conn.close()



MainApp().run()
