# Créé par Waîl Yeager, le 04/07/2023 en Python 3.7
t = ([], [], [],
     [], [], [],
     [], [], [])

"""
def verify():
    if t[0] == t[1] == t[2] == ['O']:
        print("Victoire de O")
        return True
"""

def verify_o():
    if (t[0] == t[1] == t[2] == ['O']) or \
       (t[3] == t[4] == t[5] == ['O']) or \
       (t[6] == t[7] == t[8] == ['O']) or \
       (t[0] == t[3] == t[6] == ['O']) or \
       (t[1] == t[4] == t[7] == ['O']) or \
       (t[2] == t[5] == t[8] == ['O']) or \
       (t[0] == t[4] == t[8] == ['O']) or \
       (t[2] == t[4] == t[6] == ['O']):
        print("Victoire de O")
        return True

def verify_x():
    if (t[0] == t[1] == t[2] == ['X']) or \
       (t[3] == t[4] == t[5] == ['X']) or \
       (t[6] == t[7] == t[8] == ['X']) or \
       (t[0] == t[3] == t[6] == ['X']) or \
       (t[1] == t[4] == t[7] == ['X']) or \
       (t[2] == t[5] == t[8] == ['X']) or \
       (t[0] == t[4] == t[8] == ['X']) or \
       (t[2] == t[4] == t[6] == ['X']):
        print("Victoire de X")
        return True



while True:        #pour rejouer


        b = int(input("Entrez le nombre de la case à modifier avec O : "))

        if not t[b-1]:
            t[b - 1].append('O')
        else:
            print("Vous ne pouvez pas entrer de signe dans une case déjà remplie")

        print("Tableau modifié :")
        for i in range(0, len(t), 3):
            print("------",t[i], t[i + 1], t[i + 2],"------")

        if verify_o():
            break


        b = int(input("Entrez le nombre de la case à modifier avec X : "))

        if not t[b-1]:
            t[b - 1].append('X')

        else:
            print("Vous ne pouvez pas entrer de signe dans une case déjà remplie")

        print("Tableau modifié :")
        for i in range(0, len(t), 3):
            print("------",t[i],t[i + 1],t[i + 2],"------")

        if verify_x():
            break


