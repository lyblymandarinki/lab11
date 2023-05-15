def z1():
    class Restaurant:

        def init(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт!")


    newRestaurant = Restaurant("Restoraunt", "Polski")

    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    print()
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z2():
    class Restaurant:
        def init(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")


    res_1 = Restaurant("Макдокнакс", "Усы лисы")
    res_2 = Restaurant("Кимчи", "Сабвей")
    res_3 = Restaurant("Бургер кинг", "Кфс")

    res_1.describe_restaurant()
    print()
    res_2.describe_restaurant()
    print()
    res_3.describe_restaurant()

def z3():
    class Restaurant:
        def init(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан открыт!")

        def old_rating(self, rating):
            self.rating = rating
            print(f"Рейтинг: {self.rating}")

        def new_rating(self, new_rat):
            self.rating = float(input('Введите новое значение рейтинга: '))
            print()
            newRestaurant = Restaurant("Restoraunt", "Polski")
            newRestaurant.describe_restaurant()
            newRestaurant.open_restaurant()
            print(f"Рейтинг обновлён: {self.rating}")

    newRestaurant = Restaurant("Restoraunt", "Polski")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
    newRestaurant.old_rating(3.5)
    print()
    newRestaurant.new_rating(3)