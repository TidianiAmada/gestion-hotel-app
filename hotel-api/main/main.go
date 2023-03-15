package main

import (
    "log"

    "hotel-api/configs"
    "hotel-api/handlers"
    "github.com/gofiber/fiber/v2"
)

func main() {
	app:=fiber.New()

	configs.Connect()

	
	app.Get("/hotelinfos",handlers.GetHotelInfos)
	app.Get("/hotelinfos/:num",handlers.GetHotelInfo)
	app.Post("/hotelinfos",handlers.AddHotelInfo)
	//app.Put("/hotelinfos",handlers.UpdateHotelInfo)

	app.Get("/chambres",handlers.GetChambres)
	app.Get("/chambres/:num",handlers.GetChambre)
	app.Post("/chambres",handlers.AddChambre)
	//app.Put("/chambres",handlers.UpdateChambre)
	
	app.Get("/categories",handlers.GetCategories)
	app.Get("/categories/:num",handlers.GetCategorie)
	app.Post("/categories",handlers.AddCategorie)
	//app.Put("/categories",handlers.UpdateCategorie)

	
	app.Get("/clients",handlers.GetClients)
	app.Get("/clients/:num",handlers.GetClient)
	app.Post("/clients",handlers.AddClient)
	//app.Put("/clients",handlers.UpdateClient)

	
	app.Get("/reservations",handlers.GetReservations)
	app.Get("/reservations/:num",handlers.GetReservation)
	app.Post("/reservations",handlers.AddReservation)
	//app.Put("/reservations",handlers.UpdateReservation)


	//TODO: Add endpoints for other APIs and required logic
	log.Fatal(app.Listen(":3000"))
}