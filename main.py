from window import *
from algorithms import *

def main(window, width):
    ROWS = 40
    grid = make_grid(ROWS, width)

    start = None #the start and 
    end = None #end position of the grid

    run = True #control variable
    while run:
        draw_window(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #if left mouse button is clicked
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node 
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            #if right mouse button is clicked
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    astar(lambda : draw_window(window, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_RETURN and start and end:
                    djkistra(lambda : draw_window(window, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

main(WINDOW, WIDTH)
