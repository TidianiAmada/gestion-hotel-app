package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
    "github.com/gofiber/fiber/v2"
)


func GetFactures(c *fiber.Ctx) error {
	var factures []entities.Facture

	configs.Database.Find(&factures)
	return c.Status(200).JSON(factures)
}

func GetFacture(c *fiber.Ctx) error {
	num:=c.Params("num")
	var facture entities.Facture

	result:= configs.Database.Find(&facture,num)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&facture)
}
/* 
func UpdateFacture(c *fiber.Ctx) {
	facture:=new(entities.Facture)
	num:=c.Params("num")

	if err :=c.BodyParser(facture);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("num=?",num).Updates(&facture)
	return c.Status(200).JSON(facture)
} */