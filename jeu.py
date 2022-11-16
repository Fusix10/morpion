#importe input qui prend les entrés des joueur

#deffinir la fonction StartGame
#initialisation d'un tableau dans un tableau de 3 colone et 3 ligne (BaseMorpion = ([0,1,2],[0,1,2],[0,1,2]))
coordonne = ['',"A","B","C"]
ligneUn =["1","","",""]
ligneDeux =["2","","",""]
ligneTrois =["3","","",""]
compteTour = 0

colonneUn = [ligneUn[1],ligneDeux[1],ligneTrois[1]]
colonneDeux = [ligneUn[2],ligneDeux[2],ligneTrois[2]]
colonneTrois = [ligneUn[3],ligneDeux[3],ligneTrois[3]]
diagoUn = [ligneUn[1],ligneDeux[2],ligneTrois[3]]
diagoDeux = [ligneUn[3],ligneDeux[2],ligneTrois[1]]

Jun = 0
Jdeux = 0
gagnant = 10

Tableau = [coordonne,ligneUn,ligneDeux,ligneTrois]
u = Tableau[0]
aa = Tableau[1]
bbb = Tableau[2]
cccc = Tableau[3]

print(u);print(aa);print(bbb);print(cccc)

def winner():
    global ligneDeux
    global ligneUn
    global ligneTrois
    global colonneDeux
    global colonneUn
    global colonneTrois
    global diagoDeux
    global diagoUn
    global gagnant
    if ligneUn[1] == "x" and ligneUn[2] == "x" and ligneUn[3] == "x":
        gagnant = 1
    elif ligneDeux[1] == "x" and ligneDeux[2] == "x" and ligneDeux[3] == "x":
        gagnant = 1
    elif ligneTrois[1] == "x" and ligneTrois[2] == "x" and ligneTrois[3] == "x":
        gagnant = 1
    elif colonneUn[0] == "x" and colonneUn[1] == "x" and colonneUn[2] == "x":
        gagnant = 1
    elif colonneDeux[0] == "x" and colonneDeux[1] == "x" and colonneDeux[2] == "x":
        gagnant = 1
    elif colonneTrois[0] == "x" and colonneTrois[1] == "x" and colonneTrois[2] == "x":
        gagnant = 1
    elif diagoUn[0] == "x" and diagoUn[1] == "x" and diagoUn[2] == "x":
        gagnant = 1
    elif diagoDeux[0] == "x" and diagoDeux[1] == "x" and diagoDeux[2] == "x":
        gagnant = 1
    elif ligneUn[1] == "o" and ligneUn[2] == "o" and ligneUn[3] == "o":
        gagnant = 2
    elif ligneDeux[1] == "o" and ligneDeux[2] == "o" and ligneDeux[3] == "o":
        gagnant = 2
    elif ligneTrois[1] == "o" and ligneTrois[2] == "o" and ligneTrois[3] == "o":
        gagnant = 2
    elif colonneUn[0] == "o" and colonneUn[1] == "o" and colonneUn[2] == "o":
        gagnant = 2
    elif colonneDeux[0] == "o" and colonneDeux[1] == "o" and colonneDeux[2] == "o":
        gagnant = 2
    elif colonneTrois[0] == "o" and colonneTrois[1] == "o" and colonneTrois[2] == "o":
        gagnant = 2
    elif diagoUn[0] == "o" and diagoUn[1] == "o" and diagoUn[2] == "o":
        gagnant = 2
    elif diagoDeux[0] == "o" and diagoDeux[1] == "o" and diagoDeux[2] == "o":
        gagnant = 2
    elif compteTour == 9:
        gagnant = 0




def coupJoueur():
    Reponse = input("mettre les coordonné : ")
    if not Reponse in ["a1","a2","a3","A1","A2","A3","b1","b2","b3","B1","B2","B3","c1","c2","c3","C1","C2","C3"]:
        print("réponse inconrectte")
        coupJoueur()
    else:
        print("bonne réponse")
        if Reponse == "a1" or Reponse == "A1":
            if ligneUn[1] != "":
                print("yolo")
                coupJoueur()
            elif ligneUn[1] == "":
                if Jun > Jdeux :
                    ligneUn[1] ="x"
                elif Jdeux > Jun :
                    ligneUn[1] ="o"
            else:
                print("erreur")
        elif Reponse == "b1" or Reponse == "B1":
            if ligneUn[2] != "":
                print("yolo")
                coupJoueur()
            elif ligneUn[2] == "":
                if Jun > Jdeux :
                    ligneUn[2] ="x"
                elif Jdeux > Jun :
                    ligneUn[2] ="o"
            else:
                print("erreur")
        elif Reponse == "c1" or Reponse == "C3":
            if ligneUn[3] != "":
                print("yolo")
                coupJoueur()
            elif ligneUn[3] == "":
                if Jun > Jdeux :
                    ligneUn[3] ="x"
                elif Jdeux > Jun :
                    ligneUn[3] ="o"
            else:
                print("erreur")
        elif Reponse == "a2" or Reponse == "A2":
            if ligneDeux[1] != "":
                print("yolo")
                coupJoueur()
            elif ligneDeux[1] == "":
                if Jun > Jdeux :
                    ligneDeux[1] ="x"
                elif Jdeux > Jun :
                    ligneDeux[1] ="o"
            else:
                print("erreur")
        elif Reponse == "b2" or Reponse == "B2":
            if ligneDeux[2] != "":
                print("yolo")
                coupJoueur()
            elif ligneDeux[2] == "":
                if Jun > Jdeux :
                    ligneDeux[2] ="x"
                elif Jdeux > Jun :
                    ligneDeux[2] ="o"
            else:
                print("erreur")
        elif Reponse == "c2" or Reponse == "C2":
            if ligneDeux[3] != "":
                print("yolo")
                coupJoueur()
            elif ligneDeux[3] == "":
                if Jun > Jdeux :
                    ligneDeux[3] ="x"
                elif Jdeux > Jun :
                    ligneDeux[3] ="o"
            else:
                print("erreur")
        elif Reponse == "a3" or Reponse == "A3":
            if ligneTrois[1] != "":
                print("yolo")
                coupJoueur()
            elif ligneTrois[1] == "":
                if Jun > Jdeux :
                    ligneTrois[1] ="x"
                elif Jdeux > Jun :
                    ligneTrois[1] ="o"
            else:
                print("erreur")
        elif Reponse == "b3" or Reponse == "B3":
            if ligneTrois[2] != "":
                print("yolo")
                coupJoueur()
            elif ligneTrois[2] == "":
                if Jun > Jdeux :
                    ligneTrois[2] ="x"
                elif Jdeux > Jun :
                    ligneTrois[2] ="o"
            else:
                print("erreur")
        elif Reponse == "c3" or Reponse == "C3":
            if ligneTrois[3] != "":
                print("yolo")
                coupJoueur()
            elif ligneTrois[3] == "":
                if Jun > Jdeux :
                    ligneTrois[3] ="x"
                elif Jdeux > Jun :
                    ligneTrois[3] ="o"
            else:
                print("erreur")
            
def StarterGame():
    global Jun
    global Jdeux
    global gagnant
    global compteTour
    while not gagnant in [0,1,2]:
        Jun = Jdeux + 1
        coupJoueur()
        compteTour = compteTour + 1
        Jdeux = Jun + 1
        print(u);print(aa);print(bbb);print(cccc)
        winner()
        print(compteTour)
        print(gagnant)
        coupJoueur()
        compteTour = compteTour + 1
        print(u);print(aa);print(bbb);print(cccc)
        winner()
        print(compteTour)
        print(gagnant)


            
StarterGame()

