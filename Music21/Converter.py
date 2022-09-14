from music21 import *
c = converter.Converter()
c.regularizeFormat('abc')
#for sc in c.defaultSubconverters():
    # print(sc)

'''
Utilizzo la funzione 'parse' del modulo converter per convertire i file ABC in oggetti di music21, poi testo la traduzione utilizzando il metedo .show()
che come impostato in precedenza con il modulo enviroment.UserSetting() apre il programma MuseScore e mostra gli spartiti tradotti
'''
abcPath1= "C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/nottingham-dataset-master/ABC_cleaned/ashover.abc"
#importing of ABC files from a URL to a Stream
#s = converter.parse(abcPath1)
#class abcFormat.ABCFile(abcPath1)
#per capire di che tipologia è un oggetto utilizza il metodo type('nome oggetto') e stampalo con print()= print(type('nomeoggetto'))
#s.write('musicxml', fp='output_filename.xml')
#Returns all values (as strings) stored in this metadata as a sorted list of tuples.


abcPath1= "C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/nottingham-dataset-master/ABC_cleaned/ashover.abc"
opus= converter.parse(abcPath1)

for el in opus.scores:
    el.show()
    metro= el.recurse().getElementsByClass(meter.TimeSignature)[0] #estraggo il metro del brano 
    k = el.analyze('key')# ottengo la tonalità del componimento
    title= el.metadata.title #ottengo il titolo
    internalId= el.metadata.number# ottengo l'internalId

    #el.write(fp=el.metadata.title)
    #print(el.metadata.title)
    
'''
#a= s.TimeSignature()
a= s.recurse().getElementsByClass(meter.TimeSignature)[0] #estraggo la metrica del brano 
#a= s.getTimeSignatures()
m= s.metadata.title#ottengo il titolo del componimento 
md= metadata.Metadata() #definisco un oggetto metadata
md= s.metadata.all()

md.append(k)# la aggiungo alla lista dei metadati 
md.append(a)
print(md) #stampa  una lista di metadati trovati nel componimento con c.metadata.all()
'''
''' 
#s.show()
#s.write()
'''































'''
localCorpus = corpus.corpora.LocalCorpus()
localCorpus.addPath('C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/Music21/musicxmlfile/ashover.xml')
localCorpus.directoryPaths
#Currently, after adding paths to a corpus, you’ll need to rebuild the cache.
corpus.cacheMetadata()


#Creazione di un corpus locale chiamato newCorpus 
aNewLocalCorpus = corpus.corpora.LocalCorpus('newCorpus')
aNewLocalCorpus.addPath('C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/Music21/musicxmlfile/ashover.xml')
# A metadata bundle is a collection of metadata pulled from an arbitrarily large group of different scores. 

otherLocalBundle = corpus.corpora.LocalCorpus('newCorpus').metadataBundle
otherLocalBundle.read()
'''