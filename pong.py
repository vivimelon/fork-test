import os
import time
import random

width = 20
height = 10
ball_x, ball_y = width // 2, height // 2
ball_dx, ball_dy = 1, 1
player_y = height // 2
cpu_y = height // 2

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(height):
        for x in range(width):
            if x == 0 or x == width - 1:
                print('|', end='')
            elif (x == ball_x and y == ball_y):
                print('O', end='')
            elif (x == 1 and y in range(player_y - 1, player_y + 2)):
                print('#', end='')
            elif (x == width - 2 and y in range(cpu_y - 1, cpu_y + 2)):
                print('#', end='')
            else:
                print(' ', end='')
        print()

while True:
    draw()
    
    command = input("Move (W/S): ").strip().lower()
    if command == 'w' and player_y > 1:
        player_y -= 1
    elif command == 's' and player_y < height - 2:
        player_y += 1

    if cpu_y < ball_y and cpu_y < height - 2:
        cpu_y += 1
    elif cpu_y > ball_y and cpu_y > 1:
        cpu_y -= 1

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y >= height - 1:
        ball_dy *= -1
    if ball_x <= 1 and player_y - 1 <= ball_y <= player_y + 1:
        ball_dx *= -1
    if ball_x >= width - 2 and cpu_y - 1 <= ball_y <= cpu_y + 1:
        ball_dx *= -1
    if ball_x <= 0 or ball_x >= width - 1:
        break

    time.sleep(0.1)

print("Game Over!")

