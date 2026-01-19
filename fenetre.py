from tkinter import *
from tkinter import Tk
from analyseur import analyser_chaine
from arbre import *
from arbre import construire_arbre, ArbreGraphique

result = False
liste_regle = []

# Police de texte
my_font = "Helvetica 12"

#===================== Couleurs =========================
COLOR_BG = "#ECEFF1"
COLOR_HEADER = "#263238"
COLOR_ENTRY = "#90A4AE"
COLOR_BUTTON = "#546E7A"
COLOR_BUTTON_HOVER = "#455A64"
COLOR_TEXT = "#212121"
COLOR_ACCENT = "#00BCD4"

arbre = None

# ===================== Fenêtre principale ===================================
root = Tk()
root.title("ANALYSEUR SYNTAXIQUE")
root.configure(bg=COLOR_BG)
root.geometry("800x600")
root.minsize(800, 600)
root.resizable(True, True)

# ===================== Fonctions =====================

#Fonction qui genère l'abre syntaxique
def generer_arbre():
    global arbre
    frame_ch_accepter.pack_forget()
    frame_arbre.pack(fill="both", expand=True)
    canvas.delete("all")
    racine = construire_arbre(liste_regle)
    if arbre is None:
        arbre = ArbreGraphique(canvas)
    arbre.afficher(racine)

#Supprimer la chaine entrée
def clear_entry(event):
    if entry_error.get():
        entry.delete(0, END)
        entry.config(fg="black")
        entry_error.set(False)

#Changer de frame
def changer_frame(frame_actuelle, frame_suivante):
    frame_actuelle.pack_forget()
    frame_suivante.pack(fill="both", expand=True)

#Supprimer le texte d'erreur
def clear_error_text():
    text_erreur.config(state="normal")
    text_erreur.delete("1.0", END)
    text_erreur.config(state="disabled")
    scroll_erreur.pack_forget()  # masquer scrollbar par défaut

#Fonction qui permet de lancer l'analyse
def lancer_analyse():
    global liste_regle
    if entry_error.get():
        return

    texte = entry.get().strip()
    clear_error_text()

    if texte == "":
        entry.delete(0, END)
        entry.insert(0, "⚠ Veuillez entrer une chaîne !")
        entry.config(fg="red")
        entry_error.set(True)
        root.focus()
        return

    entry.config(fg="black")
    result, liste_regle = analyser_chaine(texte)

    if result:
        entry.delete(0, END)
        entry_error.set(False)

        text_chaine.config(state="normal")
        text_chaine.delete("1.0", END)
        text_chaine.insert("end", "Chaine : ", "bold")
        text_chaine.insert("end", texte)
        text_chaine.tag_add("center", "1.0", "end")
        text_chaine.config(state="disabled")

        clear_error_text()
        changer_frame(main_frame, frame_ch_accepter)

    else:
        text_erreur.config(state="normal")
        text_erreur.insert("end", "❌ Chaine non acceptée\n", "error")
        if liste_regle:
            text_erreur.insert("end", "Règles appliquées jusqu'ici :\n", "rules")
            for i, r in enumerate(liste_regle):
                for gauche, droite in r.items():
                    regle_str = " ".join(droite)
                    if i == len(liste_regle) - 1:
                        # dernière règle en rouge
                        text_erreur.insert("end", f"{gauche} → {regle_str}\n", "last_rule")
                    else:
                        text_erreur.insert("end", f"{gauche} → {regle_str}\n", "rules")

        text_erreur.config(state="disabled")

        # Vérifier si le texte dépasse la zone visible et activer scrollbar si besoin
        text_erreur.update_idletasks()
        if text_erreur.yview()[1] < 1.0:  # si le bas n'est pas visible
            scroll_erreur.pack(side=RIGHT, fill=Y)


#Fonction qui affiche les règles appliquées 
def affiche_regles():
    frame_ch_accepter.pack_forget()
    frame_regles.pack(fill="both", expand=True)
    text_regles.config(state="normal")
    text_regles.delete("1.0", END)
    for r in liste_regle:
        for gauche, droite in r.items():
            regle_str = " ".join(droite)
            text_regles.insert("end", f"{gauche} → {regle_str}\n\n")
    text_regles.config(state="disabled")

#Permet d'harmoniser les boutons
def style_button(parent, text, command, color=COLOR_BUTTON):
    btn = Button(parent, text=text, width=20, font=("Poppins", 12),
                 bg=color, fg="white", relief="flat", cursor="hand2", command=command)
    btn.bind("<Enter>", lambda e: btn.config(bg=COLOR_BUTTON_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=color))
    btn.pack(pady=10)
    return btn

# ===================== FRAME PRINCIPALE =====================
main_frame = Frame(root, bg=COLOR_BG)
main_frame.pack(fill="both", expand=True)


Label(main_frame, text="ANALYSEUR SYNTAXIQUE",
      font=("Poppins", 22, "bold"), bg=COLOR_HEADER, fg="white", height=2).pack(fill="x")

frame = Frame(main_frame, bg=COLOR_BG, pady=20)
frame.pack(fill="both", expand=True)

Label(frame, text="Entrez votre chaîne", font=("Poppins", 18, "bold"), fg=COLOR_TEXT, bg=COLOR_BG).pack(pady=(10, 10))
entry = Entry(frame, font=my_font, background=COLOR_ENTRY, relief="flat", justify="center", fg="black")
entry.pack(fill="x", ipady=6, padx=50)
entry_error = BooleanVar(value=False)
entry.bind("<FocusIn>", clear_entry)

# Bouton analyser
btn_analyser = style_button(frame, "ANALYSER", lancer_analyse)

# Frame pour l'erreur (Text + scrollbar optionnel)
frame_erreur = Frame(frame, bg=COLOR_BG, height=150)  
frame_erreur.pack(fill="x", padx=50, pady=(5,0))

text_erreur = Text(frame_erreur, height=20, font=("Helvetica", 12), wrap="word",
                   bg=COLOR_BG, relief="flat")
text_erreur.pack(side=LEFT, fill="both", expand=True)

scroll_erreur = Scrollbar(frame_erreur, command=text_erreur.yview)
scroll_erreur.pack(side=RIGHT, fill=Y)
text_erreur.config(yscrollcommand=scroll_erreur.set)


# Tags pour couleur
text_erreur.tag_configure("error", foreground="red")
text_erreur.tag_configure("rules", foreground="#555555")
text_erreur.tag_configure("last_rule", foreground="red")

# Label pour afficher les erreurs et règles partiellement appliquées
label_erreur = Label(frame, text="", font=("Helvetica", 12), fg="red", bg=COLOR_BG, justify="left")
label_erreur.pack(anchor="w", padx=50, pady=(5,0))


# ===================== FRAME CHAÎNE ACCEPTÉE =====================
frame_ch_accepter = Frame(root, bg=COLOR_BG)

Label(frame_ch_accepter, text="CHAÎNE ACCEPTÉE ✅", font=("Poppins", 20, "bold"),
      bg=COLOR_HEADER, fg="white", height=2).pack(fill="x")

frame_label = Frame(frame_ch_accepter, bg=COLOR_BG, width=700)
frame_label.pack(pady=10)

# Text pour afficher "Chaine : <texte>" avec "Chaine" en gras
text_chaine = Text(frame_label, height=2, font=("Helvetica", 14), bg=COLOR_BG,
                   fg=COLOR_HEADER, wrap="word", bd=0, relief="flat")
text_chaine.pack(fill="both")

# Tag pour gras
text_chaine.tag_configure("bold", font=("Helvetica", 14, "bold"))

# Tag pour centrer
text_chaine.tag_configure("center", justify="center")

# Rendre le Text en lecture seule
text_chaine.config(state="disabled")


style_button(frame_ch_accepter, "Afficher règles", affiche_regles)
style_button(frame_ch_accepter, "Afficher arbre syntaxique", generer_arbre)
style_button(frame_ch_accepter, "← Retour", lambda: changer_frame(frame_ch_accepter, main_frame), color=COLOR_HEADER)

# ===================== FRAME RÈGLES =====================
frame_regles = Frame(root, bg=COLOR_BG)
frame_regles.pack_forget()

Label(frame_regles, text="Règles appliquées", font=("Poppins", 20, "bold"),
      bg=COLOR_HEADER, fg="white", height=2).pack(fill="x")

text_regles = Text(frame_regles, wrap="word", font=("Consolas", 12),
                   bg="#FAFAFA", fg=COLOR_TEXT, relief="flat", height=15)
text_regles.pack(fill="both", expand=True, pady=10, padx=20)
text_regles.config(state="disabled")

style_button(frame_regles, "← Retour", lambda: changer_frame(frame_regles, frame_ch_accepter), color=COLOR_HEADER)


# ===================== FRAME ARBRE =====================
frame_arbre = Frame(root, bg=COLOR_BG)
frame_arbre.pack_forget()

Label(frame_arbre, text="ARBRE SYNTAXIQUE", font=("Poppins", 20, "bold"),
      bg=COLOR_HEADER, fg="white", height=2).pack(fill="x")

canvas_frame = Frame(frame_arbre, bg=COLOR_BG)
canvas_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))
canvas = Canvas(canvas_frame, bg="#FAFAFA")
canvas.pack(side=LEFT, fill="both", expand=True)

scroll_y = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scroll_y.pack(side="right", fill="y")

scroll_x = Scrollbar(frame_arbre, orient="horizontal", command=canvas.xview)
scroll_x.pack(side="top", fill="x")

canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

style_button(frame_arbre, "← Retour", lambda: changer_frame(frame_arbre, frame_ch_accepter), color=COLOR_HEADER)

# ===================== Lancer l'application =====================
root.mainloop()
