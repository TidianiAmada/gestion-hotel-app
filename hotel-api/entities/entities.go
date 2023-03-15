package entities

import (
	"gorm.io/gorm"
	"time"
)

type HotelInfo struct {
	gorm.Model
	Id  	int `json:"id" gorm:"primary_key;auto_increment;"`
	Nom		string `json:"nom" gorm:"unique"`
	Nbreniveau		int `json:"nbreniveau"`
	Adresse		string `json:"adresse"`
	Telephone 	string `json:"telephone"`
}
type Niveau struct {
	gorm.Model
	Id	int `json:"id" gorm:"primary_key;auto_increment;"`
	Numero  int `json:"numero" gorm:"unique"`
	Nbreniveau int `json:"nbrniveau"`
}

type Chambre struct {
	gorm.Model
	Num 		int `json:"num" gorm:"primary_key;"` 
	Niveau		string `json:"niveau"`
	Classe		string `json:"classe"`
	Etat 	string `json:"etat"`
}

type Client struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"` 
	Tel		string `json:"tel" gorm:"unique"`
	Nom		string `json:"nom"`
	Prenom 	string `json:"prenom"`
}

type Reservation struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"` 
	ClientId int `json:"clientid"`
	Nuite	int `json:"nuite"`
	Numerochambre int `json:"numerochambre"`
	Petitdej bool `json:"petitdej"`
	Dateentree  time.Time `json:"dateentree"`
	Datesortie time.Time `json:"datesortie"`
}
type Categorie struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"` 
	Classe		string `json:"classe" gorm:"unique"`
	Tarifnormal int `json:"tarifnormal"`
	Tarifspecial int `json:"tarifspecial"`
}
type ServiceAnnexe struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"`
	Nom		string `json:"nom" gorm:"unique"`
	Tarif int `json:"tarif"`
}

type Facture struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"`
	ClientId int `json:"clientid"` 
	Nuite	int `json:"nuite"` //Get from Reservation
	Tarifchambre int `json:"tarifchambre"`
	Tarifptitdej int `json:"tarifptitdej"`
	Total int `json:"total"`
}
