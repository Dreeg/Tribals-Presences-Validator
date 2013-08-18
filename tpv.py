from Tkinter import *
import tkFileDialog as fd

datac = ''
ringrc = ''
data = ''
dataf = []
datafile = ''
elenco = {}
elencof = []

class TPV:
    def __init__(self, Genitore):
        self.mioGenitore = Genitore
        self.std = StringVar()
        self.std.set("gg/mm/aaaa")

        self.quadro1 = Frame(Genitore)
        self.quadro1["background"] = "#CCBA96"
        self.quadro1.pack(expand=1)

        self.savel = Label(self.quadro1, text = "Salva su File",
                             background="orange")
        self.savel.bind("<Button-1>", self.pulsSave)
        self.savel.pack(pady=5, side = BOTTOM)
        self.lelenco = Text(self.quadro1, width=30, height=5)
        self.lelenco.pack(padx=10, pady=5, side= BOTTOM)

        self.labelt = Label(self.quadro1, text="Tribals Presence Validator", font=("Lucida", 10 ,"bold"))
        self.labelt.pack(pady=10)

        self.labeld = Label(self.quadro1, text="Data")
        self.labeld.pack()
        self.entryd = Entry(self.quadro1, textvariable=self.std, width=30)
        self.entryd.bind("<Button-1>", self.entrydPress)
        self.entryd.pack(pady=5)

        self.labelr = Label(self.quadro1, text="Ringraziamenti")
        self.labelr.pack()
        self.ringr = Text(self.quadro1, width=30, height=5)
        self.ringr.pack(padx=10, pady=5)

        self.puls1 = Button(self.quadro1)
        self.puls1.configure(text = "Calcola",
                             background="orange", borderwidth=1)
        self.puls1.bind("<Button-1>", self.puls1Press1)
        self.puls1.pack(padx=5, pady=7, expand=1, fill="x")
        
        self.laelenco = Label(self.quadro1, text="Elenco Presenze")
        self.laelenco.pack()

    def puls1Press1(self, evento):
        global datac
        global ringrc

        datac = self.std.get()
        ringrc = self.ringr.get('1.0',END)

        data()
        conta_presenze()
        for x in elencof:
            x = x + "\n"
            self.lelenco.insert(END, x)

        #self.clipboard_clear()
        #self.clipboard_append(presenze_bbcode())
        
        self.puls1["background"] = "green"

    def pulsSave(self, evento):
        path = fd.asksaveasfilename(title="Dove Salvare",filetypes=[('text', '*.txt')])
        if len(path) > 0:
            if path[-4:] != ".txt":
                path = path+".txt"
            with open(path,'w') as f:
                for x in elencof:
                    f.write(x+'\n')
        self.savel["background"] = "green"
        self.savel["text"] = "File Salvato!"
            
    def entrydPress(self, evento):
        self.std.set("")

def data():
    global data
    global dataf
    global datafile
    global datac
    global ringrc
    data = datac
    dataf = data.split("/")
#    while(len(dataf) < 2):
#      data = raw_input("Inserisci la data nel formato corretto: ")
#      dataf = data.split("/")
#    while(dataf[0] > 1 and dataf[0] < 31 and dataf[1] > 1 and dataf[1] < 12):
#      data = raw_input("Inserisci la data nel formato corretto: ")
#      dataf = data.split("/")

    if len(dataf) == 2:
        datafile = dataf[1] + "_" + dataf[0]
    else:
        datafile = dataf[2] + "_" + dataf[1] + "_" + dataf[0]

def conta_presenze():
    global elenco
    global elencof
    presenze = ringrc
    presenzef = presenze.lower().split(",")
    
    for p in presenzef:
        f = False
        cp = ''
        vp = ''
        for x in range(len(p)):
            if p[x] == "(":
                break
            else:
                cp += p[x]
        cp = cp.strip()
        cp = cp.lower()
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
