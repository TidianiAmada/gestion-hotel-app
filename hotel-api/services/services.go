package services

import (
    "hotel-api/configs"
    "hotel-api/entities"
)

func GenerateFacture(reservation *entities.Reservation)  {
	facture:= new(entities.Facture)
	num:=reservation.Numerochambre
	var chambre entities.Chambre
	configs.Database.Find(&chambre,num)

	var categorie entities.Categorie
	classe:=chambre.Classe
	configs.Database.Find(&categorie,classe)
	
	facture.ClientId=reservation.ClientId
	facture.Tarifchambre=categorie.Tarifnormal
	//var ServiceAnnexe entities.ServiceAnnexe check ptitdej bool
	facture.Total=facture.Tarifchambre

	facture.Nuite=reservation.Nuite
	facture.Total= facture.Nuite * facture.Total
	
	configs.Database.Create(&facture)
	
}
/* func ChambreLibreCheck() bool {
	// code
} */