import pygame
from copy import deepcopy
from random import choice, randrange

w, h = 10, 20
tile = 45
game_res = w * tile, h * tile
fps = 60

pygame.init()
game_sc = pygame.display.set_mode(game_res)
clock = pygame.time.Clock()

grid = [pygame.Rect(x*tile, y*tile, tile, tile) for x in range(w) for y in range(h)]

# made considering that the blocks are formed by coordinates in a cartesian plane (each pixel is 1'cm')
blocks_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
            [(0, -1), (-1, -1), (-1, 0), (0, 0)],
            [(-1, 0), (-1, 1), (0, 0), (0, -1)],
            [(0, 0), (-1, 0), (0, 1), (-1, -1)],
            [(0, 0), (0, -1), (0, 1), (-1, -1)],
            [(0, 0), (0, -1), (0, 1), (1, -1)],
            [(0, 0), (0, -1), (0, 1), (-1, 0)]]

blocks = [[pygame.Rect(x + w // 2, y + 1, 1, 1) for x, y in block_pos] for block_pos in blocks_pos]
block_rect = pygame.Rect(0, 0, tile - 2, tile - 2)
field = [[0 for i in range(w)] for i in range(h)]

animation_count, animation_speed, animation_limit = 0, 10, 2000 #blocks falling animation

block = deepcopy(choice(blocks)) # choice will select a random block pattern

def checkBorders(): #blocks will collide with the borders
    if block[i].x < 0 or block[i].x > w - 1:
        return False
    elif block[i].y > h - 1 or field[block[i].y][block[i].x]:
        return False
    return True

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
            elif event.key == pygame.K_DOWN:
                animation_limit = 100
    # x
    block_copy = deepcopy(block)
    for i in range(4):
        block[i].x += dx
        if not checkBorders():
            block = deepcopy(block_copy)
            break

    # y
    animation_count += animation_speed
    if animation_count > animation_limit:
        animation_count = 0
        block_copy = deepcopy(block)
        for i in range(4):
            block[i].y += 1
        if not checkBorders():
            for i in range(4):
                field[block_copy[i].y][block_copy[i].x] = pygame.Color('purple')
            block = deepcopy(choice(blocks))
            animation_limit = 120
            break


    #background grid draw    
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

    #block draw
    for i in range(4):
        block_rect.x = block[i].x * tile
        block_rect.y = block[i].y * tile
        pygame.draw.rect(game_sc, pygame.Color('purple'), block_rect)

    # field draw
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                block_rect.x, block_rect.y = x * tile, y * tile
                pygame.draw.rect(game_sc, col, block_rect)

    pygame.display.flip()
    clock.tick()