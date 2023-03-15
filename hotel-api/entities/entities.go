package entities

import (
	"gorm.io/gorm"
	"time"
)

type HotelInfo struct {
	gorm.Model
	Id  	int `json:"id" gorm:"primary_key;auto_increment;"`
	Nom		string `json:"nom"`
	Nbreniveau		int `json:"nbreniveau"`
	Adresse		string `json:"adresse"`
	Telephone 	string `json:"telephone"`
}
type Niveau struct {
	gorm.Model
	Id	int `json:"id" gorm:"primary_key;auto_increment;"`
	Numero  string `json:"numero"`
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
	Tel		string `json:"tel"`
	Nom		string `json:"nom"`
	Prenom 	string `json:"prenom"`
}

type Reservation struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"` 
	Nuite	int `json:"nuite"`
	Numerochambre string `json:"numerochambre"`
	Petitdej bool `json:"petitdej"`
	Dateentree  time.Time `json:"dateentree"`
	Datesortie time.Time `json:"datesortie"`
}
type Categorie struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"` 
	Classe		string `json:"classe"`
	Tarifnormal int `json:"tarifnormal"`
	Tarifspecial int `json:"tarifspecial"`
}
type ServiceAnnexe struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"`
	Nom		string `json:"nom"`
	Tarif int `json:"tarif"`
}

type Facture struct {
	gorm.Model
	Id 		int `json:"id" gorm:"primary_key;auto_increment;"`
	Nuite	int `json:"nuite"` //Get from Reservation
	Tarifptitdej int `json:"tarifptitdej"`
	Total int `json:"total"`
}
