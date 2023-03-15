package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
    "github.com/gofiber/fiber/v2"
)

func AddNiveau(c *fiber.Ctx) error {
	niveau:= new(entities.Niveau)
	if err := c.BodyParser(niveau); err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Create(&niveau)
	return c.Status(201).JSON(niveau)
}

func GetNiveaus(c *fiber.Ctx) error {
	var niveaus []entities.Niveau

	configs.Database.Find(&niveaus)
	return c.Status(200).JSON(niveaus)
}

func GetNiveau(c *fiber.Ctx) error {
	num:=c.Params("num")
	var niveau entities.Niveau

	result:= configs.Database.Find(&niveau,num)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&niveau)
}
/* 
func UpdateNiveau(c *fiber.Ctx) {
	niveau:=new(entities.Niveau)
	num:=c.Params("num")

	if err :=c.BodyParser(niveau);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("num=?",num).Updates(&niveau)
	return c.Status(200).JSON(niveau)
} */