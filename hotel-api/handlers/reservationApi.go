package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
    "github.com/gofiber/fiber/v2"
)

func AddReservation(c *fiber.Ctx) error {
	reservation:= new(entities.Reservation)
	if err := c.BodyParser(reservation); err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Create(&reservation)
	return c.Status(201).JSON(reservation)
}

func GetReservations(c *fiber.Ctx) error {
	var reservations []entities.Reservation

	configs.Database.Find(&reservations)
	return c.Status(200).JSON(reservations)
}

func GetReservation(c *fiber.Ctx) error {
	num:=c.Params("num")
	var reservation entities.Reservation

	result:= configs.Database.Find(&reservation,num)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&reservation)
}
/* 
func UpdateReservation(c *fiber.Ctx) {
	reservation:=new(entities.Reservation)
	num:=c.Params("num")

	if err :=c.BodyParser(reservation);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("num=?",num).Updates(&reservation)
	return c.Status(200).JSON(reservation)
} */