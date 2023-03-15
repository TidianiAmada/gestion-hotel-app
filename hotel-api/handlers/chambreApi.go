package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
    "github.com/gofiber/fiber/v2"
)

func AddChambre(c *fiber.Ctx) error {
	chambre:= new(entities.Chambre)
	if err := c.BodyParser(chambre); err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Create(&chambre)
	return c.Status(201).JSON(chambre)
}

func GetChambres(c *fiber.Ctx) error {
	var chambres []entities.Chambre

	configs.Database.Find(&chambres)
	return c.Status(200).JSON(chambres)
}

func GetChambre(c *fiber.Ctx) error {
	num:=c.Params("num")
	var chambre entities.Chambre

	result:= configs.Database.Find(&chambre,num)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&chambre)
}
/* 
func UpdateChambre(c *fiber.Ctx) {
	chambre:=new(entities.Chambre)
	num:=c.Params("num")

	if err :=c.BodyParser(chambre);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("num=?",num).Updates(&chambre)
	return c.Status(200).JSON(chambre)
} */