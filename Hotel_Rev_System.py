package com.hotel;

public class Room {
    private int roomNumber;
    private String type;
    private boolean isAvailable;

    // Конструктор
    public Room(int roomNumber, String type, boolean isAvailable) {
        this.roomNumber = roomNumber;
        this.type = type;
        this.isAvailable = isAvailable;
    }

    // Геттеры и сеттеры
    public int getRoomNumber() {
        return roomNumber;
    }

    public void setRoomNumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void setAvailable(boolean isAvailable) {
        this.isAvailable = isAvailable;
    }

    // Дополнительные методы
    public void bookRoom() {
        if (isAvailable) {
            isAvailable = false;
            System.out.println("Номер " + roomNumber + " забронирован.");
        } else {
            System.out.println("Номер " + roomNumber + " уже забронирован.");
        }
    }
}
