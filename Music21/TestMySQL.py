import mysql.connector
import glob
#instauro las connessione con il mio database MySQL impostando come database specifico "mydatabase"
mydb = mysql.connector.connect(
  host="localhost",
  user="Davide",
  passwd="football170596",
  database="nottingham"
)
mycursor = mydb.cursor()


#creo un database

mycursor.execute("CREATE DATABASE mydatabase")

#ritorna la lista dei miei database di sistema
mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
    
#creo una tabella con id come chiave primaria impostata come un intero che viene sempre incrementato
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE  customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), adress VARCHAR(255))")

#controllo se la tabella esiste
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#aggiungo una chiave primaria ad una tabella già esistente con la parola chiave ALTER TABLE
mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#per inserire un elemento nella tabella usa la chiave primaria INSERT INTO 
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, adress) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()  #utilizziamo commit() per applicare il cambiamento alla tabella

print(mycursor.rowcount, "record inserted.")



#inserisci più righe alla volta col metodo executemany() che riceve come secondo parametro una lista di tuple 

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, adress) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


#inserisco una riga e ne ritorno l'ID
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, adress) VALUES (%s, %s)"
val = ("Michella", "Blue Village resort")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid) #stampo il lastrowid

#utilizza la parola chiave SELECT per selezionare delle tuple ed il metodo fetchall() pe recupererla tutte 



mycursor.execute("SELECT * FROM corpus")

myresult = mycursor.fetchall() #Usiamo il metodo fetchall(), che recupera tutte le righe dall'ultima istruzione eseguita.

for x in myresult:
  print(x)

#selezioniamo dalla tabella solo le due colonne dei nomi e degli indirizzi
mycursor.execute("SELECT name, adress FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)   


#utilizzando il metodo fetchone() mi ritornerà la prima riga del risultato 

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
'''
print(glob.glob("C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/nottingham-dataset-master/*.abc"))