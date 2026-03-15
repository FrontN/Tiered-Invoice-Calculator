def calcolo_fattura(numero_copie, prezzi_stampa, punti_riferimento):
    """
    Calcola la fattura di un certo numero di copie in base ai prezzi di stampa e ai punti di riferimento.
    
    Parameters
    ----------
    numero_copie : int
        Il numero di copie da calcolare la fattura.
    prezzi_stampa : list
        I prezzi di stampa per ogni punto di riferimento.
    punti_riferimento : list
        I punti di riferimento per ogni prezzo di stampa.
    
    Returns
    -------
    str
        La fattura calcolata.
    """
    if len(prezzi_stampa) != len(punti_riferimento):
        raise ValueError("La lunghezza di prezzi_stampa deve essere uguale alla lunghezza di punti_riferimento.")

    riferimento = sorted(punti_riferimento)

    fattura = 0
    for i, p in enumerate(riferimento[::-1]):
        if p != 0 and p < numero_copie:
            A = numero_copie - p
            fattura += A * prezzi_stampa[-(i +1)]
            numero_copie -= A
    fattura += numero_copie * prezzi_stampa[0]
    return f"{fattura:.2f}€"

p_stampa = [0.30, 0.25, 0.20]
p_riferimento = [0, 10, 30]

while True:
    try:
        nb_copie = input("Inserisci il numero di copie: ")
        nb_copie = int(nb_copie)
        if nb_copie < 0:
            print("Il numero di copie deve essere un intero positivo.")
            continue
        print(calcolo_fattura(nb_copie, p_stampa, p_riferimento))
        break
    except ValueError:
        print("Devi inserire un numero intero.")
