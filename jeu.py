#importe input qui prend les entrés des joueur

#deffinir la fonction StartGame
#initialisation d'un tableau dans un tableau de 3 colone et 3 ligne (BaseMorpion = ([0,1,2],[0,1,2],[0,1,2]))
ligneUn =["1","","",""]
ligneDeux =["2","","",""]
ligneTrois =["3","","",""]
coordonne = ['',"A","B","C"]

colonne = [coordonne,ligneUn,ligneDeux,ligneTrois]
u = colonne[0]
aa = colonne[1]
bbb = colonne[2]
cccc = colonne[3]

print(u);print(aa);print(bbb);print(cccc)

def coupJoueur():
    Reponse = input("mettre les coordonné : ")
    while 1:
        if not Reponse in ["a1","a2","a3","A1","A2","A3","b1","b2","b3","B1","B2","B3","c1","c2","c3","C1","C2","C3"]:
            print("réponse inconrectte")
            Reponse = input("mettre les coordonné : ")
        else:
            print("bonne réponse")
            if Reponse == "a1" or Reponse == "A1":
                if ligneUn[1] != "x" or ligneUn[1] != "o":
                    ligneUn[1] = "x"
                elif ligneUn[1] == "x" or ligneUn[1] == "o":
                    print("yolo")
                    coupJoueur()
                else:
                    print()
            elif Reponse == "b1" or Reponse == "B1":
                ligneUn[2] = "x"
            elif Reponse == "c1" or Reponse == "C3":
                ligneUn[3] = "x"
            elif Reponse == "a2" or Reponse == "A2":
                ligneDeux[1] = "x"
            elif Reponse == "b2" or Reponse == "B2":
                ligneDeux[2] = "x"
            elif Reponse == "c2" or Reponse == "C2":
                ligneDeux[3] = "x"
            elif Reponse == "a3" or Reponse == "A3":
                ligneDeux[1] = "x"
            elif Reponse == "b3" or Reponse == "B3":
                ligneDeux[2] = "x"
            elif Reponse == "c3" or Reponse == "C3":
                ligneDeux[3] = "x"
            print(u);print(aa);print(bbb);print(cccc)
            Reponse = input("mettre les coordonné : ")
            
def StarterGame():
    coupJoueur()

            
StarterGame()

