#Impiccato

import os      #necessario per integrare la funzione os.system('cls') nella cancellazione del blocco comandi in corso di debug (funzione unicamente grafica)
import random   #necessario per integrare la funzione random.choice() per la scelta casuale della parola

def stampa_struttura(tentativi, parola):       #funzione che si occupa stampare il classico disegno che rappresenta l'impiccatto, con ascii
    if tentativi == 0:
        print("_________")
        print("|       |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_______")
    elif tentativi == 1:
        print("_________")
        print("|       |")
        print("|     (*﹏*;)")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_______")
    elif tentativi == 2:
        print("_________")
        print("|       |")
        print("|     (*﹏*;)")
        print("|        |")
        print("|")
        print("|")
        print("|")
        print("|_______")
    elif tentativi == 3:
        print("_________")
        print("|       |")
        print("|     (*﹏*;)")
        print("|       /|")
        print("|")
        print("|")
        print("|")
        print("|_______")
    elif tentativi == 4:
        print("_________")
        print("|       |")
        print("|     (*﹏*;)")
        print("|       /|\  ")
        print("|")
        print("|")
        print("|")
        print("|_______")
    elif tentativi == 5:
        print("_________")
        print("|       |")
        print("|     (*﹏*;)")
        print("|       /|\  ")
        print("|        |")
        print("|")
        print("|")
        print("|_______")
    elif tentativi == 6:
        print("_________")
        print("|       |")
        print("|     (*﹏*;)")
        print("|       /|\  ")
        print("|        |")
        print("|       /")
        print("|")
        print("|_______")
    elif tentativi == 7:
        print("_________")
        print("|       |")
        print("|     (X_X)")
        print("|      /|\  ")
        print("|       |   ")
        print("|      / \  ")
        print("|")
        print("|_________")

def scelta_parola(scelta):     #funzione che si occupa ricevere in input la scelta della difficoltà del giocatore e sceglie attraverso la libreria random una parola casuale presente tra le linee del file
    if scelta == '0':
        file = open('[0]1000_parole_italiane.txt', 'r')
        parola = random.choice(file.readlines())
        return parola

    elif scelta == '1':
        file = open('[1]60000_parole_italiane.txt', 'r')
        parole = file.readlines()
        parola = random.choice(parole)
        return parola

    elif scelta == '2':
        file = open('[2]280000_parole_italiane.txt', 'r')
        parole = file.readlines()
        parola = random.choice(parole)
        return parola

    elif scelta == '3':
        file = open('[3]660000_parole_italiane.txt', 'r')
        parole = file.readlines()
        parola = random.choice(parole)
        return parola

    elif scelta == '4':
        file = open('[4]lista_badwords.txt', 'r')
        parole = file.readlines()
        parola = random.choice(parole)
        return parola

def impiccato(difficolta):          #funzione che rappresenta la struttura principale del gioco dell'impiccato

    tentativi = 0
    parola = scelta_parola(difficolta)
    lista_parola = list(parola)
    lista_parola.remove(parola[len(parola) - 1])
    trattini = list('_'*(len(parola) - 1))
    nuovi_trattini = list(trattini)
    lettere_usate = []

    os.system('cls')
    stampa_struttura(tentativi, parola)
    print('' + ' '.join(trattini))
    
    while tentativi < 7:
        indovina = str(input("Inserisci un carattere o una parola: "))
        indovina = indovina.lower()

        if len(indovina) > 1:
            if list(indovina) == lista_parola:
                os.system('cls')
                stampa_struttura(tentativi, parola)
                print('Ottimo lavoro! Hai vinto indovinando la parola "' + str(parola.replace('\n', '')) + '" utilizzando ' + str(tentativi) + ' tentativi')
                gioca_ancora()
            else:
                tentativi += 1
                os.system('cls')
                stampa_struttura(tentativi, parola)
                print('' + ' '.join(trattini))
                print('La parola inserita non è quella corretta...')
                
                if tentativi >= 7:
                    print('Hai perso, la parola era: ' + str(parola.replace('\n', '')))
                    gioca_ancora()

        elif indovina == '':
            print('Non puoi lasciare tutto vuoto!')

        elif indovina in lettere_usate:
            os.system('cls')
            stampa_struttura(tentativi, parola)
            print('' + ' '.join(trattini))
            print("Hai già provato questa lettera!")
            print('Queste sono le lettere provate: ' + str((lettere_usate)))

        else:
            lettere_usate.append(indovina)
            for i in range(len(lista_parola)):
                if indovina == lista_parola[i]:
                    nuovi_trattini[i] = lista_parola[i]
            if trattini == nuovi_trattini:
                tentativi += 1
                os.system('cls')
                if tentativi < 7:
                    print('La lettera inserita non si trova nella parola')
                    print('Riprova ancora!')
                    stampa_struttura(tentativi, parola)
                    print(' '.join(trattini))
                else:
                    os.system('cls')
                    stampa_struttura(tentativi, parola)
                    print('' + ' '.join(trattini))
                    print('Hai perso, la parola era: ' + str(parola.replace('\n', '')))
                    gioca_ancora()
            elif lista_parola != trattini:
                trattini = nuovi_trattini[:]
                os.system('cls')
                stampa_struttura(tentativi, parola)
                print(' '.join(trattini))
                if lista_parola == trattini:
                    print('Ottimo lavoro! Hai vinto indovinando la parola "' + str(parola.replace('\n', '')) + '" sbagliando ' + str(tentativi) + ' volte')
                    gioca_ancora()

def gioca_ancora():        #funzione che si occupa di chiedere all'utente se desidera rigiocare o uscire dal gioco
    ciclo = True
    while ciclo == True:
        print('\n')
        print("La partita è finita, vuoi...")
        print("1 - Giocare ancora!")
        print("2 - Uscire dal programma.")
        scelta = int(input("Inserisci il numero della scelta corrispondente: "))
        if scelta == 1:
            ciclo = False
            os.system('cls')
            gioco()
        elif scelta == 2:
            ciclo = False
            os.system('cls')
            print('Grazie per aver giocato con me!')
            quit()
        else:
            os.system('cls')
            print("Devi inserire un'opzione valida!")

def gioco():           #funzione che si occopa di far scegliere all'utente la difficoltà desiderata
    print('\n')
    print("0 - Facile (1.000 Parole)")
    print("1 - Medio (60.000 Parole)")
    print("2 - Difficile (280.000 Parole)")
    print("3 - Impossibile (660.000 Parole)")
    print("4 - Parolacce (400 Parolacce) - ATTENZIONE: CONTENUTO FORTE, BLASFEMO E +18")
    indice_difficolta = input("Per iniziare, inserisci il numero corrispondente alla difficoltà di gioco desiderata: ")

    impiccato(indice_difficolta)

os.system('cls')
print("Benevenuto nel gioco dell'Impiccato!")
gioco()
