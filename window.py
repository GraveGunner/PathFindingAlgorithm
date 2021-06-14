import pygame
from colors import *
WIDTH = HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Finding Algorithm Visualiser")

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width #the actual x co-ordinate of the node
        self.y = col*width #the actual y co-ordiante of the node
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self): #used to find if the node is already visited
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == YELLOW

    def is_end(self):
        return self.color == AQUA
    
    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = GREEN
    
    def make_closed(self):
        self.color = YELLOW

    def make_open(self):
        self.color = AQUA

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = RED

    def make_path(self):
        self.color = PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def __lt__(self, other): #used to compare two Node objects
        return False


def make_grid(rows, width):
    grid = []
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

def draw_grid(window, rows, width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(window, GREY, (j*gap, 0), (j*gap, width))

def draw_window(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()

#used to find the position of the node
def get_clicked_pos(pos, rows, width): 
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col
