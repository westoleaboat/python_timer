from tkinter import *
from tkinter import Frame, Tk
import math
from datetime import  time

# main content frame
class Main_content(Frame):
    def __init__(self, root):
        super().__init__()

        self.initUI()

    def initUI(self):

        # content frame inside main
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

# recognize if timer is running
running = False
# timer at zero
counter = 0

# content class
class Content:
    def __init__(self, root):

        # stopwatch config
        def stopwatch():
            global sw_start
            global count

            def count():
                if running:
                    global counter, display

                    # manage initial delay
                    if counter == 0:
                        display = 'Starting...'
                    else:

                        seconds = counter % 60
                        minutes = (counter // 60) % 60
                        hours = (counter // (60 * 60)) % (60 * 60)

                        dt = time(second=seconds, minute=minutes, hour=hours)
                        string = dt.isoformat(timespec = 'auto')
                        display = string

                    lbl['text']=display

                    counter += 1

                root.after(1000, count)

            count()

        def sw_start():
            global running
            global display
            # run counter
            running = True

        def sw_stop():
            global running
            # stop counter
            running = False

        def sw_reset():
            global counter
            # reset counter
            counter = 0

            # if reset when stop
            if running == False:
                lbl['text']='00:00:00'

            # if reset while running
            else:
                lbl['text']='Starting...'
            

        # timer label
        lbl = Label(text='00:00:00', bg='#ffffff', width=30)
        lbl.pack()

        btn_start = Button(text='Start', command=sw_start)
        btn_start.pack()

        btn_stop = Button(text='Stop', command=sw_stop)
        btn_stop.pack()

        btn_reset = Button(text='Reset', command=sw_reset)
        btn_reset.pack()

        stopwatch()



def main():
    root = Tk()
    # title
    root.title("Simple Python timer")
    # app size
    root.geometry('300x200+950+540')
    # no resize app
    root.resizable(0,0)
    # show content
    cnt = Content(root)
    # call loop
    root.mainloop()


if __name__ == '__main__':
    main()

