import tkinter as tk
from subprocess import run, PIPE

def led_on():
    cp = run(['python3', 'client_on.py'], stdout=PIPE, encoding='utf-8')
    print(cp.stdout)

def led_off():
    cp = run(['python3', 'client_off.py'], stdout=PIPE, encoding='utf-8')
    print(cp.stdout)

class App(tk.Frame):
    """Main application"""
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        # Create 'on' button.
        self.on_btn = tk.Button(self, fg='blue', text='LED On.', command=led_on)
        self.on_btn.pack(side='top')
        self.off_btn = tk.Button(self, text='LED Off.', command=led_off)
        self.off_btn.pack(side='bottom')

root=tk.Tk()
app=App(root)
app.mainloop()
