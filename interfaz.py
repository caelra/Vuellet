from tkinter import *  # Comes Defalut With Python3
from tkinter import filedialog as fd
from tkinter import messagebox as ms
from tkinter import ttk
import PIL  # Install Using PIP
from PIL import ImageTk, Image
from sistemaDifuso import sistemaDifuso
import pyperclip as cp
from threading import Thread
import db


class application:
    def __init__(self, master):
        self.master = master
        self.c_size = (700, 500)
        self.setup_gui(self.c_size)
        self.img = None

    def setup_gui(self, s):
        self.canvas = Canvas(self.master, height=s[1], width=s[0],
                             bg='black', bd=10, relief='ridge')
        self.canvas.pack()
        txt = '''

                                                  carga tu imagen
        '''
        self.wt = self.canvas.create_text(
            s[0]/2-270, s[1]/2, text=txt, font=('', 30), fill='white')
        f = Frame(self.master, bg='white', padx=10, pady=10)
        Button(f, text='Abrir Imagen', bd=2, fg='white', bg='black',
               font=('', 15), command=self.make_image).pack(side=LEFT)
        f.pack()
        self.status = Label(self.master, text='Current Image: None', bg='gray',
                            font=('Roboto', 15), bd=2, fg='black', relief='sunken', anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def copyColor(self, color):
        cp.copy(color)

    def proseso(self, File):
        paleta_de_colores = sistemaDifuso(File)
        print(paleta_de_colores)
        hex_colors = []
        for color in paleta_de_colores:
            colorrgb = color[::-1]
            mycolor = "#%02x%02x%02x" % (tuple(colorrgb))
            print(mycolor)
            hex_colors.append(mycolor)
            Label(self.master, text=mycolor, fg='white', pady=50, bg=mycolor, font=(
                'Ubuntu', 12)).pack(side=RIGHT, padx=0, pady=30)

        db_con = db.DataBase()
        print(hex_colors)
        db_con.create_color(str(hex_colors))
        db_con.select_all_colors()

    def make_image(self):
        try:
            File = fd.askopenfilename()
            Thread(target=self.proseso, args=(File,)).start()
            self.pilImage = Image.open(File)
            re = self.pilImage.resize((700, 500), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            self.canvas.delete(ALL)
            self.canvas.create_image(self.c_size[0]/2+10, self.c_size[1]/2+10,
                                     anchor=CENTER, image=self.img)
            self.status['text'] = 'Current Image:'+File

        except:
            ms.showerror('Error!', 'Este tipo de archivo no puede ser leido')
