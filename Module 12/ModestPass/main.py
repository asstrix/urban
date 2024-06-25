import ttkbootstrap as tb, secrets, string


class App:
    def __init__(self, root_):
        self.root = root_
        self.root.title("ModestPass")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.style = tb.Style()

        # Separator between left and right sides
        self.sep = tb.Separator(self.root, orient='vertical', style="primary")
        self.sep.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.4)

        # ######################### Left side #########################

        # Main Label
        tb.Label(self.root, text=f'Password Generator', font=("Helvetica", 16)).place(x=20, y=10)
        tb.Label(self.root, text=f'{"Create unique password": ^46}', font=("Helvetica", 8)).place(x=20, y=35)

        # Labels of toggle buttons
        tb.Label(self.root, text=f' Capital letters{"ABC": >12}', font=("Helvetica", 12)).place(x=45, y=126)
        tb.Label(self.root, text=f' Numbers{"123": >22}', font=("Helvetica", 12)).place(x=45, y=156)
        tb.Label(self.root, text=f' Special symbols{"!&*": >11}', font=("Helvetica", 12)).place(x=45, y=186)

        # Password length scale
        self.scale = tb.Scale(self.root, from_=8, to=32, value=16, orient='horizontal', length=200,
                              command=self.update_scale)
        self.scale.place(x=20, y=100)
        self.scale_val = tb.Label(font=16)
        self.scale_val.place(x=100, y=70)
        self.update_scale(16)

        # Letters, Numbers, Special symbols
        self.check_cap = tb.IntVar(value=1)
        self.cap = tb.Checkbutton(self.root, style="Roundtoggle.Toolbutton", variable=self.check_cap)
        self.cap.place(x=20, y=130)
        self.check_num = tb.IntVar(value=1)
        self.num = tb.Checkbutton(self.root, style="Roundtoggle.Toolbutton", variable=self.check_num)
        self.num.place(x=20, y=160)
        self.check_spec = tb.IntVar(value=1)
        self.spec = tb.Checkbutton(self.root, style='Roundtoggle.Toolbutton', variable=self.check_spec)
        self.spec.place(x=20, y=190)

        # ######################### Right side #########################

        # Password widget
        self.pwd = tb.Text(self.root, font=12, width=25, height=2)
        self.pwd.config(highlightthickness=0, borderwidth=0)
        self.pwd.tag_configure('center', justify='center')
        self.pwd.place(x=255, y=60)

        # Copy button
        tb.Button(self.root, text='Copy to clipboard', style='online', command=lambda: self.copy_to_clipboard()).place(
            x=320, y=180)

        # Regenerate button
        tb.Button(self.root, text='Regenerate', command=lambda: self.generate_pwd(self.check_cap.get(),
                                                                                  self.check_num.get(),
                                                                                  self.check_spec.get(),
                                                                                  self.scale.get())).place(x=340, y=220)
        # Generate pwd at initial startup
        self.generate_pwd(1, 1, 1, 16)

    def update_scale(self, val):
        self.scale_val.config(text=round(float(val)))

    def generate_pwd(self, let, dig, spec, length):
        if let and dig and spec:
            pwd = string.ascii_letters + string.digits + "!@#$%^&*()_+|\\?/"
        elif let and dig:
            pwd = string.ascii_letters + string.digits
        elif dig and spec:
            pwd = string.digits + "!@#$%^&*()_+|\\?/"
        elif let and spec:
            pwd = string.ascii_letters + "!@#$%^&*()_+|\\?/"
        else:
            self.pwd.delete('1.0', tb.END)
            self.pwd.insert(tb.END, 'Password must contain at least 2 type of symbols', 'center')
            return
        self.pwd.delete('0.1', tb.END)
        self.pwd.insert(tb.END, ''.join(secrets.choice(pwd) for i in range(int(length))), 'center')

    def copy_to_clipboard(self):
        password = self.pwd.get("1.0", tb.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()


if __name__ == "__main__":
    root = tb.Window()
    app = App(root)
    root.mainloop()
