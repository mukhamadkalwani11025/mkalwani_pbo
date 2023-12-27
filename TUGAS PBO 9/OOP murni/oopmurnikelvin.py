from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmKelvin:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES) 
        Label(mainFrame, text='Kelvin:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celsius:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=0, column=1, padx=5, pady=5)  

        self.txtCelsius = Entry(mainFrame) 
        self.txtCelsius.grid(row=2, column=1, padx=5, pady=5) 

        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=3, column=1, padx=5, pady=5) 

        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=4, column=1, padx=5, pady=5) 
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def get_celsius(self, suhu):
        val = suhu - 273
        return val
    
    def get_fahrenheit(self, suhu):
        val = (9/5 * (suhu - 273)) + 32
        return val
    
    def get_reamur(self, suhu):
        val = (4/5 * (suhu - 273)) 
        return val

    def onHitung(self):
        # Suhu dalam Celsius
        suhu_kelvin = self.txtKelvin.get()
        C = self.get_celsius(float(suhu_kelvin))
        self.txtCelsius.delete(0, END)
        self.txtCelsius.insert(END, str(C))

        # Suhu dalam Fahrenheit
        F = self.get_fahrenheit(float(suhu_kelvin))
        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(F))

        # Suhu dalam Reamur
        R = self.get_reamur(float(suhu_kelvin))
        self.txtReamur.delete(0, END)
        self.txtReamur.insert(END, str(R))
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()            


if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmKelvin(root, "Program Konversi Suhu Kelvin")
    root.mainloop() 
