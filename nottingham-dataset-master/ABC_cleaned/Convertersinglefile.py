from music21 import *
import mysql.connector
import os
'''
Con questo script proggetto il modo per tradurre un singolo file abc in un oggetto music21 di tipo score per poi stamparlo e salvarlo
in un file musicxml dopo aver estrato i principali metadati di interesse come l'autore la tonalità e la metrica.
Nella prima parte impostiamo dei valori di configurazione per poter utilizzare Muse score come lettore del brano estratto e impostiamo 
la cartella in cui vogliamo salvare il file con il metodo .write() 

'''
'''

#Con il modulo environmen utlizzando il metodo Usersetting() posso impostare le mie preferenze creando un oggetto environment configuration
us = environment.UserSettings()

#modificando la chiave 'directoryScratch' andiamo ai impostare la path desiderata dove verranno salvati i file ottenuti dal metodo .write()
us['directoryScratch'] ='C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/Music21/musicxmlfile'
#con la chiave 'musicxmlPath' vado ad impostare MuseScore come lettore predefinito dei file xml
us['musicxmlPath']='C:/Program Files/MuseScore/bin/MuseScore3.exe'
#modificando la chiave la chiave 'musescoreDirectPNGPath' imposto il percorso in cui trovare Musescore nel mio conputer
us['musescoreDirectPNGPath'] = 'C:/Program Files/MuseScore/bin/MuseScore3.exe'
#seleziona solo un brano dalla mio corpus di brani e lo converto con il comando convert.parse('path')


comicio la codifica del brano
'''
'''
s= converter.parseFile('C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/Music21/python Script/A and As Waltz.abc', format= 'abc')

k= s.analyze('key')# ottengo la tonalità del componimento
M= s.recurse().getElementsByClass(meter.TimeSignature)[0] #estraggo la metrica del brano 

md= metadata.Metadata() #definisco un oggetto metadata
md= s.metadata.all() #ritorna una lista con tutti i metadati trovati nel brano 
md.append(k)# aggiungo la tonalità alla lista dei metadati 
md.append(M)#aggiungo la metrica del brano alla lista dei metadati 
print(type(M)) #stampa  una lista di metadati trovati nel componimento con c.metadata.all()
#s.show()# mostro lo spartito tradotto con Musescore
#s.write('musicxml', fp='myconvertedfile.xml')# Stampo lo spartito in versione .xml e lo salvo con un nome desiderato in una cartella impostata in precedenza
'''
'''
Utilizzo la funzione 'parse' del modulo converter per convertire i file ABC in oggetti di music21, poi testo la traduzione utilizzando il metedo .show()
che come impostato in precedenza con il modulo enviroment.UserSetting() apre il programma MuseScore e mostra gli spartiti tradotti
'''

#instauro la connessione con il mio database MySQL 
mydb = mysql.connector.connect(
  host="localhost",
  user="Davide",
  passwd="football170596",
)
mycursor = mydb.cursor()


#creo un database
#mycursor.execute("CREATE DATABASE nottingham")

#entro nel database appena inserito 
mydb = mysql.connector.connect(
  host="localhost",
  user="Davide",
  passwd="football170596",
  database="nottingham")

mycursor = mydb.cursor()
#creo una tabella con id come chiave primaria impostata come un intero che viene sempre incrementato ad ogni record inserito

originalPatch="C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/nottingham-dataset-master/ABC_cleaned"
#mycursor.execute("CREATE TABLE  corpus (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), k VARCHAR(255), metric VARCHAR(255))")
for x in os.listdir(originalPatch):
  files_path= os.path.abspath(x)
  for path in files_path:
    abcPath=path
    #abcPath1="C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/nottingham-dataset-master/ABC_cleaned/ashover.abc"
    #devo creare un ciclo for per scorrere tutte i file abc nella  cartella
    s= converter.parse(abcPath,format= 'musicxml')
    #essendoci in ogni file più componimenti scritti in abc la funzione di conversione ritorna un oggetto di tipo stream.opus che indica
    #un insieme di spartiti, quindi oggetti di tipo Score
    #seleziono un brano alla volta dal mio opus con il metodo .scores per ottenere ogni singolo score contenuto in esso
    for el in s.scores:
      M= el.recurse().getElementsByClass(meter.TimeSignature)[0] #estraggo la metrica del brano 
      k = el.analyze('key')# ottengo la tonalità del componimento
      md= metadata.Metadata() #definisco un oggetto metadata
      md= el.metadata.all() #ritorna una lista con tutti i metadati trovati nel brano 
      md.append(k)# aggiungo la tonalità alla lista dei metadati 
      md.append(M)#aggiungo la metrica del brano alla lista dei metadati 
      #dovrò infine inserire nella tabella del database la lista di metadati appena creata
      #per inserire un elemento nella tabella usa la chiave primaria INSERT INTO 
    
      sql = "INSERT INTO corpus (title,k,metric) VALUES (%s,%s,%s)"
      val = (el.metadata.title,k.tonicPitchNameWithCase, M.ratioString)
      mycursor.execute(sql, val)
      #con il metodo ratioString converto l'oggetto di tipo  meter.TimeSignature in una stringa 
      #con il metodo tonicPitchNameWithCase converto l'oggeto key.Key in una Stringa che sarà maiuscola se la tonalita è maggiore e minuscola se la tonalità è minore
      mydb.commit()  #utilizziamo commit() per applicare il cambiamento alla tabella  
      #el.write(fp=el.metadata.title)# Salvo la conversione del brano in musicXML in una cartella dedicata, salvato come il titolo della canzone 
      #el.show() #mostro lo spartito tradotto tramite Musescore
      #print(el.metadata.title)
  