package configs

import (
    "gorm.io/driver/mysql"
    "gorm.io/gorm"
	"hotel-api/entities"
)


var Database *gorm.DB
// Connect to local Mysql server
var DATABASE_URI string ="root:passer123@tcp(localhost:3306)/gestionhoteldb?charset=utf8mb4&parseTime=True&loc=Local"
// Connect to proxySQL container
//var DATABASE_URI string="radmin:radmin@tcp(localhost:6032)/hoteldb?charset=utf8mb4&parseTime=True&loc=Local"
func Connect() error {
	var err error

	Database, err=gorm.Open(mysql.Open(DATABASE_URI),
				&gorm.Config{
					SkipDefaultTransaction: true,
					PrepareStmt: true,
					})
	if err != nil {
		panic(err)
	}
	//Database.Exec("CREATE DATABASE IF NOT EXISTS gestionhoteldb")
	Database.AutoMigrate(&entities.Chambre{},
		&entities.HotelInfo{},
		&entities.Niveau{},
		&entities.Client{},
		&entities.Categorie{},
		&entities.ServiceAnnexe{},
		&entities.Reservation{},
		&entities.Facture{})

	return nil
}
