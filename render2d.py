from dataclasses import dataclass
import pyglet

@dataclass
class Renderer2D:
    window: pyglet.window.Window
    label: pyglet.text.Label

    def __init__(self):
        self.window = pyglet.window.Window()

        self.label = pyglet.text.Label('2D-Renderer',
                        font_name='Times New Roman',
                        font_size=36,
                        x=self.window.width//2,
                        y=self.window.height//2,
                        anchor_x='center', anchor_y='center')

        
        @self.window.event('on_draw')
        def render():
            self.window.clear()
            self.label.draw()
            
        