tableAnalyse = {
    ('Programme', 'main(){'): {
        'Programme': ['main(){', 'Liste_declarations', 'Liste_instructions', '}']
    },

    ('Liste_declarations','}'): {
        'Liste_declarations': ['vide']
    },
    ('Liste_declarations', 'int'): {
        'Liste_declarations': ['Une_declaration', 'Liste_declarations']
    },
    ('Liste_declarations', 'float'): {
        'Liste_declarations': ['Une_declaration', 'Liste_declarations']
    },
    ('Liste_declarations', 'id'): {
        'Liste_declarations': ['vide']
    },
    ('Liste_declarations', 'if'): {
        'Liste_declarations': ['vide']
    },
    ('Liste_declarations', 'vide'): {
        'Liste_declarations': ['vide']
    },

    ('Une_declaration', 'int'): {
        'Une_declaration': ['Type', 'id']
    },
    ('Une_declaration', 'float'): {
        'Une_declaration': ['Type', 'id']
    },

    ('Liste_instructions', '}'): {
        'Liste_instructions': ['vide']
    },
    ('Liste_instructions', 'id'): {
        'Liste_instructions': ['Une_instruction', 'Liste_instructions']
    },
    ('Liste_instructions', 'if'): {
        'Liste_instructions': ['Une_instruciton', 'Liste_instructions']
    },
    ('Liste_instructions', 'vide'): {
        'Liste_instructions': ['vide']
    },

    ('Une_instruction', 'id'): {
        'Une_instruction': ['Affectation']
    },
    ('Une_instruction', 'if'): {
        'Une_instruction': ['Test']
    },

    ('Type', 'int'): {
        'Type': ['int']
    },
    ('Type', 'float'): {
        'Type': ['float']
    },

    ('Affectation', 'id'): {
        'Affectation': ['id','=', 'nombre', ';']
    },

    ('Test', 'if'):{
        'Test': ['if', 'Condition', 'une_instruction', 'else', 'une_instruction', ';']
    },

    ('Condition', 'id'): {
        'Condition': ['id', 'Operation', 'nombre']
    },

    ('Operation', '<'): {
        'Operation': ['<']
    },
    ('Operation', '>'): {
        'Operation': ['>']
    },
        ('Operation', '=='): {
        'Operation': ['==']
    }
}

#Affichage de la table d'Analyse
print("la Table d'Analyse:")
for cles, vals in tableAnalyse.items():
    print(cles, '-->', vals)

def analyseur(chaine):
    symbole_non_terminaux= ["Programme","Liste_declarations","Liste_instructions","Une_declaration","Une_instruction","Affectation","Test","Condition","Operation","Type"]
    pile = []
    liste_regle=[]
    chaine_accept= False
    chaine_non_accept = False
    chaine += "$"
    pile.append("$")
    pile.append("Programme")
    i=0
    while chaine_non_accept == False and chaine_accept == False :
        a = chaine[i]
        print(a)
        X = pile[-1]
        print(X)
        if X in symbole_non_terminaux :
            cle = (X, a)
            if cle in tableAnalyse:
                valeurs = tableAnalyse[cle]
                pile.pop()
                liste_regle.append(valeurs)

                # --- COPIE la règle pour ne pas modifier la table ---
                regle = list(valeurs[X])
                regle.reverse()

                if 'vide' not in regle:
                    pile = pile + regle

                print(pile)

            else:
                erreur = True

        else:
            if X == "$" :
                if a == "$" :
                    chaine_accept = True
                else:
                    chaine_non_accept = True
            elif X == a :
                    pile.pop()
                    print(pile)
                    i+= 1
            elif X == "vide" :
                    pile.pop()
                    print(pile)
            else:     
                chaine_non_accept= True

    if chaine_accept:
        print("chaine acceptée")
    else:
        print("chaine non acceptée")

chaine = ["main(){","int","id","float","id","id","=","nombre",";",'}']
chaine2 = ["main(){","int","id","float","id","id","=","nombre",";",'}']
analyseur(chaine)
analyseur(chaine2)





analyseur(chaine)

