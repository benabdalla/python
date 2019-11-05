#saiser e nomber   de  matier
print("en commance  a ********************************** 1er Qusetion *************************************************")
def saisie():
    nbmat1 = int(input("donnee la nomber de  matier"))
    while nbmat1 < 0:
        nbmat1 = int(input("donnee la nomber de  matier"))
    return nbmat1

#remplier  de tableau  de   note  de un eleve
nbmat=saisie()
def remplierListNote(nbmat):


    listNoteEleve = []
    for i in range(0, nbmat):
        note = float(input("donnee le note de  matier"))
        while note < 0:
            note = float(input("donnee le note de  matier"))
        listNoteEleve.append(note)
    return listNoteEleve



 #afficher le  note  d'un  eleve
listnote = remplierListNote(nbmat)
print(listnote)
#clculer  le  moyenne d'un  eleve

def moyenne(listenote,nbmat):
    moy=sum(listnote)/nbmat
    return round(moy,2)


print("la moyenne d'un  eleve est ",moyenne(listnote,nbmat))

print("en commance  ********************************************* a 2eme Qusetion **************************************")

#saiser e nomber   de  classe
def saiseClass():
    n = int(input("donnee la nomber de  classe"))
    while n < 1 or n > 4:
        n = int(input("donnee la nomber  de classe"))
    return n
#remplier  de tableau  de   note  de un classe
listNoteEleve=[]
listClasse=[]
n=saiseClass()

def remplierClasse(n):
    for i in range(0,n):
        listnote=remplierListNote(nbmat)
        moye = sum(listnote)/nbmat
        listClasse.append(moye)
    return listClasse

listClasse=remplierClasse(n)

print(listClasse)
print("en commance  ********************************************* a 3eme Qusetion **************************************")

print("moyenne Arithemtique de classe",sum(listClasse)/n)

print("en commance  ********************************************* a 4eme Qusetion **************************************")

print("la  moyenne et mimum est ",min(listClasse))

print("en commance  ********************************************* a 5eme Qusetion **************************************")


print("la  moyenne et maximum est ",max(listClasse))

print("en commance  ********************************************* a 6eme Qusetion **************************************")
def triBulle(listClasse):
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage += 1
        for k in range(0, len(listClasse) - passage):
            if listClasse[k] < listClasse[k + 1]:
                permutation = True
                aux = listClasse[k]
                listClasse[k] = listClasse[k + 1]
                listClasse[k + 1] = aux
    return listClasse

print(triBulle(listClasse))

print("en commance  ********************************************* a 7eme Qusetion **************************************")

def mointion(listClasse):
    for i in range(0, n):
        if (listClasse[i] >= 0 or listClasse[i] > 8):
            print("le moyenne et :", listClasse[i], "Faible")
        elif (listClasse[i] >= 8 or listClasse[i] >= 10):

            print("le moyenne et :", listClasse[i], "passable")

        elif (listClasse[i] > 10 or listClasse[i] >= 15):
            print("le moyenne et :", listClasse[i], "bien")
        else:
            print("le moyenne et :", listClasse[i], "excelent")












