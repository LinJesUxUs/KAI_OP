from tkinter import *
import time
import threading
import random
from collections import namedtuple, deque

Point = namedtuple('Point', ['x','y'])
Body = namedtuple('Body', ['x','y','shape'])

FRAME_LENGTH = 0.5
FRAME_SIZE = 460
SNAKE_LENGTH = 5
POINT_SIZE = 20
NORMAL_FRAME_SIZE = FRAME_SIZE // POINT_SIZE
LIMIT = NORMAL_FRAME_SIZE * POINT_SIZE - POINT_SIZE
# Цвета
SNAKE_COLOR = '#b85b68'
FOOD_COLOR = '#d83830'
BACKGROUND = "#4b3834"
CORNERS = '#3b2319'
TEXT_COLOR = SNAKE_COLOR

DIRECTIONS = {
    "Left":  Point(-POINT_SIZE, 0),
    "Right": Point(POINT_SIZE, 0),
    "Up":    Point(0, -POINT_SIZE),
    "Down":  Point(0, POINT_SIZE)
}

body = deque()
food = Body(0,0,None)
way_current = "Up"
game_running = True
score = 0
best_score = 0

move_event = threading.Event()

def is_opposite(key):
	opposites = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}
	return opposites.get(key) == way_current

def check_collision(p):
    # Проверка границ
	if p.x < POINT_SIZE or p.x >= LIMIT or p.y < POINT_SIZE or p.y >= LIMIT:
		return False
    # Проверка столкновения с собой
	for i in body:
		if i.x == p.x and i.y == p.y:
			return False
	return True

def snake_body_paint(x,y):
    return c.create_rectangle( x, y, x+POINT_SIZE-1, y+POINT_SIZE-1, tag="body", fill=SNAKE_COLOR, outline=SNAKE_COLOR)

def snake_init(c):
	c.delete("body","score","food")
	body.clear()
	start_pos = NORMAL_FRAME_SIZE // 2 * POINT_SIZE
	for i in range(SNAKE_LENGTH):
		shape = snake_body_paint( start_pos, start_pos)
		body.append( Body( start_pos, start_pos, shape) )

def drop_food(c):
	global food
	if food.shape: c.delete("food")
	pos = Point(0,0)
	while not check_collision(pos):
		pos = Point( random.randrange( POINT_SIZE, LIMIT, POINT_SIZE)
				   , random.randrange( POINT_SIZE, LIMIT, POINT_SIZE) )
	shape = c.create_oval( pos.x, pos.y, pos.x+POINT_SIZE, pos.y+POINT_SIZE, tag="food", fill=FOOD_COLOR, outline=FOOD_COLOR)
	food = Body( pos.x, pos.y, shape)

def crawl(c,new_p):
	c.delete(body[-1].shape)
	body.pop()
	shape = snake_body_paint(new_p.x, new_p.y)
	body.appendleft( Body( new_p.x, new_p.y, shape) )

def mv_snake(c):
	global game_running
	new_p = Point( body[0].x + DIRECTIONS[way_current].x
				 , body[0].y + DIRECTIONS[way_current].y)
	if not check_collision(new_p):
		game_running = False
		return #None
	if food.x == new_p.x and food.y == new_p.y:
		global score
		score+=1
		shape = snake_body_paint(food.x, food.y)
		body.appendleft( Body( food.x, food.y, shape) )
		drop_food(c)
	else: crawl(c,new_p)

def paint_frames(c):
	global game_running, best_score, score
	game_running = True
	score = 0
	snake_init(c)
	drop_food(c)
	while game_running:
		move_event.wait(timeout=FRAME_LENGTH)
		move_event.clear()
		if game_running: mv_snake(c)
	c.delete( "body", "food")
	best_score = max( score, best_score)
	c.create_text(FRAME_SIZE/2, FRAME_SIZE/2
        , text=f"Game Over\nScore: {score}\nBest: {best_score}\n[R] to Restart"
		, fill=TEXT_COLOR, font=("Arial", FRAME_SIZE//12, "bold"), justify=CENTER, tag="score")

def on_key_press(event):
	global way_current, game_running
	key = event.keysym
	if key in DIRECTIONS and not is_opposite(key):
		way_current = key
		move_event.set()
	elif key.lower() == 'r' and not game_running:
		restart()
	elif key.lower() == 'q':
		if game_running:
			game_running = False
			move_event.set()
		else: root.destroy()

def restart():
	threading.Thread( target=paint_frames,args=(c,),daemon=True).start()

root = Tk()
root.title("PySnake")
root.resizable(False, False)
c = Canvas(width=FRAME_SIZE,height=FRAME_SIZE,background=BACKGROUND)
c.pack()
c.focus_set()

border_size = NORMAL_FRAME_SIZE * POINT_SIZE
c.create_rectangle(0, 0, border_size, border_size, width=POINT_SIZE*2, outline=CORNERS, fill=BACKGROUND)

c.bind('<Key>',on_key_press)
restart()

mainloop()