#importe input qui prend les entrés des joueur
#deffinir la fonction StartGame
# import pygame
# pygame.init()
# from pygame.locals import *
# fenetre = pygame.display.set_mode((300, 300))
# pygame.display.set_caption("Morpion")

# interface = True
# while interface:
#     pygame.rect(255.255)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             interface = False
    

# pygame.quit()

coordonne = ['',"A","B","C"]
ligneUn =["1","","",""]
ligneDeux =["2","","",""]
ligneTrois =["3","","",""]
compteTour = 0
encore = 0

colonneUn = [ligneUn[1],ligneDeux[1],ligneTrois[1]]
colonneDeux = [ligneUn[2],ligneDeux[2],ligneTrois[2]]
colonneTrois = [ligneUn[3],ligneDeux[3],ligneTrois[3]]
diagoUn = [colonneUn[0],colonneDeux[1],colonneTrois[2]]
diagoDeux = [colonneUn[2],colonneDeux[1],colonneTrois[0]]

Jun = 0
Jdeux = 0
gagnant = 3

Tableau = [coordonne,ligneUn,ligneDeux,ligneTrois]


def Restart():
    global ligneDeux
    global ligneUn
    global ligneTrois
    global colonneDeux
    global colonneUn
    global colonneTrois
    global diagoDeux
    global diagoUn
    global gagnant
    global Jun
    global Jdeux
    global compteTour
    global encore
    global Tableau
    global fm
    print("yo bande de débile tu veux retenter ?")
    encore = input("-1 = retenter || -2 = j'abandone car jsui nul: ")
    if not encore in ['1','2']:
        print("te fous pas dma geu ptit batard mes 1 ou 2 et pas : ",encore)
        print("yo bande de débile tu veux retenter ?")
        Restart()
    elif encore in ['1','2']:
        if encore == '1':
            print("oki Dinosaure ON RESTARTTTTTTTRE")
            coordonne = ['',"A","B","C"]
            ligneUn =["1","","",""]
            ligneDeux =["2","","",""]
            ligneTrois =["3","","",""]
            compteTour = 0
            encore = 0
            fm = 0

            colonneUn = [ligneUn[1],ligneDeux[1],ligneTrois[1]]
            colonneDeux = [ligneUn[2],ligneDeux[2],ligneTrois[2]]
            colonneTrois = [ligneUn[3],ligneDeux[3],ligneTrois[3]]
            diagoUn = [colonneUn[0],colonneDeux[1],colonneTrois[2]]
            diagoDeux = [colonneUn[2],colonneDeux[1],colonneTrois[0]]

            Jun = 0
            Jdeux = 0
            gagnant = 3

            Tableau = [coordonne,ligneUn,ligneDeux,ligneTrois]

            StarterGame()

        elif encore == '2':
            print("NNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBBBBBBBBBBBBBB")
            return

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

    colonneUn = [ligneUn[1],ligneDeux[1],ligneTrois[1]]
    colonneDeux = [ligneUn[2],ligneDeux[2],ligneTrois[2]]
    colonneTrois = [ligneUn[3],ligneDeux[3],ligneTrois[3]]
    diagoUn = [colonneUn[0],colonneDeux[1],colonneTrois[2]]
    diagoDeux = [colonneUn[2],colonneDeux[1],colonneTrois[0]]

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
    global ligneDeux
    global ligneUn
    global ligneTrois
    global colonneDeux
    global colonneUn
    global colonneTrois
    global diagoDeux
    global diagoUn
    global gagnant
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
fm = 0
def Bot():
    global ligneDeux
    global ligneUn
    global ligneTrois
    global colonneDeux
    global colonneUn
    global colonneTrois
    global diagoDeux
    global diagoUn
    global gagnant
    global Tableau
    global compteTour
    global fm
    TableauRobot = [ligneUn[1],ligneUn[2],ligneUn[3],ligneDeux[1],ligneDeux[2],ligneDeux[3],ligneTrois[1],ligneTrois[2],ligneTrois[3]]
    colonneUn = [ligneUn[1],ligneDeux[1],ligneTrois[1]]
    colonneDeux = [ligneUn[2],ligneDeux[2],ligneTrois[2]]
    colonneTrois = [ligneUn[3],ligneDeux[3],ligneTrois[3]]
    diagoUn = [colonneUn[0],colonneDeux[1],colonneTrois[2]]
    diagoDeux = [colonneUn[2],colonneDeux[1],colonneTrois[0]]
    if compteTour == 1:
        if ligneUn[1] == 'x' or ligneUn[3] == 'x' or ligneTrois[1] == 'x' or ligneTrois[3] == 'x':
            ligneDeux[2] = 'o'
            fm = 1
            return
        if ligneDeux[2] == 'x':
            ligneUn[1] = 'o'
            fm = 1
            return
        if ligneUn[2] == 'x':
            ligneTrois = 'o'
            fm = 1
            return
        if ligneDeux[1] == 'x':
            ligneUn[3] = 'o'
            fm = 1
            return
        if ligneTrois[2] == 'x':
            ligneUn[1] = 'o'
            fm = 1
            return
        if ligneDeux[3] == 'x':
            ligneTrois[1] = 'o'
            fm = 1
            return
    if fm == 1:
        for i in TableauRobot:
            if i == "":
                if ligneUn.count('o') == 2:
                    for i in range(1, len(ligneUn)):
                        if ligneUn[i] == '':
                            ligneUn[i] = 'o'
                            return
                if ligneDeux.count('o') == 2:
                    for i in range(1, len(ligneDeux)):
                        if ligneDeux[i] == '':
                            ligneDeux[i] = 'o'
                            return
                if ligneTrois.count('o') == 2:
                    for i in range(1, len(ligneTrois)):
                        if ligneTrois[i] == '':
                            ligneTrois[i] = 'o'
                            return
                if colonneUn.count('o') == 2:
                    for i in range(len(colonneUn)):
                        if colonneUn[i] == '':
                            colonneUn[i] = 'o'
                            ligneUn[1] = colonneUn[0];ligneDeux[1] = colonneUn[1];ligneTrois[1] = colonneUn[2]
                            return
                if colonneDeux.count('o') == 2:
                    for i in range(len(colonneDeux)):
                        if colonneDeux[i] == '':
                            colonneDeux[i] = 'o'
                            ligneUn[2] = colonneDeux[0];ligneDeux[2] = colonneDeux[1];ligneTrois[2] = colonneDeux[2]
                            return
                if colonneTrois.count('o') == 2:
                    for i in range(len(colonneTrois)):
                        if colonneTrois[i] == '':
                            colonneTrois[i] = 'o'
                            ligneUn[3] = colonneTrois[0];ligneDeux[3] = colonneTrois[1];ligneTrois[3] = colonneTrois[2]
                            return
                if diagoUn.count('o') == 2:
                    for i in range(len(diagoUn)):
                        if diagoUn[i] == '':
                            diagoUn[i] = 'o'
                            ligneUn[1] = diagoUn[0];ligneDeux[2] = diagoUn[1];ligneTrois[3] = diagoUn[2]
                            return
                if diagoDeux.count('o') == 2:
                    for i in range(len(diagoDeux)):
                        if diagoDeux[i] == '':
                            diagoDeux[i] = 'o'
                            ligneUn[3] = diagoDeux[2];ligneDeux[2] = diagoDeux[1];ligneTrois[1] = diagoDeux[0]
                            return 
                if ligneUn.count('')>= 1:                     
                    if ligneUn.count('x') == 2:
                        for i in range(1, len(ligneUn)):
                            if ligneUn[i] == '':
                                ligneUn[i] = 'o'
                                return
                if ligneDeux.count('')>= 1:                
                    if ligneDeux.count('x') == 2:
                        for i in range(1, len(ligneDeux)):
                            if ligneDeux[i] == '':
                                ligneDeux[i] = 'o'
                                return
                if ligneTrois.count('')>= 1:
                    if ligneTrois.count('x') == 2:
                        for i in range(1, len(ligneTrois)):
                            if ligneTrois[i] == '':
                                ligneTrois[i] = 'o'
                                return
                if colonneUn.count('')>= 1:
                    if colonneUn.count('x') == 2:
                        for i in range(len(colonneUn)):
                            if colonneUn[i] == '':
                                colonneUn[i] = 'o'
                                ligneUn[1] = colonneUn[0];ligneDeux[1] = colonneUn[1];ligneTrois[1] = colonneUn[2]
                                return
                if colonneDeux.count('')>= 1:                
                    if colonneDeux.count('x') == 2:
                        for i in range(len(colonneDeux)):
                            if colonneDeux[i] == '':
                                colonneDeux[i] = 'o'
                                ligneUn[2] = colonneDeux[0];ligneDeux[2] = colonneDeux[1];ligneTrois[2] = colonneDeux[2]
                                return
                if colonneTrois.count('')>= 1:
                    if colonneTrois.count('x') == 2:
                        for i in range(len(colonneTrois)):
                            if colonneTrois[i] == '':
                                colonneTrois[i] = 'o'
                                ligneUn[3] = colonneTrois[0];ligneDeux[3] = colonneTrois[1];ligneTrois[3] = colonneTrois[2]
                                return
                if diagoUn.count('')>= 1:                
                    if diagoUn.count('x') == 2:
                        for i in range(len(diagoUn)):
                            if diagoUn[i] == '':
                                diagoUn[i] = 'o'
                                ligneUn[1] = diagoUn[0];ligneDeux[2] = diagoUn[1];ligneTrois[3] = diagoUn[2]
                                return
                if diagoDeux.count('')>= 1:
                    if diagoDeux.count('x') == 2:
                        for i in range(len(diagoDeux)):
                            if diagoDeux[i] == '':
                                diagoDeux[i] = 'o'
                                ligneUn[3] = diagoDeux[2];ligneDeux[2] = diagoDeux[1];ligneTrois[1] = diagoDeux[0]
                                return
                if ligneUn.count('o') == 1:
                    for i in range(1, len(ligneUn)):
                        if ligneUn[i] == '':
                            ligneUn[i] = 'o'
                            return
                if ligneDeux.count('o') == 1:
                    for i in range(1, len(ligneDeux)):
                        if ligneDeux[i] == '':
                            ligneDeux[i] = 'o'
                            return
                if ligneTrois.count('o') == 1:
                    for i in range(1, len(ligneTrois)):
                        if ligneTrois[i] == '':
                            ligneTrois[i] = 'o'
                            return
                if colonneUn.count('o') == 1:
                    for i in range(len(colonneUn)):
                        if colonneUn[i] == '':
                            colonneUn[i] = 'o'
                            ligneUn[1] = colonneUn[0];ligneDeux[1] = colonneUn[1];ligneTrois[1] = colonneUn[2]
                            return
                if colonneDeux.count('o') == 1:
                    for i in range(len(colonneDeux)):
                        if colonneDeux[i] == '':
                            colonneDeux[i] = 'o'
                            ligneUn[2] = colonneDeux[0];ligneDeux[2] = colonneDeux[1];ligneTrois[2] = colonneDeux[2]
                            return
                if colonneTrois.count('o') == 1:
                    for i in range(len(colonneTrois)):
                        if colonneTrois[i] == '':
                            colonneTrois[i] = 'o'
                            ligneUn[3] = colonneTrois[0];ligneDeux[3] = colonneTrois[1];ligneTrois[3] = colonneTrois[2]
                            return
                if diagoUn.count('o') == 1:
                    for i in range(len(diagoUn)):
                        if diagoUn[i] == '':
                            diagoUn[i] = 'o'
                            ligneUn[1] = diagoUn[0];ligneDeux[2] = diagoUn[1];ligneTrois[3] = diagoUn[2]
                            return
                if diagoDeux.count('o') == 1:
                    for i in range(len(diagoDeux)):
                        if diagoDeux[i] == '':
                            diagoDeux[i] = 'o'
                            ligneUn[3] = diagoDeux[0];ligneDeux[2] = diagoDeux[1];ligneTrois[1] = diagoDeux[2]
                            return              

explication = 0
def StarterGame():    
    global explication
    if explication == 0:
        print("yo sale dino, je t'explique les règle ^^, :")
        print("le morpion, le joueur 1 c'est la croix, joueur 2 le rond, celui qui arrive a alligner dans le cube de 3 sur 3, 3 X ou 3 O a gagner")
        print("voila bon bonne chance !")
        explication = 1
    global Jun
    global Jdeux
    global gagnant
    global compteTour
    global encore
    global Tableau
    gagnant = 3
    print("me revoila tu veux te taper contre qui ? le bot ou un pote ?")
    print("réponse possible : ")
    print("-bot");print("-pote")
    demande = "Restart"
    demande = input("votre choix: ")
    if not demande in["bot","pote"]:
        print("tu me mes roublise, stp mes une valeur possible pas :",demande)
        StarterGame()
    if demande in ["bot","pote"]:
        if demande == "pote":
            print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
            while not gagnant in [0,1,2]:
                if not gagnant in [0,1,2]:
                    Jun = Jdeux + 1
                    coupJoueur()
                    compteTour = compteTour + 1
                    print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
                    winner()
                if not gagnant in [0,1,2]:   
                    Jdeux = Jun + 1
                    coupJoueur()
                    compteTour = compteTour + 1
                    print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
                    winner()
            if gagnant == 0:
                print("matche nul, vous êtes nul !")     
                Restart()
            elif gagnant == 1:
                print("joueur 1 (ps celui qui a les x ) est gagnant, ps le joueur 2 tes nul")
                Restart()
            elif gagnant == 2:
                print("le joueur 2 (ps celui qui a les o ) est gagnant, ps le joueur 1 tes nul")
                Restart()
        if demande == "bot":
            print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
            while not gagnant in [0,1,2]:
                if not gagnant in [0,1,2]:
                    Jun = Jdeux + 1
                    coupJoueur()
                    compteTour = compteTour + 1
                    winner()
                if not gagnant in [0,1,2]:   
                    Jdeux = Jun + 1
                    Bot()
                    print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
                    compteTour = compteTour + 1
                    winner()
            if gagnant == 0:
                print("matche nul, vous êtes nul !")     
                Restart()
            elif gagnant == 1:
                print("joueur 1 (ps celui qui a les x ) est gagnant, ps je vais foutre mon bot a la casse")
                Restart()
            elif gagnant == 2:
                print("le bot (ps celui qui a les o ) est gagnant, ps le joueur 1 tes nul")
                Restart()


# Bot()            
StarterGame()