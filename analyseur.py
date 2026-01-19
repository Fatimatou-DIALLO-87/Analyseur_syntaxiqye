import re


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
        'Liste_instructions': ['Une_instruction', 'Liste_instructions']
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
        'Test': ['if', 'Condition', 'Une_instruction', 'else', 'Une_instruction']
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




def decouper_chaine(chaine):
    
    combiner_symboles = [r'main\(\)\{', r'==']  # regex pour 'main(){' et '=='

    # reconstruction de la chaine
    regex = '|'.join(combiner_symboles) + r'|\w+|[=;<>}]'

    chaine_decoupe = re.findall(regex, chaine)
    return chaine_decoupe


#implementation de l'algorithme de construction de la table d'analyse

def analyser_chaine(chaine):

    symbole_non_terminaux= ["Programme","Liste_declarations",
                            "Liste_instructions","Une_declaration",
                            "Une_instruction","Affectation","Test",
                            "Condition","Operation","Type"]
    pile = []
    liste_regle=[]
    chaine_accept= False
    chaine_non_accept = False
    chaine = decouper_chaine(chaine)
    chaine.append("$")
    pile.append("$")
    pile.append("Programme")
    i=0

    while chaine_non_accept == False and chaine_accept == False :
        a = chaine[i]
        X = pile[-1]
       
        if X in symbole_non_terminaux :
            cle = (X, a)
            if cle in tableAnalyse:
                valeurs = tableAnalyse[cle]
                pile.pop()
                liste_regle.append(valeurs)
                
                regle = list(valeurs[X])
                regle.reverse()
                if  'vide' not in regle: 
                    pile = pile + regle
            else:
                chaine_non_accept = True

        else:
            if X == "$" :
                if a == "$" :
                    chaine_accept = True
                else:
                    chaine_non_accept = True
            elif X == a :
                    pile.pop()
                    i+= 1
            elif X == "vide" :
                    pile.pop()
            else:     
                chaine_non_accept= True

    return chaine_accept, liste_regle
