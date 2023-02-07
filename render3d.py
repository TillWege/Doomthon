from dataclasses import dataclass
import pyglet

@dataclass
class Renderer3D:
    window: pyglet.window.Window
    label: pyglet.text.Label

    def __init__(self):
        self.window = pyglet.window.Window()

        self.label = pyglet.text.Label('3D-Renderer',
                        font_name='Times New Roman',
                        font_size=36,
                        x=self.window.width//2,
                        y=self.window.height//2,
                        anchor_x='center', anchor_y='center')

        def render():
            self.window.clear()
            self.label.draw()
        
        
        self.window.on_draw = render
        
        