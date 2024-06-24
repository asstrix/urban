import ttkbootstrap as tb
from tkinter import PhotoImage
import tkinter as tk


class App:
    def __init__(self, root_):
        self.root = root_
        self.root.title("ModestPass")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.style = tb.Style()
        self.scale_val = tb.Label(font=16)
        self.scale_val.place(x=100, y=70)
        self.create_widgets()

    def create_widgets(self):
        # Separator between left and right sides
        tb.Separator(orient='vertical', style="primary").place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.4)

        # Left side

        # Main Label
        tb.Label(text=f'Password Generator', font=("Helvetica", 16)).place(x=20, y=10)
        tb.Label(text=f'{"Create unique password": ^46}', font=("Helvetica", 8)).place(x=20, y=35)

        # Labels of toggle buttons
        tb.Label(text=f' Capital letters{"ABC": >12}', font=("Helvetica", 12)). place(x=45, y=126)
        tb.Label(text=f' Numbers{"123": >22}', font=("Helvetica", 12)).place(x=45, y=156)
        tb.Label(text=f' Special symbols{"!&*": >11}', font=("Helvetica", 12)).place(x=45, y=186)
        self.update_scale_label(16)
        # Password length scale
        tb.Scale(from_=0, to=100, value=16, orient='horizontal', length=200, command=self.update_scale_label).place(x=20, y=100)

        # Capital letters, Numbers, Special symbols
        tb.Checkbutton(style="Roundtoggle.Toolbutton", variable=tb.IntVar(value=1)).place(x=20, y=130)
        tb.Checkbutton(style="Roundtoggle.Toolbutton", variable=tb.IntVar(value=1)).place(x=20, y=160)
        tb.Checkbutton(style='Roundtoggle.Toolbutton', variable=tb.IntVar(value=1)).place(x=20, y=190)

        # Right side

        # Label of generated password
        tb.Label(text='Password1!').place(x=350, y=70)

        # Copy button
        copy_image = PhotoImage(file="copy.png")
        tb.Button(root, image=copy_image, command=lambda: print("Button clicked!"), width=35, height=35).place(x=350, y=90)

        # Regenerate button
        regen_image = PhotoImage(file="regen.png")
        tb.Button(root, image=regen_image, command=lambda: print("Button clicked!")).place(x=370, y=90)

    def update_scale_label(self, val):
        self.scale_val.config(text=round(float(val)))


if __name__ == "__main__":
    root = tb.Window()
    app = App(root)
    root.mainloop()