from tkinter import *

# initialization
root=Tk()
cw=400
ch=300

wnd=Canvas(root,width=cw,height=ch)
wnd.pack()

# custom drawing functions
def drawrect(x,y,w,h):
    wnd.create_line(x,y,x+w,y)
    wnd.create_line(x,y,x,y+h)
    wnd.create_line(x+w,y+h,x+w,y)
    wnd.create_line(x+w,y+h,x,y+h)

y=int(ch/2)
# line to divide the window horizontally
wnd.create_line(0,y,cw,y,fill="#476042")
wnd.create_text(cw/2,ch/2-10,text='python graphics')
drawrect(50,50,100,20)
drawrect(250,250,100,20)

mainloop()
