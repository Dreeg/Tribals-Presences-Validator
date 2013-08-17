data = ''
dataf = []
datafile = ''
elenco = {}
elencof = []

def data():
    global data
    global dataf
    global datafile
    data = raw_input("Inserisci la data: ")
    dataf = data.split("/")
    while(len(dataf) < 2):
      data = raw_input("Inserisci la data nel formato corretto: ")
      dataf = data.split("/")
    while(dataf[0] > 1 and dataf[0] < 31 and dataf[1] > 1 and dataf[1] < 12):
      data = raw_input("Inserisci la data nel formato corretto: ")
      dataf = data.split("/")

    if len(dataf) == 2:
        datafile = dataf[1] + "_" + dataf[0]
    else:
        datafile = dataf[2] + "_" + dataf[1] + "_" + dataf[0]

def conta_presenze():
    global elenco
    global elencof
    presenze = raw_input("Inserisci i Ringraziamenti: ")
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
    return elencof

def stampa_presenze():
    print("\n\nPlayer presenti e attivi nel forum il "+data+": \n")
    for x in elencof:
        print x

def esporta_presenze_file():
    filename = "presenze"+datafile+".txt"
    with open(filename,'w') as f:
        for x in elencof:
            f.write(x+'\n')
    print("\nFile "+filename+" generato con successo!")
    
def file_presenze_bbcode():
    app = ''
    filename = "presenze"+datafile+"-bbcode.txt"
    for p in elencof:
        app += "[player]"+str(p)+"[/player], "
    with open(filename,'w') as f:
        f.write(app)
    print("\nFile "+filename+" generato con successo!")
    
def presenze():
    data()
    conta_presenze()
    stampa_presenze()

    print("\n")
    s = input("Inserisci 1 se vuoi salvare presenze"+datafile+".txt altrimenti inserisci 0: ")
    if s == 1:
        esporta_presenze_file()
    s = 0
    s = input("Inserisci 1 se vuoi salvare presenze"+datafile+"-bbcode.txt altrimenti inserisci 0: ")
    if s == 1:
        file_presenze_bbcode()


presenze()
