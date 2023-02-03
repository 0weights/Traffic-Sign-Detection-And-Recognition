import tkinter as tk
from tkinter import filedialog as fd
from Traffic_Sign_Detection.prediction import predict
import tkinter.font as font
import cv2

# master form
master = tk.Tk()
master.geometry('700x700')
master.attributes('-fullscreen', True)
master.bind("<F11>", lambda event: master.attributes("-fullscreen",
                                                     not master.attributes("-fullscreen")))
master.bind("<Escape>", lambda event: master.attributes("-fullscreen", False))
master.title('Traffic Sign Detection')


def make_prediction():
    path = fd.askopenfilename(initialdir="../Desktop", title="Select A File")
    cv_img = cv2.imread(path, 0)
    predict(cv_img, path, master)


# browse button
button = tk.Button(master, width=10, text="Browse An Image", command=make_prediction)
button['font'] = font.Font(family='Courier', size=30, weight='bold')
button.pack(fill="x", padx="10", pady="10")

master.mainloop()
