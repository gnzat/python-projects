from tkinter import Label, Tk 
import time
#define title and size of application
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
#for it to be resizable set to (1,1), for it to be fixed set to (0,0)
app_window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25
#define label of clock application
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)
#define main function of the clock
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()