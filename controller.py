## methods for communicating between View and back-end Model.

from tkinter import *
import View
import config

class Control:
    def __init__(self):
        self.root = Tk()
        self.view = View.View(self.root)
        self.root.mainloop()

    @staticmethod
    def update_api_key():
    ## make a new tk window which prompts for the new api key...call the
    ## setter function to update config.json.

        def set_key():
            # function called when submit button is pressed.
            config.set_transloc_key(text.get())
            newwindow.destroy()

        newwindow = Toplevel()
        label = Label(newwindow, text="enter your new api key:") 
        label.grid()

        text = Entry(newwindow) 
        text.grid()

        button = Button(newwindow, text="Submit", command=set_key)
        button.grid()
    


    

if __name__ == '__main__':
    c = Control() 