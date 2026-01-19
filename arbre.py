class Node:
    def __init__(self, nom):
        self.value = nom         
        self.children = []        
        self.nb_feuilles = 1      

    def add_child(self, enfant):
        self.children.append(enfant)


# fonction qui construit l'arbre à partir des règles et retourne la racine
def construire_arbre(liste_regle):
    racine = None  
    noeuds = {}         
    for regle in liste_regle:
        for gauche, droite in regle.items():
            if gauche not in noeuds:
                noeuds[gauche] = Node(gauche)
                if racine is None:
                    racine = noeuds[gauche]
            parent = noeuds[gauche]
            for symbole in droite:
                enfant = Node(symbole)
                parent.add_child(enfant)
                for r in liste_regle:
                    cle = next(iter(r))
                    if symbole == cle:
                        noeuds[symbole] = enfant
                        break
    return racine


# Compte le nombre de feuilles
def compter_feuilles(node):
    if not node.children:
        node.nb_feuilles = 1
    else:
        node.nb_feuilles = 0
        for enfant in node.children:
            node.nb_feuilles += compter_feuilles(enfant)
    return node.nb_feuilles


# fonction qui calcule les positions x,y des nœuds pour l'affichage graphique
def placer_noeuds(noeud, profondeur, x_min, x_max, positions, hauteur=120, marge=80):
    x = (x_min + x_max) / 2
    y = marge + profondeur * hauteur
    positions[noeud] = (x, y)
    if not noeud.children:
        return
    largeur = x_max - x_min
    position_courante = x_min
    for enfant in noeud.children:
        largeur_enfant = (enfant.nb_feuilles / noeud.nb_feuilles) * largeur
        placer_noeuds(enfant, profondeur + 1, position_courante,
                      position_courante + largeur_enfant, positions, hauteur, marge)
        position_courante += largeur_enfant


# class qui gere l'affichage graphique de l'arbre dans un canvas
class ArbreGraphique:

    def __init__(self, canvas):
        self.canvas = canvas
        self.zoom = 1.0
        self.racine = None
        self.canvas.bind("<Control-MouseWheel>", self.zoom_molette)

    # ici on change le zoom avec CTRL + molette
    def zoom_molette(self, event):
        if event.delta > 0:
            self.zoom *= 1.1
        else:
            self.zoom /= 1.1
        self.redessiner()

    # fonction qui affiche l'arbre à partir de la racine
    def afficher(self, racine):
        self.racine = racine
        self.redessiner()

    # cette fonction fface et redessine l'arbre
    def redessiner(self):
        self.canvas.delete("all")
        if self.racine is None:
            return
        compter_feuilles(self.racine)
        positions = {}
        largeur_totale = max(800, self.racine.nb_feuilles * 190)
        placer_noeuds(self.racine, 0, 0, largeur_totale, positions)
        self.dessiner_depuis_positions(positions)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # Dessine les nœuds et les liens parent-enfant
    def dessiner_depuis_positions(self, positions):
        rectangles = {}
        marge_x = 14 * self.zoom
        marge_y = 14 * self.zoom

        # Calcul des rectangles pour chaque nœud
        for noeud, (x, y) in positions.items():
            x *= self.zoom
            y *= self.zoom
            temp = self.canvas.create_text(x, y, text=noeud.value,
                                        font=("Consolas", int(14 * self.zoom), "bold"))
            x1, y1, x2, y2 = self.canvas.bbox(temp)
            self.canvas.delete(temp)
            rectangles[noeud] = (x1 - marge_x, y1 - marge_y, x2 + marge_x, y2 + marge_y)

        # Dessine les lignes parent-enfant
        for parent, (x1, y1, x2, y2) in rectangles.items():
            px = (x1 + x2) / 2
            py = y2
            for enfant in parent.children:
                ex1, ey1, ex2, ey2 = rectangles[enfant]
                cx = (ex1 + ex2) / 2
                cy = ey1
                self.canvas.create_line(px, py, cx, cy, fill="#777", width=1.5)

        # Dessine les rectangles et le texte des nœuds avec couleur selon présence d'enfants
        for noeud, (x1, y1, x2, y2) in rectangles.items():
            if not noeud.children:
                
                if noeud.value.strip() == "vide":
                    couleur = "#FFCDD2"  # rouge pour mot vide
                else:
                    couleur = "#D7E3EC"  
            else:
                couleur = "#C8E6C9"  # parent -> vert clair

            self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur,
                                        outline="#0369A1", width=1.4)
            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=noeud.value,
                                    font=("Consolas", int(14 * self.zoom), "bold"))
