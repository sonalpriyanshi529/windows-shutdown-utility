from tkinter import *
from tkinter import ttk

win = Tk()
win.title('Shut Down Windows-Priyanshi sahu')
win.geometry('460x270')
win.resizable(0, 0)

photo = PhotoImage(file='This PC.png')
Label(image=photo, height=100, width=100).grid(column=0, row=0)

Label(text='Windows 10', font=('arialbold', 40), fg='darkblue').grid(column=1, row=0)

photo11 = PhotoImage(file='Windows.png')
Label(image=photo11).grid(column=0, row=1)

Label(text='What do you want the computer to do ?').grid(column=1, columnspan=2, row=1, sticky=W)

Combo_var = StringVar()
v = ['Shut down', 'Restart', 'Log Off']
combo = ttk.Combobox(values=v, width=40, state='readonly', textvariable=Combo_var)
combo.grid(column=1, columnspan=2, row=2, sticky=W)
combo.current(0)

Label(text='Closes all apps and turn off the PC. ').grid(column=1, columnspan=1, row=3, sticky=W)


def action():
    a = Combo_var.get()
    if a == 'Shut down':
        import os
        os.system('shutdown /s /t 8')
    if a == 'Restart':
        import os
        os.system('shutdown /r /t 8')
    if a == 'Log Off':
        import os
        os.system('shutdown /l/t 8')


Button(win, text='Ok', command=action).grid(column=0, row=4, ipadx=22, padx=5, pady=22)


def cancel():
    exit()


Button(win, text='Cancel', command=cancel).grid(column=1, row=4, ipadx=15, padx=5, sticky=W)


def helping():
    top = Toplevel()
    top.geometry('300x150')
    top.title('Help')
    top.resizable(0, 0)

    f1 = Frame(top, borderwidth=6, bg='black')
    f1.pack(side=TOP, fill='x')

    Label(f1, text='Welcome to help', fg='white', bg='black').pack()
    Label(f1, text='You can shutdown, restart and logoff your PC here.', fg='white', bg='black').pack()
    Label(f1, text='By Priyanshi Sahu', fg='white', bg='black', font=('Comic Sans MS', 20)).pack()
    Label(f1, fg='white', bg='black').pack()
    Button(f1, text='OK', fg='white', bg='purple', command=top.destroy).pack(ipadx=20)
    Label(f1, fg='white', bg='black', font=('Comic Sans MS', 20)).pack()


Button(win, text='Help', command=helping).grid(column=1, row=4, ipadx=20)

win.mainloop()
