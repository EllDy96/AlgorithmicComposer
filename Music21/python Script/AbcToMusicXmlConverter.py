from music21 import *
import mysql.connector
import os





#Utlizzando il metodo Usersetting() posso impostare le mie preferenze creando un oggetto di environment configuration
us = environment.UserSettings()
#con la chiave 'musicxmlPath' vado ad impostare MuseScore come lettore predefinito dei file Musicxml
us['musicxmlPath']='C:/Program Files/MuseScore/bin/MuseScore3.exe'





'''
Utilizzo la funzione 'parse' del modulo converter per convertire i file ABC in oggetti di music21, testando la coversione con il metedo .show()
che come impostato in precedenza con il modulo enviroment.UserSetting() apre il programma MuseScore e mostra gli spartiti tradotti

'''  

#istauro una connessione con il server  specificando come database 'nottingham'
mydb = mysql.connector.connect(
  host="localhost",
  user="Davide",
  passwd="********",
  database="nottingham")

mycursor = mydb.cursor() # permette di interrogare il database

#currentDir salva il percorso della directory corrente
currentDir = os.getcwd()

#aggiunge a currentDir la cartella XML_file dove salviamo i file convertiti in Musicxml
directoryWrite = os.path.join(currentDir, 'XML_files')

abcFiles = os.listdir('./ABC_files') #lista dei nomi dei file nella directory ABC_files

for abcFile in abcFiles:

	abcFilePath = os.path.abspath(os.path.join('ABC_files', abcFile)) #ottengo il percorso assoluto di ogni file 

	opus = converter.parse(abcFilePath) #l'oggetto opus è un contenitore di numerose partiture musicali 

	for score in opus.scores:

		metro= score.recurse().getElementsByClass(meter.TimeSignature)[0] #estraggo il metro del brano 
		k = score.analyze('key')# ottengo la tonalità del componimento
		
		title= score.metadata.title #ottengo il titolo
		internalId= score.metadata.number# ottengo l'internalId

		abspath=os.path.join(directoryWrite, score.metadata.title) #aggiungendo al percorso della directoryWrite il titolo del brano

		score.write(fp=abspath)# Salvo la conversione del brano nella cartella dedicata 'XML_files' 

		score.show() #mostro lo spartito tramite Musescore  
			
		#per inserire un elemento nella tabella usa la chiave primaria INSERT INTO 
		
		sql = "INSERT INTO corpus (title,k,meter,originalId,originalFileName) VALUES (%s,%s,%s,%s,%s)"
		val = (title,k.tonicPitchNameWithCase, metro.ratioString, internalId ,abcFile)
		mycursor.execute(sql, val)
		#con il metodo ratioString converto l'oggetto di tipo  meter.TimeSignature in una stringa 
		#con il metodo tonicPitchNameWithCase converto l'oggeto key.Key in una Stringa: maiuscola se la tonalita è maggiore e minuscola se la tonalità è minore
		mydb.commit()  #utilizziamo commit() per applicare il cambiamento alla tabella  
		

    
    

mycursor.execute("SELECT * FROM corpus")

myresult = mycursor.fetchall() #Usiamo il metodo fetchall(), che recupera tutte le righe dall'ultima istruzione eseguita.

for x in myresult:
	print(x)

