# Naam: Sophie Hospel
# Datum: 29-10
# Versie: 3

def main():   
    try:
        bestand = open("FASTA.fna-1") 
        headers, seqs = lees_inhoud(bestand)
         
        #vraagt om woord
        zoekwoord = input("Geef een zoekwoord op: ")
        for sequentie in seqs:
            if zoekwoord in sequentie:
                if zoekwoord != "":
                    #print("Sequentie:",sequentie)
                    positie = sequentie.find(zoekwoord)
                    #print("Positie",positie)
        for sequentie in headers:
            if zoekwoord in sequentie:
                if zoekwoord != 0:
                   # print(sequentie.find(zoekwoord))
                    print("Header:",sequentie)

           # for sequentie in seqs:
             #  print(is_dna(sequentie))
        knipt(seqs)
        #print(seqs)

    except TypeError as err:
        print("Error 1:", str(err))
    
        
def lees_inhoud(bestand):
    try:
        print(80*"-") 
        #bestand = open("FASTA.fna-1")
        headers = []
        seqs = []
        seq = ""
    
        for line in bestand:
            seq += line
        
        #regels voorafgaande >
        sequentie = seq.split(">")
        #print(sequentie)
        sequentie.pop(0)
        #print(sequentie[0])

        for index in range(len(sequentie)):
            header, seq = sequentie[index].split("\n", 1)
            seq = seq.replace("\n", "")
            #print(header)
            #print(seq)
            headers.append(header)
            seqs.append(seq)
    except Exception:
        print("Error 2")
    finally:
        return headers, seqs

  
def is_dna(seq):
    try:
        print(80*"-") 
        #alle nucleotiden voorkomen in sequentie
        nA = "A"
        nT = "T"
        nG = "G"
        nC = "C"
    
        if nA in seq and nT in seq and nG in seq and nC in seq:
            print("DNA sequentie")
            return True
        else:
            print("mRNA sequentie")
            return False
       # return seq
    except Exception as err:
        print("Error 3", str(err))
        
def knipt(seqs):
    try:
        print(80*"-")
        #open restrictie enzymen
        bestand = open("enzymen.txt", "r")
        lines = bestand.readlines()
        lijst = []
    
        for line in lines:
            line = line.rstrip().replace("^", "")
            naam = line.split(" ")[0]
            enzym = line.split(" ")[1]
            samen = [naam, enzym]
            lijst.append(samen)

        bestand.close()

        #controleren knippen
        #relevante output
        for x in range(len(seqs)):
            for i in range(len(lijst)):
               # print(lijst[i][1])
                positie = seqs[x].find(lijst[i][1])

                if positie >= 0:
                    print("Match met:",lijst[i][0]," op positie", positie)
           
    except Exception as err:
        print("Error 4", str(err))
main()
