from tkinter import *
import time
import _thread

c = Canvas(width=460,height=460,bg='grey80')
c.pack()

oval = c.create_oval(30,10,130,80)
rect = c.create_rectangle(180,10,280,80)
trian = c.create_polygon(330,80,380,10,430,80, fill='grey80',outline="black")

c.move(rect,0,150)
c.itemconfig(trian,outline="red",width=3)
c.coords(oval,300,200,450,450)

def mooove(event):
    c.move(rect,0,2)
c.bind('<Button-1>',mooove)

oval2 = c.create_oval(30,10,130,80,tag="group1")
c.create_line(10,100,450,100,tag="group1")

def color(event):
    if ( c.itemcget(oval2, "fill") == "red" ):
        c.itemconfig('group1',fill="black",width=1)
        c.itemconfig(oval2,fill="")
    else: c.itemconfig('group1',fill="red",width=3)
c.bind('<Button-3>',color)

def clean(event):
    c.delete(oval, trian)
c.bind('<Button-2>',clean)

c2 = Canvas(width=460,height=100,bg='grey80')
c2.pack()

oval = c2.create_oval(30,10,130,80,fill="orange")
c2.create_rectangle(180,10,280,80,tag="rect",fill="lightgreen")
trian = c2.create_polygon(330,80,380,10,430,80,fill='white',outline="black")

def oval_func(event):
    c2.delete(oval)
    _thread.start_new_thread(f1, ())
def rect_func(event):
    c2.delete("rect")
    c2.create_text(180,10,text="Здесь был\nпрямоугольник",anchor="nw")
def triangle(event):
    c2.create_polygon(350,70,380,20,410,70,fill='yellow',outline="black")
def f1():
    while True:
        oval = c2.create_oval(30,10,130,80,fill="red")
        time.sleep(0.5)
        c2.delete(oval)
        time.sleep(0.5)
    _thread.exit()

c2.tag_bind(oval,'<Button-1>',oval_func)
c2.tag_bind("rect",'<Button-1>',rect_func)
c2.tag_bind(trian,'<Button-1>',triangle)

mainloop()
