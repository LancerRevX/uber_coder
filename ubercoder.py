import tkinter
import tkinter.ttk
import coding


class UberCoder(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.title('Uber Coder')
        self.geometry('512x256+256+128')
        
        tkinter.Label(self, text='Coding method').grid(row=0, columnspan=2)
        self.method_chooser = tkinter.ttk.Combobox(self)
        self.method_chooser['values'] = coding.get_methods()
        self.method_chooser.current(0)
        self.method_chooser.grid(row=1, columnspan=2)

        tkinter.Label(self, text='Text').grid(row=2, column=0)
        self.text = tkinter.Text(self)
        self.text.grid(row=3, column=0, sticky='nswe')

        tkinter.Label(self, text='Code').grid(row=2, column=1)
        self.code = tkinter.Text(self)
        self.code.grid(row=3, column=1, sticky='nswe')

        text_buttons_frame = tkinter.Frame(self)
        text_buttons_frame.grid(row=4, column=0)
        tkinter.Button(text_buttons_frame, text='Load from file').pack(side='left')
        tkinter.Button(text_buttons_frame, text='Save to file').pack(side='left')
        tkinter.Button(text_buttons_frame, text='Encode', command=self.on_encode_button_clicked).pack(side='left')
        code_buttons_frame = tkinter.Frame(self)
        code_buttons_frame.grid(row=4, column=1)
        tkinter.Button(code_buttons_frame, text='Load from file').pack(side='left')
        tkinter.Button(code_buttons_frame, text='Save to file').pack(side='left')
        tkinter.Button(code_buttons_frame, text='Decode').pack(side='left')

    def on_encode_button_clicked(self):
        method = self.method_chooser.get()
        text = self.text.get('1.0', 'end')
        code = coding.encode(method, text)
        self.code.delete('1.0', 'end')
        self.code.insert('1.0', code)


if __name__ == '__main__':
    UberCoder().mainloop()
