import pygame

w, h = 10, 20
tile = 45
game_res = w * tile, h * tile
fps = 60

pygame.init()
game_sc = pygame.display.set_mode(game_res)
clock = pygame.time.Clock()

grid = [pygame.Rect(x*tile, y*tile, tile, tile) for x in range(w) for y in range(h)]

# made considering that the blocks are formed by coordinates in a cartesian plane (each pixel is 1`cm`)
blocks_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
            [(0, -1), (-1, -1), (-1, 0), (0, 0)],
            [(-1, 0), (-1, 1), (0, 0), (0, -1)],
            [(0, 0), (-1, 0), (0, 1), (-1, -1)],
            [(0, 0), (0, -1), (0, 1), (-1, -1)],
            [(0, 0), (0, -1), (0, 1), (1, -1)],
            [(0, 0), (0, -1), (0, 1), (-1, 0)]]

blocks = [[pygame.Rect(x + w // 2, y + 1, 1, 1) for x, y in block_pos] for block_pos in blocks_pos]
block_rect = pygame.Rect(0, 0, tile - 2, tile - 2)

block = blocks[0]

while True:
    dx = 0
    game_sc.fill(pygame.Color('black'))

    #controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1

    # x
    for i in range(4):
        block[i].x += dx

    #background grid draw    
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

    #block draw
    for i in range(4):
        block_rect.x = block[i].x * tile
        block_rect.y = block[i].y * tile
        pygame.draw.rect(game_sc, pygame.Color('purple'), block_rect)

    pygame.display.flip()
    clock.tick()