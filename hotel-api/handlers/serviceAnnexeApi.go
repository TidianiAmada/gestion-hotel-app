package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
    "github.com/gofiber/fiber/v2"
)

func AddServiceAnnexe(c *fiber.Ctx) error {
	serviceAnnexe:= new(entities.ServiceAnnexe)
	if err := c.BodyParser(serviceAnnexe); err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Create(&serviceAnnexe)
	return c.Status(201).JSON(serviceAnnexe)
}

func GetServiceAnnexes(c *fiber.Ctx) error {
	var serviceAnnexes []entities.ServiceAnnexe

	configs.Database.Find(&serviceAnnexes)
	return c.Status(200).JSON(serviceAnnexes)
}

func GetServiceAnnexe(c *fiber.Ctx) error {
	num:=c.Params("num")
	var serviceAnnexe entities.ServiceAnnexe

	result:= configs.Database.Find(&serviceAnnexe,num)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&serviceAnnexe)
}
/* 
func UpdateServiceAnnexe(c *fiber.Ctx) {
	serviceAnnexe:=new(entities.ServiceAnnexe)
	num:=c.Params("num")

	if err :=c.BodyParser(serviceAnnexe);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("num=?",num).Updates(&serviceAnnexe)
	return c.Status(200).JSON(serviceAnnexe)
} */