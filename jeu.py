#importe input qui prend les entrés des joueur

#deffinir la fonction StartGame
#initialisation d'un tableau dans un tableau de 3 colone et 3 ligne (BaseMorpion = ([0,1,2],[0,1,2],[0,1,2]))
ligneUn =["1","","",""]
ligneDeux =["2","","",""]
ligneTrois =["3","","",""]
coordonne = ['',"A","B","C"]
Jun = 0
Jdeux = 0

colonne = [coordonne,ligneUn,ligneDeux,ligneTrois]
u = colonne[0]
aa = colonne[1]
bbb = colonne[2]
cccc = colonne[3]

print(u);print(aa);print(bbb);print(cccc)

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
    Jun = Jdeux + 1
    coupJoueur()
    Jdeux = Jun + 1
    print(u);print(aa);print(bbb);print(cccc)
    coupJoueur()
    print(u);print(aa);print(bbb);print(cccc)

            
StarterGame()

