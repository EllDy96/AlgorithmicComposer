import numpy as np
import random as rm
from music21 import * 
import os
import types
import random
#definisco lo spazio degli stati della catena di Markov come un dizionario che associa ad ogni nota un numero da 0 a 11
LetterToNumber= {'A' : 0, 'A#': 1,'B-':1 ,'B': 2,'C-':2,'B#':3, 'C':3, 'C#': 4,'D-':4, 'D': 5, 'D#': 6,'E-':6, 'E': 7,'F-':7,'E#':8, 'F': 8, 'F#': 9,'G-':9, 'G': 10, 'G#':11,'A-':11}

letter=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

number= range(12)
NumberToLetter={}
for n in number:
	NumberToLetter[n]=letter[n]


letter5 = {'A': 'A5', 'A#': 'A#5', 'B': 'B5', 'C': 'C5', 'C#': 'C#5', 'D': 'D5', 'D#': 'D#5', 'E': 'E5','F': 'F5','F#': 'F#5', 'G': 'G5','G#': 'G#5' }
# quando si crea una nota senza specificare l'ottava music21 imposta come numero di ottava di default la quarta.
#per ottenere l'ottava maggiore corrispondente basterà aggiungere alla nota nella sequenza il numero 5 come D5, C#5. 
letter4 = {'A': 'A4', 'A#': 'A#4', 'B': 'B4', 'C': 'C4', 'C#': 'C#4', 'D': 'D4', 'D#': 'D#4', 'E': 'E4','F': 'F4','F#': 'F#4', 'G': 'G4','G#': 'G#4' }


transitionFrequencyMatrix=np.zeros((12,12))#matrice della frequenza di transizione tra ogni nota inizializzata come matrice di zeri
transitionProbabilityMatrix=np.zeros((12,12)) #matrice delle probabilità di transizione 


'''
creo la matrice di transizione [12x12] di zeri 
leggo una nota alla volta, la converto in numero da zero ed 11, leggo quella successiva, la converto in numero e incremento di uno la casella della matrice in 
posizione ab dove a è la prima nota e b è la seconda
'''

abcFiles = os.listdir('./ABC_files')

for abcFile in abcFiles:
	abcFilePath = os.path.abspath(os.path.join('ABC_files', abcFile))

	opus = converter.parseFile(abcFilePath)

	for score in opus.scores:
		scoreKey= score.analyze('key')# ottengo la tonalità del componimento
		scoreKeytonic= scoreKey.tonic #ottengo la tonica della tonalità eliminando il "major" o "minor"
		keyNumber=LetterToNumber[scoreKeytonic.name] #trasformo la key nel numero corrispondente 
		

		distance= 3 - keyNumber  #distance between scoreKeyTonic and C note
		
	
		
		
		temp= None         #creo una variabile temp che salvi l'ultima nota del ciclo per  compararla con la successiva
		for n in score.flat.iter.notes:
			if n.isNote:#entra nell'if solo se l'oggetto del ciclo è di tipo note.Note
				notetranspose= n.transpose(distance)
				#print(notetranspose)
				
				noteNumber= LetterToNumber[notetranspose.name]							
				if temp==None:
						temp=notetranspose
				else:
						tempNumber=LetterToNumber[temp.name]
				
						transitionFrequencyMatrix[tempNumber][noteNumber]= (transitionFrequencyMatrix[tempNumber][noteNumber] +1)
				
						temp=notetranspose
           
        
rowsArraySum=transitionFrequencyMatrix.sum(axis=1, dtype= 'int')     #ritorna un array contenente la somma degli elementi della matrice raggruppati per riga o per colonna
                                                                     #axis=0 indica la somma di tutte le colonne, axis=1 indica la somma di tutte le righe 
                
#creazione della matrice delle probabilità    
for row in range(12):
	for column in range(12):
		transitionProbabilityMatrix[row][column]= transitionFrequencyMatrix[row][column]/rowsArraySum[row]      

print(transitionProbabilityMatrix)
'''
#test per valutare il lavoro svolto 
rowsArraySumprobability= transitionProbabilityMatrix.sum(axis=1)
print(rowsArraySumprobability) #deve tornare un array contetente solo numeri uno 



#Prima implementazione di generazione di melodie utilizzando un pattern ritmico fisso 

#creao una lista di durate delle note che si riperà in modo cicliclo
noteTypeDurations=['half','quarter','quarter','half','quarter','quarter','eighth','eighth','half','eighth','eighth','half','half','quarter','quarter','half','quarter','quarter','eighth','eighth','half','eighth','eighth','half','eighth','eighth','eighth','eighth','half','half','whole']

#potrei fare tanti tipi di noteTypeDuractions e sceglierlo in modo randomico
newStream= stream.Stream() # il tempo 4/4 è impostato di default per gli oggetti Stream

startingNoteNumber=3
startingNote= NumberToLetter[startingNoteNumber]
newStream.append(note.Note(startingNote,type=noteTypeDurations[0]))

for noteIndex in range(1, 60):
        
	randomNumber= random.random() #restiuisce un intero compreso tra zero e uno
	
	probabilityMatrixRow=transitionProbabilityMatrix[startingNoteNumber] 
	
	
	temp=0 #variabile temporanea pe permettermi la scelta della nota successiva
	for index in range(12):
		
		temp= temp+probabilityMatrixRow[index]
		if randomNumber<= temp:
			duration = noteTypeDurations[noteIndex % len(noteTypeDurations)] 	
			nextNoteLetter= NumberToLetter[index]
			nextNote= note.Note(nextNoteLetter, type= duration)
		
			newStream.append(nextNote) #aggiungo la nota trovata allo spartito
			startingNote=nextNoteLetter                #inizializzo la nuova nota di partenza 
			startingNoteNumber=LetterToNumber[startingNote] #ricavo il suo numero 
			break


#definizione della funzione per ottenere una nota ad un certo intervallo 
def calcHarmony(note, harmonyType):
	harmonyTypes = {'terzaMinore': 3, 'terzaMaggiore': 4, 'quinta': 7, 'ottava': 12 }
	noteNumber = LetterToNumber[note]
	harmonyNumber = noteNumber + harmonyTypes[harmonyType]
	if (harmonyType is 'ottava'):
		harmonyNote = letter5[NumberToLetter[harmonyNumber % len(letter5)]]
	else:
		harmonyNote = NumberToLetter[harmonyNumber % len(letter5)]
	return harmonyNote

newStream.show()
'''





