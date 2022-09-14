import mysql.connector

#instauro la connessione con il mio database MySQL 
mydb = mysql.connector.connect(
  host="localhost",
  user="Davide",
  passwd="football170596",
)

mycursor = mydb.cursor()

#creo un database
mycursor.execute("CREATE DATABASE nottingham")

#accedo al database appena creato 
mydb = mysql.connector.connect(
  host="localhost",
  user="Davide",
  passwd="football170596",
  database="nottingham")

#mycursor = mydb.cursor()


#creo la tabella corpus
# imposto come chiave primaria un intero che si auto icrementa ad ogni record inserito
mycursor.execute("CREATE TABLE  corpus (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), k VARCHAR(255), meter VARCHAR(255),originalId INT, originalFileName VARCHAR(255)) ")


mycursor.execute("SELECT * FROM corpus")

myresult = mycursor.fetchall() #Usiamo il metodo fetchall() per recupera tutte i record dell'istruzione di selezione.

for x in myresult:
  print(x)
'''
sql = "DROP TABLE corpus"

mycursor.execute(sql)

mydb.commit()
'''

