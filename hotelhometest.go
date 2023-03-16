package main

import "fmt"

type Hotel struct {
	chambre map[int]string
}

func NewHotel() *Hotel {
	return &Hotel{chambre: make(map[int]string)}
}

func (h *Hotel) ReserveRoom(id int) error {
	if _, exists := h.chambre[id]; exists {
		return fmt.Errorf("La chambre  %d est deja reservee", id)
	}
	h.chambre[id] = "reservee"
	return nil
}

func (h *Hotel) OccupyRoom(id int) error {
	if _, exists := h.chambre[id]; !exists {
		return fmt.Errorf("La chambre %d n est pas reservee", id)
	}
	if h.chambre[id] == "occupee" {
		return fmt.Errorf("La chambre %d est deja occupee", id)
	}
	h.chambre[id] = "occupee"
	return nil
}

func (h *Hotel) FreeRoom(id int) error {
	if _, exists := h.chambre[id]; !exists {
		return fmt.Errorf("La chambre %d n est pas reservee", id)
	}
	h.chambre[id] = "libre"
	return nil
}

func (h *Hotel) GetRoomStatus(id int) (string, error) {
	if _, exists := h.chambre[id]; !exists {
		return "", fmt.Errorf("La chambre %d n esxiste pas", id)
	}
	return h.chambre[id], nil
}

func main() {
	hotel := NewHotel()
	hotel.ReserveRoom(101)
	hotel.OccupyRoom(101)

	status, err := hotel.GetRoomStatus(101)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("la chambre  101 est %s\n", status)
	}
}
