package handlers

import (
    "hotel-api/configs"
    "hotel-api/entities"
    "github.com/gofiber/fiber/v2"
)

func AddHotelInfo(c *fiber.Ctx) error {
	hotelInfo:= new(entities.HotelInfo)
	if err := c.BodyParser(hotelInfo); err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Create(&hotelInfo)
	return c.Status(201).JSON(hotelInfo)
}

func GetHotelInfos(c *fiber.Ctx) error {
	var hotelInfos []entities.HotelInfo

	configs.Database.Find(&hotelInfos)
	return c.Status(200).JSON(hotelInfos)
}

func GetHotelInfo(c *fiber.Ctx) error {
	num:=c.Params("num")
	var hotelInfo entities.HotelInfo

	result:= configs.Database.Find(&hotelInfo,num)
	if result.RowsAffected==0 {
		return c.SendStatus(404)
	}

	return c.Status(200).JSON(&hotelInfo)
}
/* 
func UpdateHotelInfo(c *fiber.Ctx) {
	hotelInfo:=new(entities.HotelInfo)
	num:=c.Params("num")

	if err :=c.BodyParser(hotelInfo);err!=nil {
		return c.Status(503).SendString(err.Error())
	}
	configs.Database.Where("num=?",num).Updates(&hotelInfo)
	return c.Status(200).JSON(hotelInfo)
} */