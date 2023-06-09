package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
    "github.com/gofiber/fiber/v2"
)

func AddCategorie(c *fiber.Ctx) error {
	categorie:= new(entities.Categorie)
	if err := c.BodyParser(categorie); err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Create(&categorie)
	return c.Status(201).JSON(categorie)
}

func GetCategories(c *fiber.Ctx) error {
	var categories []entities.Categorie

	configs.Database.Find(&categories)
	return c.Status(200).JSON(categories)
}

func GetCategorie(c *fiber.Ctx) error {
	id:=c.Params("id")
	var categorie entities.Categorie

	result:= configs.Database.Find(&categorie,id)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&categorie)
}
/* 
func UpdateCategorie(c *fiber.Ctx) {
	categorie:=new(entities.Categorie)
	id:=c.Params("id")

	if err :=c.BodyParser(categorie);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("id=?",id).Updates(&categorie)
	return c.Status(200).JSON(categorie)
} */