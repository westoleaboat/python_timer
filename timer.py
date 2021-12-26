from tkinter import *
from tkinter import Frame, Tk
import math
from datetime import  time
from tkinter import ttk

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
# lap data
lap_count = 1

#lst = []
# content class
class Content:
    def __init__(self, root):

        # stopwatch config
        def stopwatch():
            global sw_start
            global count

            def count():
                if running:
                    global counter, display, string

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
            global lap_count
            # reset counter
            counter = 0
            lap_count = 1
            lap_text['state']='normal'
            lap_text.delete("1.0", "end")

            lap_text['state']='disabled'

            # if reset when stop
            if running == False:
                lbl['text']='00:00:00'

            # if reset while running
            else:
                lbl['text']='Starting...'

        def sw_lap():
            global lst
            global lap_count
            # if counter = 0, no lap 
            if counter == 0:
                print('stopwatch no running!')

            # if timer is not running but not 0
            elif running == False and counter != 0:
                print(string +  ' ' + 'stopwatch is not running!')

            # print lap time
            else:
                add_lap()
                lap_count += 1


        def add_lap():
            #print(lap_count)
            
            lap_text['state']="normal"
            # define text value to get
            value = ("\t" + str(lap_count) + "\t" + str(display) + '\n')
            #print(str(value))
            lap_text.insert(END, value)
            lap_text['state']="disabled"
        
        # stopwatch display labelframe container
        display_lf = LabelFrame()
        display_lf.pack()

        # lap info container 
        lap_lf = LabelFrame(width=10, height=10)
        lap_lf.pack()

        #lap info titles
        lap_text_title = Label(lap_lf, text='LAP \t  TIME', font='bold')
        lap_text_title.pack(side=TOP)#, anchor="w")

        # lap info
        lap_text = Text(lap_lf, state='disabled', font='bold', width=30, height=10)
        lap_text.pack(anchor='center')#fill=X)
            

        # timer label
        lbl = Label(display_lf, text='00:00:00', font='Verdana 30', bg='#ffffff', width=10)
        lbl.pack()

        # start - stop - reset & lap buttons
        btn_start = Button(display_lf, text='Start', command=sw_start)
        btn_start.pack(side='left')

        btn_stop = Button(display_lf, text='Stop', command=sw_stop)
        btn_stop.pack(side='left')

        btn_reset = Button(display_lf, text='Reset', command=sw_reset)
        btn_reset.pack(side='left')

        btn_lap = Button(display_lf, text='Lap', command=sw_lap)
        btn_lap.pack(side='left')


        


        stopwatch()




def main():
    # define GUI frame
    root = Tk()
    # title
    root.title("Simple Python Timer")
    # app screen size
    root.geometry('300x300+950+540')
    # no resize app
    root.resizable(0,0)
    # show content
    cnt = Content(root)
    # call loop
    root.mainloop()


if __name__ == '__main__':
    main()

