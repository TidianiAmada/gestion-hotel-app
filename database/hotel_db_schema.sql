
DROP DATABASE IF EXISTS hoteldb;
CREATE DATABASE hoteldb;
USE hoteldb;
DROP TABLE IF EXISTS HotelInfo;
CREATE TABLE HotelInfo(
        id   int  Auto_increment,
        nom     Varchar (30),
        nbre_niv     Integer,
        nbre_chambre     Integer,
        adresse     Varchar (50),
        tel     Varchar (30),
        PRIMARY KEY (id)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS Client;
CREATE TABLE Client(
        id  int   Auto_increment,
        tel     Varchar (20),
        nom     Varchar (20),
        prenom     Varchar (20),
        PRIMARY KEY (id)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS Chambre;
CREATE TABLE Chambre(
        num     Varchar (5),
        niveau     Varchar (25),
        classe     Char (1),
        etat     Char (1),
        num_niveau_Niveau     Integer,
        PRIMARY KEY (num)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS Stats;
CREATE TABLE Stats(
        id   int  Auto_increment,
        nclasse_e     Integer,
        nclasse_s     Integer,
        nclasse_a     Integer,
        mclasse_e     Double,
        mclasse_s     Double,
        mclasse_a     Double,
        nbar     Integer,
        ntel     Integer,
        npti_dej     Integer,
        mbar     Double,
        mtel     Double,
        mpti_dej     Double,
        mchambre     Double,
        PRIMARY KEY (id)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS SER_annexes;
CREATE TABLE SER_annexes(
        nom     Varchar (30),
        tarif     Double,
        PRIMARY KEY (nom)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS Reservation;
CREATE TABLE Reservation(
        id     Integer auto_increment,
        nuite     Integer,
        classe char(1),
        numChambre varchar(5),
        tarif_spe     Bool,
        pti_dej     Bool,
        phone     Bool,
        bar     Bool,
        tarif_chambre     Double,
        tarif_pti_dej     Double,
        tarif_phone     Double,
        tarif_bar     Double,
        total     Double,
        dateReservation Date,
        dateEntree     Date,
        dateSortie     Date,
        id_Client   int,
        PRIMARY KEY (id)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS Facture;
CREATE TABLE Facture(
        num_facture  int   Auto_increment,
        nuite     Integer,
        tarif_chambre     Double,
        tarif_pti_dej     Double,
        tarif_phone     double,
        tarif_bar     Double,
        total     Double,
        nom_SER_annexes     Varchar (30),
        PRIMARY KEY (num_facture)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS Categorie;
CREATE TABLE Categorie(
        id  int   Auto_increment,
        classe     Varchar (20),
        tarif_normal     Double,
        tarif_special     Double,
        num_Chambre     Varchar (5),
        PRIMARY KEY (id)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS Niveau;
CREATE TABLE Niveau(
        num_niveau     Integer,
        nbr_chambres     Integer,
        id_HotelInfo  int  ,
        PRIMARY KEY (num_niveau)
)ENGINE=InnoDB;



DROP TABLE IF EXISTS Facture_Reservation;
CREATE TABLE Facture_Reservation(
        num_Chambre     Varchar (5),
        num_facture_Facture  int  ,
        id_Reservation     Integer,
        PRIMARY KEY (num_Chambre,num_facture_Facture,id_Reservation)
)ENGINE=InnoDB;



ALTER TABLE Chambre ADD CONSTRAINT FK_Chambre_num_niveau_Niveau FOREIGN KEY (num_niveau_Niveau) REFERENCES Niveau(num_niveau);
ALTER TABLE Reservation ADD CONSTRAINT FK_Reservation_id_Client FOREIGN KEY (id_Client) REFERENCES Client(id);
ALTER TABLE Facture ADD CONSTRAINT FK_Facture_nom_SER_annexes FOREIGN KEY (nom_SER_annexes) REFERENCES SER_annexes(nom);
ALTER TABLE Niveau ADD CONSTRAINT FK_Niveau_id_HotelInfo FOREIGN KEY (id_HotelInfo) REFERENCES HotelInfo(id);
ALTER TABLE Facture_Reservation ADD CONSTRAINT FK_Facture_Reservation_num_Chambre FOREIGN KEY (num_Chambre) REFERENCES Chambre(num);
ALTER TABLE Facture_Reservation ADD CONSTRAINT FK_Facture_Reservation_num_facture_Facture FOREIGN KEY (num_facture_Facture) REFERENCES Facture(num_facture);
ALTER TABLE Facture_Reservation ADD CONSTRAINT FK_Facture_Reservation_id_Reservation FOREIGN KEY (id_Reservation) REFERENCES Reservation(id);
