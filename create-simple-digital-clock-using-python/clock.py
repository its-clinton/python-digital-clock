import os
import time
from tkinter import *
root = Tk()
root.title('Digital clock')

def get_time():
    current_time = time.strftime('%H:%M:%S %p')
    clock.configure(text = current_time)
    clock.after(10, get_time)
Label(root,font=('verdana', 16), bg='blue', fg='white')
clock = Label(root, font=('verdana', 50), bg='blue', fg='white')
get_time()
clock.pack()
root.mainloop()
