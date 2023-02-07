from dataclasses import dataclass

from render2d import Renderer2D
from render3d import Renderer3D
from world import World
import pyglet

@dataclass
class Game:
    world: World
    render2d: Renderer2D
    render3d: Renderer3D
    
    
    def __init__(self):
        self.world = World(10, 10)
        print(self.world)
        self.render2d = Renderer2D()
        self.render3d = Renderer3D()
        
    def run():
        pyglet.app.run()