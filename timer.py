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

running = False
counter = 0

class Content:
    def __init__(self, root):

        def stopwatch():
            global sw_start
            global count

            def count():
                if running:
                    global counter, display

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
            running = True

        def sw_stop():
            global running
            running = False

        def sw_reset():
            global counter
            counter = 0

            if running == False:
                lbl['text']='00:00:00'

            else:
                lbl['text']='Starting...'
            

        lbl = Label(text='00:00:00')
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
    cnt = Content(root)
    root.mainloop()

if __name__ == '__main__':
    main()

