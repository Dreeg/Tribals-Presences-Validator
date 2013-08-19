from Tkinter import *
import tkFileDialog as fd

datac = ''
ringrc = ''
datai = ''
dataf = []
datafile = ''
dataerror = False
elenco = {}
elencof = []

class TPV:
    def __init__(self, Genitore):
        self.strdata = StringVar()
        self.strdata.set(" gg/mm/aaaa")
        self.mioGenitore = Genitore

        self.quadro1 = Frame(Genitore)
        self.quadro1.pack(expand=1)
        
        self.ltitle = Label(self.quadro1, text="Tribals Presences Validator", font=("Lucida", 11 ,"bold"))
        self.ltitle.pack(pady=5)
        self.ldataerror = Label(self.quadro1, text="", fg="red")
        self.ldataerror.pack(pady=5)
        self.ldata = Label(self.quadro1, text="Data")
        self.ldata.pack()
        self.edata = Entry(self.quadro1, textvariable=self.strdata, width=30)
        self.edata.bind("<Button-1>", self.edataPress)
        self.edata.pack(pady=5)
        self.lringr = Label(self.quadro1, text="Ringraziamenti")
        self.lringr.pack()
        self.tringr = Text(self.quadro1, width=30, height=5)
        self.tringr.bind("<Double-Button-1>", self.tringrDel)
        self.tringr.bind("<Button-3>", self.tringrPaste)
        self.tringr.pack(padx=10, pady=5)
        self.lcalc = Label(self.quadro1, text="Calcola", background="orange")
        self.lcalc.bind("<Button-1>", self.lcalcPress)
        self.lcalc.pack(padx=5, pady=7, expand=1, fill="x", side=BOTTOM)
        
        
        self.quadro2 = Frame(Genitore)
        self.quadro2.pack(expand=1)
        
	self.lelenco = Label(self.quadro2, text="Elenco Presenze")
	self.lelenco.pack()
	self.sbelenco = Scrollbar(self.quadro2, orient=VERTICAL)
	self.telenco = Text(self.quadro2, width=30, height=5)
	self.telenco.bind("<Double-Button-1>", self.telencoDel)
	self.telenco.bind("<Button-3>", self.copyele)
	self.telenco.config(yscrollcommand=self.sbelenco.set)
	self.sbelenco.config(command=self.telenco.yview)
	self.sbelenco.pack(ipady=10, padx=5, pady=5, side=RIGHT)
	self.telenco.pack(padx=5, pady=5, side=LEFT)


	self.quadro3 = Frame(Genitore)
	self.quadro3.pack(expand=1)
	
	self.lsavefile = Label(self.quadro3, text = "Salva su File", background="orange")
        self.lsavefile.bind("<Button-1>", self.lSave)
        self.lsavefile.pack(padx=5, pady=5, side=LEFT)
        self.lsavebb = Label(self.quadro3, text = "Copia BB-Code", background="orange")
        self.lsavebb.bind("<Button-1>", self.copybb)
        self.lsavebb.pack(padx=5, pady=5, side=RIGHT)
        self.lele = Label(self.quadro3, text = "Copia Elenco", background="orange")
        self.lele.bind("<Button-1>", self.copyele)
        self.lele.pack(padx=5, pady=5, side=BOTTOM)

    def lcalcPress(self, evento):
        global datac
        global ringrc

        datac = self.strdata.get()
        data()
        if dataerror:
            self.ldataerror["text"] = "Data Errata, ricalcola inserendo una data corretta!"
        else:
            self.ldataerror["text"] = ""
            ringrc = self.tringr.get('1.0',END)
            conta_presenze()
            self.telenco.delete('1.0',END)
            for x in elencof:
                x = x + "\n"
                self.telenco.insert(END, x)
            
        if dataerror:
            self.lcalc["background"] = "red"
        else:
            self.lcalc["background"] = "green"
            
        if self.lsavebb["background"] == "red" or self.lsavebb["background"] == "green":
            self.lsavebb["background"] = "orange"
            self.lsavebb["text"] = "Copia BB-Code"
        if self.lsavefile["background"] == "red" or self.lsavefile["background"] == "green":
            self.lsavefile["background"] = "orange"
            self.lsavefile["text"] = "Salva su File"
        if self.lele["background"] == "red" or self.lele["background"] == "green":
            self.lele["background"] = "orange"
            self.lele["text"] = "Copia Elenco"

    def lSave(self, evento):
        if len(elencof)>0:
            path = fd.asksaveasfilename(title="Dove Salvare",filetypes=[('text', '*.txt')])
            if len(path) > 0:
                if path[-4:] != ".txt":
                    path = path+".txt"
                with open(path,'w') as f:
                    for x in elencof:
                        f.write(x+'\n')
            self.lsavefile["background"] = "green"
            self.lsavefile["text"] = "File Salvato!"
        else:
            self.lsavefile["background"] = "red"
            self.lsavefile["text"] = "Nulla da Salvare"
            
    def edataPress(self, evento):
        self.strdata.set("")

    def copybb(self, evento):
        if len(elencof)>0:
            self.lsavebb["background"] = "green"
            self.lsavebb["text"] = "BB-Code copiato!"
            self.mioGenitore.clipboard_clear()
            self.mioGenitore.clipboard_append(presenze_bbcode())
            if self.lele["background"] == "green":
                self.lele["background"] = "orange"
                self.lele["text"] = "Copia Elenco"
        else:
            self.lsavebb["background"] = "red"
            self.lsavebb["text"] = "Nulla da copiare"

    def copyele(self,evento):
        if len(elencof)>0:
            self.lele["background"] = "green"
            self.lele["text"] = "Elenco copiato!"
            self.mioGenitore.clipboard_clear()
            self.mioGenitore.clipboard_append(self.telenco.get('1.0',END))
            if self.lsavebb["background"] == "green":
                self.lsavebb["background"] = "orange"
                self.lsavebb["text"] = "Copia BB-Code"
        else:
            self.lele["background"] = "red"
            self.lele["text"] = "Nulla da copiare"
                       
    def tringrPaste(self, evento):
        text = self.mioGenitore.clipboard_get()
        self.tringr.delete('1.0', END)
        self.tringr.insert(END, text)
        if self.lcalc["background"] == "green":
            self.lcalc["background"] = "orange"

    def tringrDel(self, evento):
        self.tringr.delete('1.0', END)

    def telencoDel(self, evento):
        self.telenco.delete('1.0', END)
        if self.lsavebb["background"] == "green":
            self.lsavebb["background"] = "orange"
            self.lsavebb["text"] = "Copia BB-Code"

def data():
    global datai
    global dataf
    global datafile
    global datac
    global dataerror
    datai = datac
    dataf = datai.split("/")
    if dataf[0][0] in '0123456789' and dataf[0][1] in '0123456789' and dataf[1][0] in '0123456789' and dataf[1][1] in '0123456789':
        if len(dataf) < 2 or len(dataf) > 3 or int(dataf[0]) < 1 or int(dataf[0]) > 31 or int(dataf[1]) < 1 or int(dataf[1]) > 12:
            dataerror = True
        else:
            dataerror = False
    else:
        dataerror = True

    if len(dataf) == 2:
        datafile = dataf[1] + "_" + dataf[0]
    if len(dataf) == 3:
        datafile = dataf[2] + "_" + dataf[1] + "_" + dataf[0]

def conta_presenze():
    global elenco
    global elencof
    elenco = {}
    elencof = []
    presenze = ringrc
    presenzef = presenze.lower().split(",")
    
    for p in presenzef:
        f = False
        cp = ''    #chiave player - Elenco
        vp = ''    #valore player - Elenco
        for x in range(len(p)):
            if p[x] == "(":
                break
            else:
                cp += p[x]
        cp = cp.strip()
        " ".join(cp.split())
        for x in range(len(p)):
            if p[x] == "(":
                f = True
            if p[x] == ")":
                f = False
            if f:
                if p[x] in '0123465789.:':
                    vp += p[x]
        vp = vp.split(".")
        elenco[cp] = vp

    for p in elenco:
        if elenco[p][0] == dataf[0]:
            if elenco[p][1] == dataf[1]:
                elencof.append(p)
    elencof.sort()
    
def presenze_bbcode():
    app = ''
    for p in elencof:
        app += "[player]"+str(p)+"[/player], "
    app = "[spoiler]"+app+"[/spoiler]"
    return app
    
def presenze():
    data()
    conta_presenze()
    stampa_presenze()


def main():
    finestra = Tk()
    finestra.title("Tribals Presences Validator")
    tPV = TPV(finestra)
    finestra.mainloop()

main()
