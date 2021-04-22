import tkinter

mainWindow = tkinter.Tk()

mainWindow.title('Hello World')
mainWindow.geometry('640x400+8+400')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
# To expand vertically
# canvas.pack(side='left', fill=tkinter.Y)
# To expand horizontally, a bit different
# canvas.pack(side='left', fill=tkinter.X, expand=True)
# To expand both vertically and horizontally
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

# add buttons to a canvas
canvas.pack(side='top')
button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")

button1.pack(side='top', anchor='n')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='e')




mainWindow.mainloop()

