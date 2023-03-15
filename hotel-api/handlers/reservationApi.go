package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
	"hotel-api/services"
    "github.com/gofiber/fiber/v2"
)


func AddReservation(c *fiber.Ctx) error {
	reservation:= new(entities.Reservation)

	if err := c.BodyParser(reservation); err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Create(&reservation)
	services.GenerateFacture(reservation)
	return c.Status(201).JSON(reservation)
}

func GetReservations(c *fiber.Ctx) error {
	var reservations []entities.Reservation

	configs.Database.Find(&reservations)
	return c.Status(200).JSON(reservations)
}

func GetReservation(c *fiber.Ctx) error {
	id:=c.Params("id")
	var reservation entities.Reservation

	result:= configs.Database.Find(&reservation,id)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&reservation)
}
/* 
func UpdateReservation(c *fiber.Ctx) {
	reservation:=new(entities.Reservation)
	id:=c.Params("id")

	if err :=c.BodyParser(reservation);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("id=?",id).Updates(&reservation)
	return c.Status(200).JSON(reservation)
} */