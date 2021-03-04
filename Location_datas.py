# -*- coding:UTF-8 *-
import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "Rachid",
    password = "simplon59",
    database = "locations"
)

print(mydb)

mycursor = mydb.cursor()


""" AJOUT DES TABLES """

mycursor.execute("CREATE TABLE IF NOT EXISTS Logement (logement_id INT UNSIGNED NOT NULL AUTO_INCREMENT, type VARCHAR(20), address VARCHAR(70) NOT NULL, size SMALLINT NOT NULL, quartier VARCHAR(30), prix_specifique INT UNSIGNED NOT NULL, loyer_total INT NOT NULL, PRIMARY KEY (logement_id))")

mycursor.execute("CREATE TABLE IF NOT EXISTS City (city_id INT UNSIGNED NOT NULL AUTO_INCREMENT, city_name VARCHAR(30) NOT NULL, city_postcode CHAR(5), inhabitants_number INT UNSIGNED, distance_agence SMALLINT UNSIGNED, PRIMARY KEY (city_id))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Civilite(civilite VARCHAR(8) NOT NULL, sexe CHAR(1) NOT NULL, PRIMARY KEY (civilite))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Client (client_id INT UNSIGNED NOT NULL AUTO_INCREMENT, civilite VARCHAR(8) NOT NULL, nom VARCHAR(40) NOT NULL, prenom VARCHAR(40) NOT NULL, date_of_birth DATE NOT NULL, address VARCHAR(80) NOT NULL, ville VARCHAR(30) NOT NULL, nombre_contrats TINYINT UNSIGNED NOT NULL, PRIMARY KEY (client_id))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Type (type VARCHAR(20) NOT NULL, base_loyer INT NOT NULL, PRIMARY KEY (type))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Telephone (telephone VARCHAR(10) NOT NULL, client_id INT UNSIGNED NOT NULL, CONSTRAINT fk_client_id FOREIGN KEY (client_id) REFERENCES Client(client_id))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Contrat (contrat_id INT UNSIGNED NOT NULL, debut_contrat DATE NOT NULL, fin_contrat DATE, logement_id INT UNSIGNED NOT NULL, client_id INT UNSIGNED NOT NULL, CONSTRAINT fk_logement_id FOREIGN KEY (logement_id) REFERENCES Logement(logement_id), CONSTRAINT fk_client_id2 FOREIGN KEY (client_id) REFERENCES Client(client_id))")

""" AJOUT DE CLÉS ETRANGÈRES """


#mycursor.execute("ALTER TABLE Logement ADD CONSTRAINT fk_type FOREIGN KEY (type) REFERENCES Type(type)")

#mycursor.execute("ALTER TABLE Client ADD CONSTRAINT fk_civilite FOREIGN KEY (civilite) REFERENCES Civilite(civilite)")

#mycursor.execute("ALTER TABLE Logement ADD COLUMN city_id INT UNSIGNED NOT NULL AFTER logement_id")

#mycursor.execute("ALTER TABLE Logement ADD CONSTRAINT fk_city_id FOREIGN KEY (city_id) REFERENCES City(city_id)")


""" AJOUT DE TUPLES """

#sql = "INSERT INTO City(city_name, city_postCode, inhabitants_number, distance_agence) VALUES(%s, %s, %s, %s)"
#val = [('Lille', '59100', 100000, 15), 
#       ('Wasquehal', '59700', 20000,10),
#       ('Croix', '59170', 21000,11),
#       ('Wattrelos', '59150', 40000,17),
#       ('Tourcoing', '59200', 97000,16)
# ]


""" MODIFICATION D'UN TUPLE """

# sql_modif = "UPDATE City SET city_name = 'Roubaix' WHERE city_postcode = '59100'"
# mycursor.execute(sql_modif)
# mydb.commit()


""" AJOUT DE TUPLES """

# sql = "INSERT INTO Type(type, base_loyer) VALUES(%s, %s)"
# val = [('T2', 200), 
#       ('T4', 275), 
#       ('T3', 400), 
#       ('T1', 500), 
#       ('T5', 600)
# ]


""" MODIFICATION DE TUPLES """

# sql_modif = "UPDATE Type SET base_loyer = 200 WHERE type = 'T2'"
# mycursor.execute(sql_modif)
# mydb.commit()

# sql_modif = "UPDATE Type SET base_loyer = 175 WHERE type = 'T1'"
# mycursor.execute(sql_modif)
# mydb.commit()

# sql_modif = "UPDATE Type SET base_loyer = 500 WHERE type = 'T4'"
# mycursor.execute(sql_modif)
# mydb.commit()


""" AJOUT DE TUPLES """

# sql = "INSERT INTO Logement(city_id, type, address, size, quartier, prix_specifique, loyer_total) VALUES(%s, %s, %s, %s, %s, %s, %s)"
# val = [(6, 'T2', '18, rue de Paris', 45, "Lille-Centre", 320, 370), 
#       (7, 'T4', '57, rue des Impôts', 80, "Hôtel de Ville", 510, 550), 
#       (8, 'T3', '5, rue des Postes', 60, "Mairie", 320, 370), 
#       (9, 'T1', '98, rue de Herseaux', 25, "Beaulieu", 220, 260), 
#       (10, 'T5', '140, rue de la Lys', 100, "Colbert", 600, 700)
# ]


""" MODIFICATION D'UN TUPLE """

# sql_modif = "UPDATE Logement SET quartier = 'Saint-Maurice' WHERE type = 'T2'"
# mycursor.execute(sql_modif)
# mydb.commit()


""" AJOUT DE TUPLES """

# sql = "INSERT INTO Civilite(civilite, sexe) VALUES(%s, %s)"
# val = [('Monsieur', 'M'), 
#       ('Madame', 'F'), 
# ]


""" MODIFICATION DE TUPLES """

# sql_modif = "UPDATE Civilite SET sexe = 'm' WHERE civilite = 'Monsieur'"
# mycursor.execute(sql_modif)
# mydb.commit()

# sql_modif = "UPDATE Civilite SET sexe = 'M' WHERE civilite = 'Monsieur'"
# mycursor.execute(sql_modif)
# mydb.commit()

""" AJOUT DE TUPLES """

# sql = "INSERT INTO Client (civilite, nom, prenom, date_of_birth, address, ville, nombre_contrats) VALUES(%s, %s, %s, %s, %s, %s, %s)"
# val = [('Monsieur', 'Durand', 'Pierre', '1970-05-25', '50, rue de la Perche', 'Roubaix', 2), 
#       ('Madame', 'Dupont', 'Pierrette', '1961-08-02', '40, rue Colbert', 'Tourcoing', 1), 
#       ('Monsieur', 'Colin', 'Jean', '1975-12-06', '43, rue de Lyon', 'Croix', 3), 
#       ('Madame', 'Vasseur', 'Leïla', '1994-11-29', '54, rue du Long Pot', 'Lille', 5), 
#       ('Monsieur', 'Albert', 'Martin', '1972-06-18', '68, rue des Arts', 'Roubaix', 4)
# ]


""" MODIFICATION D'UN TUPLE """

# sql_modif = "UPDATE Client SET prenom = 'Louis' WHERE nom = 'Durand'"
# mycursor.execute(sql_modif)
# mydb.commit()


""" AJOUT DE TUPLES """

# sql = "INSERT INTO Telephone (telephone, client_id) VALUES(%s, %s)"
# val = [('0625613859', 1),
#        ('0645235453', 1),
#        ('0623115856', 1),
#        ('0695624125', 1),
#        ('0625613859', 1)
# ]


""" MODIFICATION D'UNE COLONNE """

#mycursor.execute("ALTER TABLE Contrat MODIFY COLUMN contrat_id INT UNSIGNED NOT NULL AUTO_INCREMENT")


""" MODIFICATION D'UN TUPLE """

# sql_modif = "UPDATE Telephone SET client_id = 2 WHERE telephone = '0645235453'"
# mycursor.execute(sql_modif)
# mydb.commit()


""" AJOUT DE TUPLES """

# sql = "INSERT INTO Contrat (debut_contrat, fin_contrat, logement_id, client_id) VALUES(%s, %s, %s, %s)"
# val = [('2018-09-25', '2019-06-15', 12, 2), 
#        ('2016-02-10', '2020-07-25', 14, 1), 
#        ('2014-12-06', '2019-06-15', 13, 4), 
#        ('2019-10-11', '2022-08-19', 11, 3), 
#        ('2017-04-12', '2020-06-05', 15, 5)
#  ]




""" MODIFICATION D'UN TUPLE """

# sql_modif = "UPDATE Contrat SET fin_contrat = NULL WHERE client_id = 4"
# mycursor.execute(sql_modif)
# mydb.commit()


""" SUPPRESSION D'UN TUPLE """

# sql_delete = "DELETE FROM Contrat WHERE client_id = 1"
# mycursor.execute(sql_delete)
# mydb.commit()


""" ENREGISTREMENT DES TUPLES DANS LA BASE DE DONNEES """
# mycursor.executemany(sql, val)
# mydb.commit()


""" AFFICHAGE DES DIFFERENTES TABLES """

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#    print(x)


""" AFFICHAGE D'UNE TABLE """

mycursor.execute("SELECT * FROM Contrat")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)

