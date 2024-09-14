class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1:
            print("Такого этажа не существует")
        elif new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)




house_1 = House('Ленина_1', 9)
house_2 = House('Ленина_2', 17)
house_1.go_to(12)
house_2.go_to(12)


