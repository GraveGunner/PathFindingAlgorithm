from queue import PriorityQueue
import pygame
#used to find the heuristic value using manhattan distance
#as movement is allowed in only 4 directions
def h_func(p1, p2): 
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def u_neighbours(grid, node):
    node.neighbours = []
    if node.row < node.total_rows - 1 and not grid[node.row + 1][node.col].is_barrier(): # DOWN
        node.neighbours.append(grid[node.row + 1][node.col])

    if node.row > 0 and not grid[node.row - 1][node.col].is_barrier(): # UP
        node.neighbours.append(grid[node.row - 1][node.col])

    if node.col < node.total_rows - 1 and not grid[node.row][node.col + 1].is_barrier(): # RIGHT
        node.neighbours.append(grid[node.row][node.col + 1])

    if node.col > 0 and not grid[node.row][node.col - 1].is_barrier(): # LEFT
        node.neighbours.append(grid[node.row][node.col - 1])


def astar(draw, grid, start, end):
    count = 0 
    open_set = PriorityQueue() #start node in the open set when starting
    open_set.put((0, count, start)) #f score, number for tiebreak, node itself
    came_from = {} #keep track of path
    g_score = {node: float("inf") for row in grid for node in row} #keeps track of shortest distance from start to current node
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row} #keeps track of our predicted distance from current to end
    f_score[start] = h_func(start.get_pos(), end.get_pos())

    open_set_track = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2] #get the smallest node from priority queue
        open_set_track.remove(current) #update according to the queue

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        u_neighbours(grid, current)

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1 #+1 because distance is considered 1

            if temp_g_score < g_score[neighbour]: #if a better path is found we add that to our dict
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h_func(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_track:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_track.add(neighbour)
                    neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    print("Path not found.")
    return False

def djkistra(draw, grid, start, end):
    count = 0 
    open_set = PriorityQueue() #start node in the open set when starting
    open_set.put((0, count, start)) #f score, number for tiebreak, node itself
    came_from = {} #keep track of path
    g_score = {node: float("inf") for row in grid for node in row} #keeps track of shortest distance from start to current node
    g_score[start] = 0

    open_set_track = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2] #get the smallest node from priority queue
        open_set_track.remove(current) #update according to the queue

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        u_neighbours(grid, current)

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1 #+1 because distance is considered 1

            if temp_g_score < g_score[neighbour]: #if a better path is found we add that to our dict
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                if neighbour not in open_set_track:
                    count += 1
                    open_set.put((g_score[neighbour], count, neighbour))
                    open_set_track.add(neighbour)
                    neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
