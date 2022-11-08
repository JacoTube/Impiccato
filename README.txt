### Dati Personali
1. [Nome]: Jacopo Pio Vicchio
2. [Matricola]: 230566
3. [Corso di Laurea]: Ingegnria Informatica
4. [Nome Progetto]: Impiccato by JacoTube
5. [Contatti]: vccjpp02h20c349x@studenti.unical.it, jacopovicchio02@gmail.com

### Info Generali
Il programma è una versione in Python del famoso gioco dell'impiccato, il quale consiste nell'indovinare una parola, conoscendone inzialmente solo la lunghezza e provando gradualmente 
ad inserire lettere, fino al massimo di tentativi possibili, che varia a seconda dei dettagli che si vogliono aggiungere al disegno che raffigura il caratteristico "omino".

### Tecnologie Utilizzate
* [Python] Versione 3.7
* [Microsoft Visual Studio Code] Versione 1.63.2
* [paroleitaliane by napolux] (https://github.com/napolux/paroleitaliane)

### Installazione
Per usare il gioco è necessario aprire il file "#Impiccato.py" con un qualsiasi editor di linguaggio ed effettuare il debug. È obbligatorio che all'interno della cartella
siano presenti i quattro file .txt contenenti una lista di parole italiane.

### Struttura Programma
Il programma, all'avvio, chiede di scegliere la difficoltà tra le 4 disponibili, una volta inserito il numero della scelta corrispondente alla difficoltà desiderata, il programma cancellerà
ciò che è stato scritto finora e stamperà la struttura dell'impiccato sopra a dei trattini il cui numero corrispondete alla lunghezza della parola che il programma ha scelto atraverso la
libreria "random". Il programma chiede di inserire un carattere o una parola; qui bisogna inserire il tentativo, il programma riconoscerà in automatico se si sta cercando di indovinare l'intera
parola o una sola lettera di essa. A questo punto dell'esecuzione il programma risponderà di conseguenza all'input inserito, aggiungendo una lettera nella lista dei trattini sottostanti alla
struttura, oppure aggiungendo una parte del corpo ad essa. Il gioco terminerà quando la parola sarà completata, o quando i tentativi a disposizione saranno finiti, in quest'ultimo caso, il 
programma restituirà la parola che non si è riusciti ad indovinare. Come atto finale del ciclo, viene chiesto all'utente se vuole giocare ancora o chiudere il gioco, nella caso della prima,
si ripartirà dalla scelta della difficoltà, nella seconda il programma verrà chiuso, ringraziando l'utente per aver giocato.

### Spiegazione di "def impiccato()"
La funzione impiccato è divisa in tre pezzi principali:
1. Dichiarazione delle variabili: 
	vengono dichiarate un totale di 6 variabili:
	1. tentativi: verrà usata per tenere il conto dei tentativi provati dall'utente;
	2. parola: la parola scelta dalla lista;
	3. lista_parola: la variabile "parola" sotto forma di lista a cui poi viene rimosso l'ultimo posto nella lista, poiché su tratta di un "\n";
	4. trattini: i trattini sottostanti al disegno della struttura;
	5. nuovi_trattini: una lista uguale alla precendete;
	6. lettere_usate: verrà usata per ricordare all'utente quali lettere sono state usate;

2. Input e riconoscimento: 
	il sistema stampa la struttura ed entra in un while da cui si può uscire solo indovinando la parola e terminando i tentativi disponibili:
	1. input: viene chiesto di inserire in input un carattere o una parola;
	2. riconoscimento: al variare della lunghezza dell'input, il programma riconosce se è vuoto (chiederà di reinserire l'input), se è un carattere o una parola;

3. Controllo della risposta:
	1. parola: se l'input inserito è una parola, il programma controllerà se la lista dell'input è uguali, e si comportà di conseguenza (aggiungendo +1 tentativi oppure facendo vincere l'utente)
	2. carattere: se l'input inserito è un carattere, il programma controllerà se l'elemento ha corrispondenza nella parola, se sì aggiungerà la lettera nell'indice corrispondente nella lista nuovi_trattini,
		      confronterà quindi la lista nuovi_trattini con trattini, e se le due sono uguali, significa che il carattere non era presente, quindi aggiunge un tentativo, altrimenti aggiorna la lista trattini,
		      controlla infine se nuovi_trattini è uguale a lista_parola, restituendo vittoria in quel caso.

