keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

# mainWindowPadding = 8
# mainWindow = tkinter.Tk()
#
# mainWindow.title('Calculator')
# mainWindow.geometry('640x400-8-200')
#
# result = tkinter.Entry(mainWindow)
# result.grid(row=0, column=0, sticky='nsew')
#
# keyPad = tkinter.Frame(mainWindow)
# keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    print('*' * 40)
    print(f"col = {col} row={row}")
    for key in keyRow:
        print(key)
        # tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row +=1
    print(f"row = {row}")