from dataclasses import dataclass
from enum import Enum

class Tile(Enum):
    Empty = 0
    Wall = 1
    
@dataclass
class World:
    Tiles: list[list[Tile]]
    
    def __init__(self, width: int, height: int):
        self.Tiles = [[Tile.Empty for x in range(width)] for y in range(height)]
        for x in range(width):
            self.Tiles[0][x] = Tile.Wall
            self.Tiles[height-1][x] = Tile.Wall
        for y in range(height):
            self.Tiles[y][0] = Tile.Wall
            self.Tiles[y][width-1] = Tile.Wall
            
    def __str__(self):
        return '\n'.join([''.join([str(tile.value) for tile in row]) for row in self.Tiles])