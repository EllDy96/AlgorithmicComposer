from music21 import *
import mysql.connector
'''
configure.run()

us = environment.Environment()
#ciclo for che riorna tutti i valori di configurazione possibili noi ci interesseremo espressi come chiavi
# noi ci soffermeremo su 'directoryScratch' 'musicxmlPath' e 'musescoreDirectPNGPath'
for key in sorted(us.keys()):
    print(key)
'''
#Con il modulo environmen utlizzando il metodo Usersetting() posso impostare le mie preferenze creando un oggetto environment configuration

us = environment.UserSettings()

#modificando la chiave 'directoryScratch' andiamo ai impostare la path desiderata dove verranno salvati i file ottenuti dal metodo .write()
us['directoryScratch'] ='C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/Music21/musicxmlfile'
#con la chiave 'musicxmlPath' vado ad impostare MuseScore come lettore predefinito dei file xml
us['musicxmlPath']='C:/Program Files/MuseScore/bin/MuseScore3.exe'
us['musescoreDirectPNGPath'] = 'C:/Program Files/MuseScore/bin/MuseScore3.exe'
#con il metodo get('keyname') ottengo il percorso assegnato alla chiave di configurazione 'keyname'
environment.get('musicxmlPath')
#imposto il debugger 
environment.UserSettings()['debug'] = True



