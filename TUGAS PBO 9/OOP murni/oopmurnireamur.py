from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmReamur:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES) 
        Label(mainFrame, text='Reamur:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=0, column=1, padx=5, pady=5)  

        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=2, column=1, padx=5, pady=5) 

        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=3, column=1, padx=5, pady=5) 

        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5) 
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def get_celcius(self, suhu):
        val = (5/4 * suhu)
        return val
    
    def get_fahrenheit(self, suhu):
        val = (9/4 * suhu) + 32
        return val
    
    def get_kelvin(self, suhu):
        val = (5/4 * suhu) + 273
        return val
    
    def get_reamur_from_celcius(self, suhu_celcius):
        val = (4/5 * suhu_celcius)
        return val

    def onHitung(self):
        # Suhu dalam Reamur
        suhu_reamur = self.txtReamur.get()
        
        # Suhu dalam Celcius
        C = self.get_celcius(float(suhu_reamur))
        self.txtCelcius.delete(0, END)
        self.txtCelcius.insert(END, str(C))

        # Suhu dalam Fahrenheit
        F = self.get_fahrenheit(float(suhu_reamur))
        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(F))

        # Suhu dalam Kelvin
        K = self.get_kelvin(float(suhu_reamur))
        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(K))
        
    def onKeluar(self, event=None):
        self.parent.destroy()            

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmReamur(root, "Program Konversi Suhu Reamur")
    root.mainloop() 
