import tkinter
import colorgame
root1 = tkinter.Tk()

#def start():

def login_button_click(self, event=None):
    self.destroy()
    colorgame.HomeWindow()



# set the title
root1.title("COLORGAME")

# set the size
root1.geometry("375x200")
namelable = tkinter.Label(root1, text="Enter your name",
                             font=('Helvetica', 12))
namelable.pack()

# add a score label


e = tkinter.Entry(root1)
#root1.bind('<Return>',)
e.pack()
e.focus_set()

button1 = tkinter.Button(root1, text="Press enter to start",
                           font=('Helvetica', 12))
button1.pack()
button1.bind('<Return>', login_button_click)




# start the GUI
root1.mainloop()