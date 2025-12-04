import tkinter as Tkinter
from datetime import datetime

counter = 0
running = False
//added a comment here.
def counter_label(label):
    def count():
        global counter
        if running:
            if counter == 0:
                display = '⏱️ Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                display = '⏰ ' + tt.strftime('%H:%M:%S')
            label.config(text=display)
            counter += 1
            label.after(1000, count)
    count()

def start_pause_resume(label):
    global running
    if not running:  # Means currently stopped or paused, so start or resume
        running = True
        counter_label(label)
        start_pause_btn.config(text='⏸️ Pause', bg='#ffd1d1')
        stop.config(state='normal')
        reset.config(state='disabled')
    else:  # currently running, so pause
        running = False
        start_pause_btn.config(text='▶️ Resume', bg='#d1ffd1')
        reset.config(state='normal')

def Stop():
    global running, counter
    running = False
    counter = 0
    label.config(text='🔁 00:00:00')
    start_pause_btn.config(text='▶️ Start', bg='#d1ffd1', state='normal')
    stop.config(state='disabled')
    reset.config(state='normal')

def Reset(label):
    global counter
    counter = 0
    label.config(text='🔁 00:00:00')
    reset.config(state='disabled')

# UI Setup
root = Tkinter.Tk()
root.title("✨ Stopwatch ⏳")
root.config(bg="#f0f8ff")
root.minsize(width=300, height=100)

label = Tkinter.Label(root, text='⏱️ Ready!', fg='#333', bg="#f0f8ff", font='Helvetica 28 bold')
label.pack(pady=10)

f = Tkinter.Frame(root, bg="#f0f8ff")

start_pause_btn = Tkinter.Button(f, text='▶️ Start', width=10, font='Helvetica 10 bold', bg='#d1ffd1',
                               command=lambda: start_pause_resume(label))
stop = Tkinter.Button(f, text='⏹️ Stop', width=10, font='Helvetica 10 bold', bg='#ffd1d1', state='disabled',
                      command=Stop)
reset = Tkinter.Button(f, text='🔄 Reset', width=10, font='Helvetica 10 bold', bg='#d1e0ff', state='disabled',
                      command=lambda: Reset(label))

f.pack()
start_pause_btn.pack(side='left', padx=5)
stop.pack(side='left', padx=5)
reset.pack(side='left', padx=5)

root.mainloop()
