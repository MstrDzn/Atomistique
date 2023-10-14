import matplotlib.pyplot as plt
al="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ :"
elements=['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg',
'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr',
'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',
'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La',
'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er',
'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au',
'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md',
'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn',
'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
class Atomistique:
    def __init__(self,X,action):
        '''
        __init__ défini les variables importantes pour les fonctions de la classe Atomistique
        et permet aussi d'afficher la valeur souhaité dans "action"

        elle prend en paramètres X et action avec:

            - X l'entité chimique (numéro atomique ou bien chaine de caractère pouvant
             être complémentée avec un nombre d'ions (écrit sous forme: "y+ ou y-"
             ou encore "++++ ou ------"))
            - action qui est le paramètre souhaitée, c'est-à-dire:
                * soit casesQuantiques
                * soit structureComplete
                * soit structureAllegee
                * soit structureValence

        '''
        self.elements=elements
        self.exceptions = ['Cr', 'Cu', 'Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'Ag', 'Pt', 'Au',
                      'La', 'Ce', 'Gd', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Cm']
        self.ordre='1s2s2p3s3p4s3d4p5s4d5p6s4f5d6p7s5f6d7p'
        self.nb_electrons,self.nom=self.nb_electrons(X)
        if type(X)==str:
            self.nomion=X
        else:
            self.nomion=self.nom

        for i in range (len(self.nb_electrons)):
            if self.nb_electrons[i] not in al:
                self.nb_electrons_r=int(self.nb_electrons[i-1:])
                break
        self.structureComplete,self.structureComplete_r = self.structureComplete()

        assert 118 >= self.nb_electrons_r > 0
        self.structureAllegee = self.structureAllegee()
        self.structureValence=self.structureValence()

        if action=="casesQuantiques":
            self.casesQuantiques()
        if action=="structureComplete":
            print(self.structureComplete)
        if action=="structureAllegee":
            print(self.structureAllegee)
        if action =="structureValence":
            print(self.structureValence)

    def nb_electrons(self,X):
        '''
        nb_electrons prend en paramètre X (précisé dans le docstring de __init__)

        elle retourne deux variables:
            - self.nb_electrons, qui est une chaîne de caractère donnant le nombre d'éléctrons de
            l'élément chimique
            - self.nom, une variable seulement utlie pour les autres fonctions contenant
            seulement le nom de l'atome, n'étant pas dévoilée à l'utilisateur.
        '''
        nb_electrons = 0
        if type(X) == str:
            if len(X) >= 2:
                if X[1] in al:
                    if len(X) >= 3:
                        self.nom=X[:2]
                        if X[2] == "+" or X[2] == "-":
                            nb_electrons = self.elements.index(X[:2]) + 1
                            if len(X) >= 3:
                                for i in range(2, len(X)):
                                    if X[i] == "+":
                                        nb_electrons -= 1
                                    if X[i] == "-":
                                        nb_electrons += 1
                                return X[0:2] + ": " + str(nb_electrons), self.nom
                        else:
                            nb_electrons = self.elements.index(X[:2]) + 1
                            self.nom=X[:2]
                            if X[3] == "+" or X[3] == "-":
                                if X[3] == "+":
                                    nb_electrons -= int(X[2])
                                if X[3] == "-":
                                    nb_electrons += int(X[2])

                            else:
                                if X[4] == "+" or X[4] == "-":
                                    if X[4] == "+":
                                        nb_electrons -= int(X[2:4])
                                    if X[4] == "-":
                                        nb_electrons += int(X[2:4])

                                else:
                                    if X[5] == "+" or X[5] == "-":
                                        if X[5] == "+":
                                            nb_electrons -= int(X[2:5])
                                        if X[5] == "-":
                                            nb_electrons += int(X[2:5])

                            return X[0:2] + ": " + str(nb_electrons), self.nom


                    else:
                        nb_electrons = self.elements.index(X) + 1
                        self.nom = X
                        return str(X) + ": " + str(nb_electrons), self.nom

                else:
                    nb_electrons = self.elements.index(X[:1]) + 1
                    self.nom = X[0]
                    if X[1] == "+" or X[1] == "-":
                        for i in range(1, len(X)):
                            if X[i] == "+":
                                nb_electrons -= 1
                            if X[i] == "-":
                                nb_electrons += 1
                        return X[0:1] + ": " + str(nb_electrons), self.nom
                    else:
                        nb_electrons = self.elements.index(X[0]) + 1
                        self.nom = X[0]
                        if X[2] == "+" or X[2] == "-":
                            if X[2] == "+":
                                nb_electrons -= int(X[1])
                            if X[2] == "-":
                                nb_electrons += int(X[1])

                        else:
                            if X[3] == "+" or X[3] == "-":
                                if X[3] == "+":
                                    nb_electrons -= int(X[1:3])
                                if X[3] == "-":
                                    nb_electrons += int(X[1:3])

                            else:
                                if X[4] == "+" or X[4] == "-":
                                    if X[4] == "+":
                                        nb_electrons -= int(X[1:4])
                                    if X[4] == "-":
                                        nb_electrons += int(X[1:4])

                        return X[0] + ": " + str(nb_electrons),self.nom
            else:
                nb_electrons = self.elements.index(X) + 1
                self.nom=X
                return str(X) + ": " + str(nb_electrons),self.nom
        else:
            nb_electrons = X
            self.nom=self.elements[X-1]
            return str(self.elements[X - 1]) + ": " + str(X),self.nom

    def structureComplete(self):
        '''
        structureComplete ne prend rien en paramètre exceptés les variables de la classe

        elle renvoie deux variables:
            - self.structureComplete qui est une chaine de caractères indiquant la structure
            éléctronique de l'élément chimique avec une mise en forme et le nom de l'élément
            - self.structureComplete_r qui est aussi une chaine de caractères mais contenant
            uniquement la structure éléctronique de l'élément chimique
        '''
        a=""
        b=self.nb_electrons_r
        for i in range (0,len(self.ordre),2):
            if b>0:
                if self.ordre[i+1]=="s":
                    if b<2:
                        a=a+self.ordre[i]+self.ordre[i+1]+str(b)+" "
                        b-=b
                    else:
                        a = a + self.ordre[i] + self.ordre[i + 1] + "2" + " "
                        b-=2
                if self.ordre[i + 1] == "p":
                    if b < 6:
                        a = a + self.ordre[i] + self.ordre[i + 1] + str(b) + " "
                        b -= b
                    else:
                        a = a + self.ordre[i] + self.ordre[i + 1] + "6" + " "
                        b -= 6
                if self.ordre[i + 1] == "d":
                    if b < 10:
                        a = a + self.ordre[i] + self.ordre[i + 1] + str(b) + " "
                        b -= b
                    else:
                        a = a + self.ordre[i] + self.ordre[i + 1] + "10" + " "
                        b -= 10
                if self.ordre[i + 1] == "f":
                    if b < 14:
                        a = a + self.ordre[i] + self.ordre[i + 1] + str(b) + " "
                        b -= b
                    else:
                        a = a + self.ordre[i] + self.ordre[i + 1] + "14" + " "
                        b -= 14
        if self.nom in self.exceptions:
            return self.nomion+"*" + ": " + a,a
        else:
            return self.nomion+": "+a,a

    def structureAllegee(self):
        '''
        structureAllegee ne prend rien en paramètre exceptés les variables de la classe

        elle renvoie une variable:
            - self.structureAllegee qui est une chaine de caractères comportant la
            structure éléctronique allégée à l'aide des gaz nobles
        '''
        z=self.structureComplete_r
        if self.nb_electrons_r==118:
            if self.nom in self.exceptions:
                return self.nomion + "*" + ": " + "[Og]"
            else:
                return self.nomion + ": " + "[Og]"

        elif self.nb_electrons_r>=86:  #6p6 couche finale
            for i in range (0,len(z)):
                if z[i:i+3]=="6p6":
                    y=z[i+4:]

            if self.nom in self.exceptions:
                return self.nomion + "*" + ": " + "[Rn] "+y
            else:
                return self.nomion + ": " + "[Rn] "+y

        elif self.nb_electrons_r>=54:  #5p6 cf
            for i in range (0,len(z)):
                if z[i:i+3]=="5p6":
                    y=z[i+4:]

            if self.nom in self.exceptions:
                return self.nomion + "*" + ": " + "[Xe] "+y
            else:
                return self.nomion + ": " + "[Xe] "+y
        elif self.nb_electrons_r>=36:  #4p6 cf
            for i in range (0,len(z)):
                if z[i:i+3]=="4p6":
                    y=z[i+4:]

            if self.nom in self.exceptions:
                return self.nomion + "*" + ": " + "[Kr] "+y
            else:
                return self.nomion + ": " + "[Kr] "+y
        elif self.nb_electrons_r>=18:  #3p6 cf
            for i in range (0,len(z)):
                if z[i:i+3]=="3p6":
                    y=z[i+4:]

            if self.nom in self.exceptions:
                return self.nomion + "*" + ": " + "[Ar] "+y
            else:
                return self.nomion + ": " + "[Ar] "+y
        elif self.nb_electrons_r>=10:  #2p6 cf
            for i in range (0,len(z)):
                if z[i:i+3]=="2p6":
                    y=z[i+4:]

            if self.nom in self.exceptions:
                return self.nomion + "*" + ": " + "[Ne] "+y
            else:
                return self.nomion + ": " + "[Ne] "+y
        elif self.nb_electrons_r>=2:  #1s2 cf
            for i in range (0,len(z)):
                if z[i:i+3]=="1s2":
                    y=z[i+4:]

            if self.nom in self.exceptions:
                return self.nomion + "*" + ": " + "[He] "+y
            else:
                return self.nomion + ": " + "[He] "+y

    def structureValence(self):
        '''
        structureValence ne prend rien en paramètre exceptés les variables de la classe

        elle renvoie une variable:
            - self.structureValence qui est une chaine de caractère contenant les éléctrons
            de Valence seulement, accompagnée d'une mise en forme avec une phrase
        '''
        a=""
        l=[]
        for i in range (len(self.structureComplete_r)):
            if self.structureComplete_r[i] not in al and self.structureComplete_r[i-1]==" " and i not in l:
                l.append(self.structureComplete_r[i])
        b=max(l)
        for i in range (len(self.structureComplete_r)):
            if self.structureComplete_r[i] not in al and self.structureComplete_r[i]==b and self.structureComplete_r[i-1]==" ":
                if self.structureComplete_r[i+3] in al:
                    a+=self.structureComplete_r[i:i+3]+" "
                else:
                    a+=self.structureComplete_r[i:i+4]+" "
        if self.structureComplete_r[-2] not in al:
            if self.structureComplete_r[-3] not in al:
                if self.structureComplete_r[-5:] not in a:
                    if self.structureComplete_r[-4]=="f":
                        if self.structureComplete_r[-3:]!="14":
                            a+=self.structureComplete_r[-5:]
            else:
                if self.structureComplete_r[-4:] not in a:
                    if self.structureComplete_r[-3]=="s":
                        if self.structureComplete_r[-2]!="2":
                            a+=self.structureComplete_r[-4:]
                    elif self.structureComplete_r[-3]=="p":
                        if self.structureComplete_r[-2]!="6":

                            a+=self.structureComplete_r[-4:]
                    if self.structureComplete_r[-3]=="d" or self.structureComplete_r[-3]=="f":
                        a+=self.structureComplete_r[-4:]



        return "Electrons de Valence de "+ self.nomion+' : '+a

    def casesQuantiques(self):
        '''
        casesQuantiques ne prend rien en paramètre exceptés les variables de la classe

        Elle ne renvoie pas de valeurs, elle effectue le tracé des cases quantiques à l'aide du module
        matplotlib.pyplot qui affichera:
            * La totalité des cases quantiques rangées en fonction de leur nombre quantique ainsi que dans l'ordre
            des sous-couches "s,p,d,f"
            * Au dessus des cases, la structure Allégée de l'élément chimimque
            * En bas à droite du tracé se trouve la structure complète de l'élément chimique
            (* une légende avec les éléctrons de Valence)
        '''
        cordtext=[]
        st=self.structureComplete_r
        plt.close()
        plt.figure(figsize=(22,13))
        plt.axis("off")
        b=12
        for i in range (1,8):
            plt.text(1,b-0.55,"n = "+str(i),color="black",fontsize=18,verticalalignment='center',horizontalalignment='center',)
            cordtext.append(b)
            b-=1.71
        plt.text(11.4, cordtext[-1], "Structure complète:", color="chocolate", fontsize=18, verticalalignment='center',horizontalalignment='center', fontstyle="italic")
        plt.text(9, cordtext[-1]-1, self.structureComplete_r, color="black", fontsize=14, fontstyle="italic")
        #PARTIE TRACAGE CASES################
        plt.plot([3, 4, 4, 3, 3], [cordtext[0], cordtext[0], cordtext[0] - 1.0, cordtext[0] - 1.0, cordtext[0]],c="black")
        plt.text(3.5,cordtext[0]+0.2,"s",color="blue",fontsize=13,horizontalalignment="center",verticalalignment="center")

        plt.plot([3,4,4,3,3],[cordtext[1], cordtext[1], cordtext[1] - 1.0, cordtext[1] - 1.0, cordtext[1]],c="black")
        plt.text(3.5, cordtext[1] + 0.2, "s", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(2,5):
            plt.plot([3+i, 4+i, 4+i, 3+i, 3+i], [cordtext[1], cordtext[1], cordtext[1] - 1.0, cordtext[1] - 1.0, cordtext[1]],
                     c="black")
        plt.text(3.5+3, cordtext[1] + 0.2, "p", color="blue", fontsize=13, horizontalalignment="center",verticalalignment="center")

        plt.plot([3, 4, 4, 3, 3], [cordtext[2], cordtext[2], cordtext[2] - 1.0, cordtext[2] - 1.0, cordtext[2]],
                 c="black")
        plt.text(3.5, cordtext[2] + 0.2, "s", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(2,5):
            plt.plot([3+i, 4+i, 4+i, 3+i, 3+i], [cordtext[2], cordtext[2], cordtext[2] - 1.0, cordtext[2] - 1.0, cordtext[2]],
                     c="black")
        plt.text(3.5 + 3, cordtext[2] + 0.2, "p", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(6,11):
            plt.plot([3+i, 4+i, 4+i, 3+i, 3+i], [cordtext[2], cordtext[2], cordtext[2] - 1.0, cordtext[2] - 1.0, cordtext[2]],
                     c="black")
        plt.text(3.5 + 3+5, cordtext[2] + 0.2, "d", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")

        plt.plot([3, 4, 4, 3, 3], [cordtext[3], cordtext[3], cordtext[3] - 1.0, cordtext[3] - 1.0, cordtext[3]],
                 c="black")
        plt.text(3.5, cordtext[3] + 0.2, "s", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(2, 5):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[3], cordtext[3], cordtext[3] - 1.0, cordtext[3] - 1.0, cordtext[3]],
                     c="black")
        plt.text(3.5 + 3, cordtext[3] + 0.2, "p", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(6, 11):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[3], cordtext[3], cordtext[3] - 1.0, cordtext[3] - 1.0, cordtext[3]],
                     c="black")
        plt.text(3.5 + 3 + 5, cordtext[3] + 0.2, "d", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(12, 19):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[3], cordtext[3], cordtext[3] - 1.0, cordtext[3] - 1.0, cordtext[3]],
                     c="black")
        plt.text(3.5 + 3 + 5 + 7, cordtext[3] + 0.2, "f", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")

        plt.plot([3, 4, 4, 3, 3], [cordtext[4], cordtext[4], cordtext[4] - 1.0, cordtext[4] - 1.0, cordtext[4]],
                 c="black")
        plt.text(3.5, cordtext[4] + 0.2, "s", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(2, 5):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[4], cordtext[4], cordtext[4] - 1.0, cordtext[4] - 1.0, cordtext[4]],
                     c="black")
        plt.text(3.5 + 3, cordtext[4] + 0.2, "p", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(6, 11):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[4], cordtext[4], cordtext[4] - 1.0, cordtext[4] - 1.0, cordtext[4]],
                     c="black")
        plt.text(3.5 + 3 + 5, cordtext[4] + 0.2, "d", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(12, 19):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[4], cordtext[4], cordtext[4] - 1.0, cordtext[4] - 1.0, cordtext[4]],
                     c="black")
        plt.text(3.5 + 3 + 5+7, cordtext[4] + 0.2, "f", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")

        plt.plot([3, 4, 4, 3, 3], [cordtext[5], cordtext[5], cordtext[5] - 1.0, cordtext[5] - 1.0, cordtext[5]],
                 c="black")
        plt.text(3.5, cordtext[5] + 0.2, "s", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(2, 5):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[5], cordtext[5], cordtext[5] - 1.0, cordtext[5] - 1.0, cordtext[5]],
                     c="black")
        plt.text(3.5 + 3, cordtext[5] + 0.2, "p", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(6, 11):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[5], cordtext[5], cordtext[5] - 1.0, cordtext[5] - 1.0, cordtext[5]],
                     c="black")
        plt.text(3.5 + 3 + 5, cordtext[5] + 0.2, "d", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")

        plt.plot([3, 4, 4, 3, 3], [cordtext[6], cordtext[6], cordtext[6] - 1.0, cordtext[6] - 1.0, cordtext[6]],
                 c="black")
        plt.text(3.5, cordtext[6] + 0.2, "s", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")
        for i in range(2, 5):
            plt.plot([3 + i, 4 + i, 4 + i, 3 + i, 3 + i],
                     [cordtext[6], cordtext[6], cordtext[6] - 1.0, cordtext[6] - 1.0, cordtext[6]],
                     c="black")
        plt.text(3.5 + 3, cordtext[6] + 0.2, "p", color="blue", fontsize=13, horizontalalignment="center",
                 verticalalignment="center")

        print(st)
        for i in range(len(st)):
            if st[i] not in al and st[i+1] in "spdf":
                if st[i + 1] == "s":

                    for j in range (1,8):
                        if st[i]==str(j):
                            if st[i+2]=='1':
                                plt.arrow(3 + 0.25, cordtext[j-1] - 0.9, 0, 0.5, width=0.07, color="black")
                            else:
                                plt.arrow(3 + 0.25, cordtext[j - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                                plt.arrow(4 - 0.25, cordtext[j - 1] - 0.1, 0, -0.5, width=0.07, color="black")

                if st[i + 1] == "p":
                    for j in range (1,8):
                        if st[i + 2] == '1':
                            plt.arrow(3 +2 + 0.25, cordtext[int(st[i])-1] - 0.9, 0, 0.5, width=0.07, color="black")
                        elif st[i + 2] == '2':
                            for k in range(2, 4):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                        elif st[i + 2] == '3':
                            for k in range(2, 5):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                        elif st[i + 2] == '4':
                            for k in range(2, 5):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                                if k != 3 and k!= 4:
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                              color="black")
                        elif st[i + 2] == '5':
                            for k in range (2,5):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i])-1] - 0.9, 0, 0.5, width=0.07, color="black")
                                if k!=4:
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i])-1] - 0.1, 0, -0.5, width=0.07, color="black")
                        elif st[i + 2] == '6':
                            for k in range (2,5):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i])-1] - 0.9, 0, 0.5, width=0.07, color="black")
                                plt.arrow(4 + k - 0.25, cordtext[int(st[i])-1] - 0.1, 0, -0.5, width=0.07, color="black")

                if st[i + 1] == "d":
                    for j in range(1, 8):
                        if st[i + 2] == '1':
                            if st[i+3]=="0":
                                for k in range(6, 11):
                                    plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                              color="black")
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                              color="black")
                            else:
                                plt.arrow(3 + 6 + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                        elif st[i + 2] == '2':
                            for k in range(6, 8):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                        elif st[i + 2] == '3':
                            for k in range(6, 9):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                        elif st[i + 2] == '4':
                            for k in range(6, 10):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                        elif st[i + 2] == '5':
                            for k in range(6, 11):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                        elif st[i + 2] == '6':
                            for k in range(6, 11):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                                if str(k) not in "78910":
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07, color="black")
                        elif st[i + 2] == '7':
                            for k in range(6, 11):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                                if str(k) not in "8910":
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07, color="black")
                        elif st[i + 2] == '8':
                            for k in range(6, 11):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                                if str(k) not in "910":
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07, color="black")
                        elif st[i + 2] == '9':
                            for k in range(6, 11):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                                if str(k) not in "10":
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07, color="black")
                if st[i + 1] == "f":        # PARTIE FFFFFFF
                    for j in range(1, 8):
                        if st[i + 2] == '1':
                            if st[i+3]=="4":
                                for k in range(12, 19):
                                    plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                              color="black")
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                              color="black")
                            elif st[i+3]=="3":
                                for k in range(12, 19):
                                    plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                              color="black")
                                    if str(k) not in "18":
                                        plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                                  color="black")
                            elif st[i+3]=="2":
                                for k in range(12, 19):
                                    plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                              color="black")
                                    if str(k) not in "1718":
                                        plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                                  color="black")
                            elif st[i+3]=="1":
                                for k in range(12, 19):
                                    plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                              color="black")
                                    if str(k) not in "161718":
                                        plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                                  color="black")
                            elif st[i+3]=="0":
                                for k in range(12, 19):
                                    plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                              color="black")
                                    if str(k) not in "15161718":
                                        plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                                  color="black")
                            else:
                                plt.arrow(3 + 6 + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                        elif st[i + 2] == '2':
                            for k in range(12, 14):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                        elif st[i + 2] == '3':
                            for k in range(12, 15):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                        elif st[i + 2] == '4':
                            for k in range(12, 16):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07,
                                          color="black")
                        elif st[i + 2] == '5':
                            for k in range(12, 17):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                        elif st[i + 2] == '6':
                            for k in range(12, 18):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                        elif st[i + 2] == '7':
                            for k in range(12, 19):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                        elif st[i + 2] == '8':
                            for k in range(12, 19):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                                if str(k) not in "131415161718":
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                              color="black")
                        elif st[i + 2] == '9':
                            for k in range(12, 19):
                                plt.arrow(3 + k + 0.25, cordtext[int(st[i]) - 1] - 0.9, 0, 0.5, width=0.07, color="black")
                                if str(k) not in "1415161718":
                                    plt.arrow(4 + k - 0.25, cordtext[int(st[i]) - 1] - 0.1, 0, -0.5, width=0.07,
                                              color="black")


        if self.structureAllegee!=None:
            plt.title("Structure de "+self.structureAllegee,color="red",fontsize=20)
        else:
            plt.title("Structure de " + self.structureComplete, color="red", fontsize=20)
        plt.legend([self.structureValence],edgecolor="black",labelcolor="red",shadow=1)
        plt.show()






#Atomistique(5, "casesQuantiques")
#Atomistique("U", "casesQuantiques")


#Atomistique("Cr2+", "casesQuantiques")


Atomistique("Cr---", "casesQuantiques")
Atomistique("Br+", "structureAllegee")








