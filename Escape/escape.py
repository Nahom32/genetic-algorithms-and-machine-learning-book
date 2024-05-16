import turtle
import pickle
import argparse
import random
def escaped(position):
    return position[0] < -35 or position[0] > 35 or position[1] < -35 or position[1] > 35

def draw_line():
    angle = 0
    step = 5
    t = turtle.Turtle()
    while not escaped(t.position()):
        t.left(angle)
        t.forward(step)
        
def store_position_data(L, t):
    position = t.position()
    L.append([position[0], position[1], escaped(position)])
    
def draw_square(t, size):
    L = []
    for i in range(4):
        t.forward(size)
        t.left(90)
        store_position_data(L, t)
    return L

def draw_squares(number):
    t = turtle.Turtle()
    L = []
    for i in range(1, number + 1):
        t.penup()
        t.goto(-i, -i)
        t.pendown()
        L.extend(draw_square(t, i * 2))
    return L

def draw_squares_until_escaped(n):
    t = turtle.Turtle()
    L = draw_squares(n)
    with open("data_square", "wb") as f:
        pickle.dump(L, f)

def draw_spirals_until_escaped():
    t = turtle.Turtle()
    t.penup()
    t.left(random.randint(0, 360))
    t.pendown()
    i = 0
    turn = 360/random.randint(1, 10)
    L = []
    store_position_data(L, t)
    while not escaped(t.position()):
        i += 1
        t.forward(i*5)
        t.right(turn)
        store_position_data(L, t)
    return L

def draw_random_spirangles():
    L = []
    for _ in range (10):
        L.extend(draw_spirals_until_escaped())
        with open("data_rand", "wb") as f:
            pickle.dump(L, f)
            





