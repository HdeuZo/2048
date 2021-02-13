import tkinter
from random import *


class Jeu(tkinter.Tk):
    cases = [0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0]
    score = 0

    mouv = False

    # Dictionnaire des couleurs des cases. Trouvé sur internet
    bg_color = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                1024: "#edc53f", 2048: "#edc22e"}

    # Dictionnaire des couleurs de la police d'écriture. Inchangé sur le programme
    police_color = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2",
                    16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2",
                    128: "#f9f6f2", 256: "#f9f6f2", 512: "#f9f6f2",
                    1024: "#f9f6f2", 2048: "#f9f6f2"}

    def __init__(self):

        tkinter.Tk.__init__(self)

        # Forme de l'affichage puis retouche personnel
        tkinter.Tk.geometry(self, "500x395")

        # Lore/Finalisation
        tkinter.Tk.title(self, "2048")
        tkinter.Tk.iconbitmap(self, "2048.ico")

        # Ecriture de chaque Label sur le côté droit du jeu
        self.label = tkinter.Label(self, text="SCORE:", font=("Helvetica", 28))
        self.label_score = tkinter.Label(self, text=self.score, font=("Helvetica", 26))
        self.restart = tkinter.Button(self, height=1, width=12, text="recommencer", font=("Helvetica", 14),
                                      command=self.start)

        # Création de chaque case puis leur mise en place
        self.button = [
            tkinter.Button(self, height=2, width=4, state=tkinter.DISABLED, bg="#9e948a", font=("Helvetica", 24)) for i
            in range(16)]
        for i in range(16):
            self.button[i].grid(row=i // 4, column=i % 4)

        # mise en place du score et du bouton 'recommencer'
        self.label.grid(row=0, column=4)
        self.label_score.grid(row=1, column=4)
        self.restart.grid(row=2, column=4)

        # reconnaissance de chaque touche
        self.bind('<Up>', self.Mouv)
        self.bind('<Down>', self.Mouv)
        self.bind('<Left>', self.Mouv)
        self.bind('<Right>', self.Mouv)

        # Début de la partie
        self.start()
        self.mainloop()

    def new(self):
        """Cette fonction place un nouveau '2' dans un emplacement aléatoire."""

        nvl_cases = randint(0, 15)
        while self.cases[nvl_cases] != 0:
            nvl_cases = randint(0, 15)

        self.cases[nvl_cases] = 2
        self.button[nvl_cases].config(text='2', bg=self.bg_color[2])
        # print(self.cases)

    def start(self):
        """cette fonction start permet de réinitialiser le quadrillage et de placer deux '2' aléatoirement."""

        # reset
        for i in range(16):
            self.cases[i] = 0
            self.button[i].config(text=' ', bg="#9e948a")

        self.score = 0
        self.label_score.config(text='0')

        # case n°1
        st = randint(0, 15)
        self.cases[st] = 2
        self.button[st].config(text='2', bg=self.bg_color[2])

        # case n°2
        st_b = randint(0, 15)
        while st_b == st:
            st_b = randint(0, 15)
        self.cases[st_b] = 2
        self.button[st_b].config(text='2', bg=self.bg_color[2])

        # print(self.cases)

    def Mouv(self, event):

        """ La fonction permet de reconnaître quel touche est utilisée puis d'éffecter son mouvement apropriée, de
        reconnaître si la partie est gagnée ou perdu, puis de placer un '2' aléatoirement (seulement si un mouvement
        s'est produit ou bien deux chiffres se sont additionnés). """

        if event.keysym == 'Up':
            self.up()
            self.affich()
            if self.mouv:
                self.new()
                self.mouv = False
            self.win()
            self.lose()
        elif event.keysym == 'Down':
            self.down()
            self.affich()
            if self.mouv:
                self.new()
                self.mouv = False
            self.win()
            self.lose()
        elif event.keysym == 'Left':
            self.left()
            self.affich()
            if self.mouv:
                self.new()
                self.mouv = False
            self.win()
            self.lose()
        elif event.keysym == 'Right':
            self.right()
            self.affich()
            if self.mouv:
                self.new()
                self.mouv = False
            self.win()
            self.lose()

    def win(self):
        """La fonction affiche "YOU WIN!" au milieu de l'écrans lorsqu'un 2048 est présent sur le quadrillage."""

        for i in range(16):
            if self.cases[i] == 2048:
                self.cases[5] = 0
                self.button[5].config(text="YOU", bg="white")
                self.cases[6] = 0
                self.button[6].config(text="WIN!", bg="white")

    def lose(self):
        """ NON FONCTIONNEL
        score_perdu = 0
        for i in range(15):
            if i == 5 or i == 6 or i == 9 or i == 10:
                if self.cases[i + 1] != self.cases[i]:
                    score_perdu += 1
                if self.cases[i - 1] != self.cases[i]:
                    score_perdu += 1
                if self.cases[i + 4] != self.cases[i]:
                    score_perdu += 1
                if self.cases[i - 4] != self.cases[i]:
                    score_perdu += 1
            if i == 0:
                if self.cases[i + 1] != self.cases[i]:
                    score_perdu += 1
                if self.cases[i + 4] != self.cases[i]:
                    score_perdu += 1
            if i == 3:
                if self.cases[i - 1] != self.cases[i]:
                    score_perdu += 1
                if self.cases[i + 4] != self.cases[i]:
                    score_perdu += 1
            if i == 12:
                if self.cases[i - 4] != self.cases[i]:
                    score_perdu += 1
                if self.cases[i + 1] != self.cases[i]:
                    score_perdu += 1
            if i == 15:
                if self.cases[i - 1] != self.cases[i]:
                    score_perdu += 1
                if self.cases[i - 4] != self.cases[i]:
                    score_perdu += 1
        if score_perdu == 24:
            self.cases[5] = 0
            self.button[5].config(text="YOU", bg="white")
            self.cases[6] = 0
            self.button[6].config(text="LOSE!", bg="white")"""

    def up(self):
        """Fonction de mouvement vers le haut."""

        for i in range(4):
            for null in range(1, 4):
                a = 4 + i
                colonne = 0 + i
                ligne = 0
                for j in range(3):
                    if self.cases[colonne + ligne] == 0 and self.cases[a] > 0:
                        self.cases[colonne + ligne] = self.cases[a]
                        self.cases[a] = 0
                        self.mouv = True
                    if a < 12 + i:
                        a += 4
                    if ligne < 11:
                        ligne += 4
            base = 0 + i
            c = 4 + i
            for x in range(3):
                if self.cases[base] > 0:
                    if self.cases[base] == self.cases[c]:
                        self.cases[base] += self.cases[c]
                        self.cases[c] = 0
                        self.mouv = True
                        self.score += self.cases[base]
                        self.label_score.config(text=self.score)
                        # print(self.score)
                base += 4
                c += 4
            a = 4 + i
            colonne = 0 + i
            ligne = 0
            for j in range(3):
                if self.cases[colonne + ligne] == 0 and self.cases[a] > 0:
                    self.cases[colonne + ligne] = self.cases[a]
                    self.cases[a] = 0
                if a < 12 + i:
                    a += 4
                if ligne < 11:
                    ligne += 4

    def down(self):
        """Fonction de mouvement vers le bas."""

        for i in range(4):
            for null in range(1, 4):
                a = 11 - i
                ligne = 15 - i
                for j in range(3):
                    if self.cases[ligne] == 0 and self.cases[a] > 0:
                        self.cases[ligne] = self.cases[a]
                        self.cases[a] = 0
                        self.mouv = True
                    if a > 3 - i:
                        a -= 4
                    if ligne > 7 - i:
                        ligne -= 4
            c = 15 - i
            h = 11 - i
            for x in range(3):
                if self.cases[c] > 0:
                    if self.cases[h] == self.cases[c]:
                        self.cases[c] += self.cases[c]
                        self.cases[h] = 0
                        self.mouv = True
                        self.score += self.cases[c]
                        self.label_score.config(text=self.score)
                        # print(self.score)
                if h > 3 - i:
                    h -= 4
                if c > 7 - i:
                    c -= 4
                a = 11 - i
                ligne = 15 - i
                for j in range(3):
                    if self.cases[ligne] == 0 and self.cases[a] > 0:
                        self.cases[ligne] = self.cases[a]
                        self.cases[a] = 0
                    if a > 3 - i:
                        a -= 4
                    if ligne > 7 - i:
                        ligne -= 4

    def left(self):
        """Fonction de mouvement vers la gauche"""

        a = 1
        b = 0
        c = 0
        for i in range(4):
            for null in range(1, 4):
                for j in range(3):
                    if self.cases[j + b] == 0 and self.cases[j + a] > 0:
                        self.cases[j + b] = self.cases[j + a]
                        self.cases[j + a] = 0
                        self.mouv = True
            for x in range(1, 4):
                if self.cases[c] > 0:
                    if self.cases[c] == self.cases[c + 1]:
                        self.cases[c] += self.cases[c + 1]
                        self.cases[c + 1] = 0
                        self.mouv = True
                        self.score += self.cases[c]
                        self.label_score.config(text=self.score)
                        # print(self.score)
                c += 1
            if c < 14:
                c += 1
            for j in range(3):
                if self.cases[j + b] == 0 and self.cases[j + a] > 0:
                    self.cases[j + b] = self.cases[j + a]
                    self.cases[j + a] = 0
            a += 4
            b += 4

    def right(self):
        """Fonction de mouvement vers la droite."""

        for i in range(4):
            for null in range(1, 4):
                a = 2 + 4 * i
                ligne = 3 + 4 * i
                for j in range(3):
                    if self.cases[ligne] == 0 and self.cases[a] > 0:
                        self.cases[ligne] = self.cases[a]
                        self.cases[a] = 0
                        self.mouv = True
                    if a > 0 + 4 * i:
                        a -= 1
                    if ligne > 1 + 4 * i:
                        ligne -= 1
            h = 3 + 4 * i
            c = 2 + 4 * i
            for x in range(3):
                if self.cases[h] > 0:
                    if self.cases[h] == self.cases[c]:
                        self.cases[h] += self.cases[c]
                        self.cases[c] = 0
                        self.mouv = True
                        self.score += self.cases[h]
                        self.label_score.config(text=self.score)
                        # print(self.score)
                if c > 0 + 4 * i:
                    c -= 1
                if h > 1 + 4 * i:
                    h -= 1
                a = 2 + 4 * i
                ligne = 3 + 4 * i
                for j in range(3):
                    if self.cases[ligne] == 0 and self.cases[a] > 0:
                        self.cases[ligne] = self.cases[a]
                        self.cases[a] = 0
                    if a > 0 + 4 * i:
                        a -= 1
                    if ligne > 1 + 4 * i:
                        ligne -= 1

    def affich(self):

        for i in range(16):
            if self.cases[i] > 0:
                self.button[i].config(text=self.cases[i], bg=self.bg_color[self.cases[i]])
            if self.cases[i] == 0:
                self.button[i].config(text=' ', bg="#9e948a")


Jeu()
