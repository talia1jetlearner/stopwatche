from tkinter import*
import tkinter as tk
window= Tk()
hour= StringVar()
minute= StringVar()
second= StringVar()
def submit():
    #try and except is used when the user writes something wrong but instead of the code stopping,they get an error message
    pass
window.geometry("300x150")
window.title("stopwatch")
hours= Entry(window)
hours.place(x=20,y=10)
minutes= Entry(window)
minutes.place(x=100,y=10)
seconds= Entry(window)
seconds.place(x=180,y=10)
enter= Button(window,text="Set timer")
enter.place(x=100,y=120)
window.mainloop()