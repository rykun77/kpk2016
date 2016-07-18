import Tkinter

def button1_command():
    print('Button 1 default command. ')

def print_hello(event):
    print ('Hello!')
    print (event.num)
    print(event.x, event.y)
    me = event.widget
    if me== button1:
        print ('Hello!')
    elif me == button2:
        print ('You pressed button 2!')
    else:
        raise ValueError()

def init_main_window():
    global root, button1, button2, label, text, ruler
    root = Tkinter.Tk()

    button1 = Tkinter.Button(root, text="Button 1", command=button1_command)
    button1.bind("<Button>", print_hello)

    button2 = Tkinter.Button(root, text="Button 2")
    button2.bind("<Button>", print_hello)

    variable = Tkinter.IntVar(0)
    label = Tkinter.Label(root, textvariable=variable)
    scale = Tkinter.Scale(root, orient=Tkinter.HORIZONTAL, length=300,from_=0,to=100,tickinterval=10,
               resolution=5, variable=variable)
    text = Tkinter.Entry(root, textvariable = variable)

    for obj in button1, button2, label, scale, text:
        obj.pack()

if __name__  =="__main__":
    init_main_window()

    root.mainloop()
