from tkinter import *
import time


window = Tk()
window.title("disappearing text app")
window.geometry("800x500")
last_key_press_time = time.time()


def on_key_press(event):
    global last_key_press_time
    last_key_press_time = time.time()


def check_keyboard_activity():
    if time.time() - last_key_press_time > 5:
        label.config(text="No keys were pressed in the last five seconds.")
        inputtxt.delete('1.0', END)
    else:
        label.config(text="Keyboard activity detected.")
    window.after(1000, check_keyboard_activity)


window.bind("<Key>", on_key_press)
window.after(1000, check_keyboard_activity)
inputtxt = Text(window, height=10, width=100)
Font_tuple = ("Comic Sans MS", 20, "bold")
inputtxt.configure(font=Font_tuple)
inputtxt.pack()
label = Label(window, text="")
label.pack(pady=10)




window.mainloop()
