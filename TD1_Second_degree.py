def second_degre(a,b,c):
    if a == 0:
        resultat= "Ce n'est pas une fonction polynôme du second degré"
    else:
        x= -b/(2*a)
        if a > 0:

            resultat= "Elle est décroissante sur  ]-inf ; "+str(x)+"] puis croissante sur ["+str(x)+" ; +inf[."
        else:
            
            resultat ="Elle fonction est croissante sur  ]-inf ; "+str(x)+"] puis décroissante sur ["+str(x)+" ; +inf[."
    return resultat