from functions import gener_bloc

if __name__ == "__main__":
    resultat = ""
    for i in range (1000):
        resultat += gener_bloc()
    print(resultat)
    input("Appuyez sur Entrée pour quitter...")