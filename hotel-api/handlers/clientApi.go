package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
    "github.com/gofiber/fiber/v2"
)

func AddClient(c *fiber.Ctx) error {
	client:= new(entities.Client)
	if err := c.BodyParser(client); err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Create(&client)
	return c.Status(201).JSON(client)
}

func GetClients(c *fiber.Ctx) error {
	var clients []entities.Client

	configs.Database.Find(&clients)
	return c.Status(200).JSON(clients)
}

func GetClient(c *fiber.Ctx) error {
	num:=c.Params("num")
	var client entities.Client

	result:= configs.Database.Find(&client,num)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&client)
}
/* 
func UpdateClient(c *fiber.Ctx) {
	client:=new(entities.Client)
	num:=c.Params("num")

	if err :=c.BodyParser(client);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("num=?",num).Updates(&client)
	return c.Status(200).JSON(client)
} */