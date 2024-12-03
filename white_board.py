from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root=Tk()
root.title("White board")
root.geometry("700x500")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

current_x=0
current_y=0
color='pink'

def locate_xy(work):
    global current_x,current_y
    current_x=work.x
    current_y=work.y

def addline(work):
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=2,fill=color)
    current_x,current_y= work.x, work.y

def show_color(new_color):
    global color
    color=new_color

def new_canvas():
    canvas.delete("all")
    display_palette()

color_box=PhotoImage(file="color_selector.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=0,y=2)

eraser=PhotoImage(file="icons8-eraser-50.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=30,y=400)

colors=Canvas(root,bg="#ffffff",width=30,height=300,bd=13)
colors.place(x=30,y=60)

canvas=Canvas(root,width=900,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=2)

def display_palette():
    id=colors.create_rectangle((20,20,40,40),fill="black")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    id=colors.create_rectangle((20,50,40,70),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

    id=colors.create_rectangle((20,80,40,100),fill="grey")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('grey'))

    id=colors.create_rectangle((20,110,40,130),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id=colors.create_rectangle((20,140,40,160),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))

    id=colors.create_rectangle((20,170,40,190),fill="pink")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('pink'))

    id=colors.create_rectangle((20,200,40,220),fill="orange")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))

    id=colors.create_rectangle((20,230,40,250),fill="brown")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown'))

    id=colors.create_rectangle((20,260,40,280),fill="beige")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('beige'))

    id=colors.create_rectangle((20,290,40,310),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))
display_palette()


canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addline)

root.mainloop()