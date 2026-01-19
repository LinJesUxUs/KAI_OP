from tkinter import *
import time
import threading
import random
from collections import namedtuple, deque

Point = namedtuple('Point', ['x','y'])
Body = namedtuple('Body', ['x','y','shape'])

frameLength = 0.5
frameSize = 460
snakeLength = 5
pointSize = 20

directions = {
    "Left":  Point(-pointSize, 0),
    "Right": Point(pointSize, 0),
    "Up":    Point(0, -pointSize),
    "Down":  Point(0, pointSize)
}

field = Point( frameSize, frameSize)
food = Body(0,0,None)
body = deque()
way_current = "Up"
game = True
best_score = 0
score = 0

move_event = threading.Event()

def SnakeInit(c):
	c.delete("body","score","food")
	body.clear()
	for i in range(snakeLength):
		buf = Point( field.x/pointSize//2*pointSize, field.y/pointSize//2*pointSize)
		body.append( Body( buf.x, buf.y
			,c.create_oval(buf.x, buf.y, buf.x+pointSize-1, buf.y+pointSize-1, tag="body", fill='black')) )

def is_opposite(key):
	if key == 'Left' and way_current == 'Right':
		return True
	if key == 'Right' and way_current == 'Left':
		return True
	if key == 'Up' and way_current == 'Down':
		return True
	if key == 'Down' and way_current == 'Up':
		return True
	return False


def on_key_press(event):
	global way_current
	global game
	key = event.keysym
	print(key)
	if key in directions and not is_opposite(key):
		way_current = key
		move_event.set()
	if key == 'r' and game == False:
		restart()
	if key == 'q':
		if game == True:
			game = False
			move_event.set()
		else: root.destroy()


def crawl(c,p):
	c.delete(body[-1].shape)
	body.pop()
	body.appendleft( Body( p.x, p.y
			,c.create_oval(p.x, p.y, p.x+pointSize-1, p.y+pointSize-1, tag="body", fill='black')) )

def check(p):
	if p.x < pointSize or p.x > frameSize//pointSize*(pointSize-1) or p.y < pointSize or p.y > frameSize//pointSize*(pointSize-1):
		return False
	for i in body:
		if i.x == p.x and i.y == p.y:
			return False
	return True

def DropFood(c):
	global food
	if not food.shape == None:
		c.delete("food")
	buf = Point(0,0)
	while not check(buf):
		buf = Point( random.randrange( pointSize, frameSize//pointSize*(pointSize-1), pointSize)
				   , random.randrange( pointSize, frameSize//pointSize*(pointSize-1), pointSize) )
	food = Body( buf.x, buf.y, c.create_rectangle(buf.x, buf.y, buf.x+pointSize, buf.y+pointSize, tag="food", fill='black') )

def Eating(c):
	global score
	body.appendleft( Body( food.x, food.y
			,c.create_oval(food.x, food.y, food.x+pointSize-1, food.y+pointSize-1, tag="body", fill='black')) )
	DropFood(c)
	score+=1

def MvSnake(c):
	global game
	checkPoint = Point(body[0].x + directions[way_current].x
					  ,body[0].y + directions[way_current].y)
	if not check(checkPoint):
		game = False
		return None
	if food.x == checkPoint.x and food.y == checkPoint.y:
		Eating(c)
		return None
	crawl(c,checkPoint)

def paintFrames(c):
	global game
	global best_score
	global score
	game = True
	score = 0
	SnakeInit(c)
	DropFood(c)
	while game:
		move_event.wait(timeout=frameLength)
		move_event.clear()
		MvSnake(c)
	c.delete("body","food")
	if score > best_score:
		best_score = score
	score_text = c.create_text(frameSize/2, frameSize/2, text=f"Game Over\nscore: {score}\nbest score: {best_score}"
		, fill="black", font=("Arial", frameSize//9), anchor="center", tag="score")

root = Tk()
c = Canvas(width=field.x,height=field.y,bg='grey40')
c.focus_set()
c.pack()
root.resizable(False, False)
c.create_rectangle(0,0,frameSize//pointSize*pointSize,frameSize//pointSize*pointSize,width=pointSize*2)

c.bind('<Key>',on_key_press)
thread = threading.Thread( target=paintFrames,args=(c,),daemon=True)
thread.start()

def restart():
	move_event.set()
	thread = threading.Thread( target=paintFrames,args=(c,),daemon=True)
	thread.start()

mainloop()