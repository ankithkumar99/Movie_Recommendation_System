from tkinter import *
from algorithm import *


class Gui(Tk, Recommendation):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.title("Noel's Ktm")
        self.geometry('800x600')
        #self.iconbitmap('icon.ico')
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.xy = []

        self.photo2 = PhotoImage(file='new.png')
        self.bg_image = Label(self, image=self.photo2, bg='white')
        self.bg_image.place(relwidth=1, relheight=1)

        self.temp = Label(self, text='Enter the movie you watched recently :', bg='#ffffff', fg='#777777',
                          anchor=W, font=('Helvetica', 12, 'italic'))
        self.temp.place(relx=0.08, rely=0, relwidth=0.6, relheight=0.06)

        self.e = Entry(self, textvariable=self.var1, font=('Calibri', 16), bg='#eeeeee', fg='#000000')
        self.e.place(relx=0.08, rely=0.05, relwidth=0.6, relheight=0.06)

        self.submit = Button(self, text='submit', command=self.ak, font=('Calibri', 12), bg='#eeeeee')
        self.submit.place(relx=0.7, rely=0.05, relwidth=0.1, relheight=0.06)

    def ak(self):
        try:
            self.var2 = self.var1.get().lower()
            Recommendation.__init__(self, self.var2)
            self.xy = self.req_list
            temp1 = Label(self, text='Then, you might like to watch :', bg='#ffffff', fg='#777777', anchor=W,
                          font=('Helvetica', 12, 'italic'))
            temp1.place(relx=0.08, rely=0.12, relwidth=0.3, relheight=0.06)

            mylabel0 = Label(self, text=self.xy[0], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel0.place(relx=0.09, rely=0.18, relwidth=0.35, relheight=0.04)

            mylabel1 = Label(self, text=self.xy[1], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel1.place(relx=0.09, rely=0.24, relwidth=0.35, relheight=0.04)

            mylabel2 = Label(self, text=self.xy[2], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel2.place(relx=0.09, rely=0.30, relwidth=0.35, relheight=0.04)

            mylabel3 = Label(self, text=self.xy[3], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel3.place(relx=0.09, rely=0.36, relwidth=0.35, relheight=0.04)

            mylabel4 = Label(self, text=self.xy[4], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel4.place(relx=0.09, rely=0.42, relwidth=0.35, relheight=0.04)

            mylabel5 = Label(self, text=self.xy[5], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel5.place(relx=0.09, rely=0.48, relwidth=0.35, relheight=0.04)

            mylabel6 = Label(self, text=self.xy[6], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel6.place(relx=0.09, rely=0.54, relwidth=0.35, relheight=0.04)

            mylabel7 = Label(self, text=self.xy[7], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel7.place(relx=0.09, rely=0.60, relwidth=0.35, relheight=0.04)

            mylabel8 = Label(self, text=self.xy[8], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel8.place(relx=0.09, rely=0.66, relwidth=0.35, relheight=0.04)

            mylabel9 = Label(self, text=self.xy[9], bg='#ffffff', anchor=W, font=('Calibri', 14))
            mylabel9.place(relx=0.09, rely=0.72, relwidth=0.35, relheight=0.04)

        except AttributeError:
            temp1 = Label(self, text='That movie does not exist!!', bg='#ffffff', fg='#777777', anchor=W,
                          font=('Helvetica', 12, 'italic'))
            temp1.place(relx=0.08, rely=0.12, relwidth=0.3, relheight=0.06)


window = Gui()
window.mainloop()
