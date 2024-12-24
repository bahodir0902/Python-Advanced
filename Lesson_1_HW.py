class Foods:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_num_of_foods(self) -> int:
        return len(self.__dict__.values())


    def get_food_by_id(self, id: int) -> dict:
        try:
            if id > self.get_num_of_foods() or id < 0:
                raise ValueError(f"Foods range is in range 1-{self.get_num_of_foods()}")
            for i, (key, value) in enumerate(self.__dict__.items(), 1):
                if i == id:
                    return {key: value}
        except ValueError as e:
            print(f"Fatal error! {e}")


    def get_foods(self) -> str:
        return '\n'.join(f"{i}. {key}: {value} " for i, (key, value) in enumerate(self.__dict__.items() , 1))


# print(foods.get_foods())

class Main_Menu():
    def __init__(self, *args):
        menu = ["Display menu", "Take order", "Calculate total", "Apply discount", "Delete orders", "Exit"]
        for i, item in enumerate(args, 1):
            setattr(self, item, i)

    def get_num_of_choices(self) -> int:
        return len(self.__dict__.values())

    def display(self):
        print()
        for key, value in self.__dict__.items():
            print(f"{value} - {key}")


class Promocodes:
    def __init__(self, **kwargs):
        n = len(kwargs.keys())
        try:
            if n > 8 or n < 0:
                raise ValueError("It is not allowed to use more than 8 promocodes!")
            for i, (key, value) in enumerate(kwargs.items(), 1):
                setattr(self, key, value)
        except ValueError as e:
            print(f"Error! {e}")

    def apply_discount(self, foods: Foods, orders):
        try:
            if not orders:
                raise ValueError("Siz hech narsa buyutrma bermadingiz!")
        except ValueError as e:
            print(f"Xatolik! {e}")
            return
        while True:
            client_answer = input(f"chegirma olish uchun promokod kiriting: ")
            if client_answer in self.__dict__:
                print(f"{self.__dict__[client_answer]} lik chegirma qo\'llanildi.")
                Orders.calculate_total(orders, foods, orders, discount=True)
                break
            else:
                a = input(f"'{client_answer}' chegirmasi mavjud emas! Iltimos boshqatdan urinib koring. (ha/yoq): ")
                if a.lower() == "ha":
                    continue
                else:
                    break


class Orders:
    def __init__(self, foods: Foods):
        self.num_of_foods = foods.get_num_of_foods()
        self.orders = []

    def add_order(self, foods: Foods) -> list[int]:
        temp = True
        while temp:
            try:
                choice = int(input("Qaysi ovqatni buyurtma qilasiz? "))
                if not (0 < choice < self.num_of_foods + 1):
                    raise ValueError(f"Son 1 dan {self.num_of_foods} gacha bo\'lishi kerak!")
                self.orders.append(choice)
                while True:
                    extra = input("Yana biror nima buyutrma qilasizmi? (ha/yoq) ")
                    if extra.lower() == "ha":
                        break
                    else:
                        temp = False
                        break
            except (ValueError, TypeError) as e:
                print(f"Xatolik! {e}")
        return self.orders


    def calculate_total(self, foods: Foods, orders, discount=False):
        try:
            if not orders:
                raise ValueError("Siz hech narsa buyurtma bermadingiz!")
        except ValueError as e:
            print(f"Xatolik! {e}")
            return
        sum = 0
        print("Sizning buyurtmalaringiz: ")
        for i in orders:
            food = foods.get_food_by_id(i)
            sum += list(food.values())[0]
            print(
                f"- {list(food.keys())[0]} - {list(food.values())[0] if not discount else list(food.values())[0] * 0.7}")
        if not discount:
            print(f"Umumiy summa: {sum}")
        else:
            print(f"Umumiy summa: {sum * 0.7}")

    def clear(self) -> None:
        self.orders.clear()


def main():
    current_orders = []
    foods = Foods(Osh=25000, Manti=15000, Lagmon=20000, Shashlik=10000)
    menu = Main_Menu("Display menu", "Take order", "Calculate total", "Apply discount", "Delete orders", "Exit")
    promos = Promocodes(TEZ3=10, QWERTY20=20, UZ24=30)
    orders = Orders(foods)

    while True:
        menu.display()
        while True:
            try:
                main_choice = int(input("Qaysi funksiyadan foyadalanas? "))
                if not (0 < main_choice < menu.get_num_of_choices()):
                    raise ValueError(f"Son 1 dan {menu.get_num_of_choices()} gacha bo\'lishi kerak!")
                break
            except (ValueError, TypeError) as e:
                print(f"Xatolik! {e}")

        if main_choice == 1:
            print(foods.get_foods())

        elif main_choice == 2:
            current_orders = orders.add_order(foods)

        elif main_choice == 3:
            orders.calculate_total(foods, current_orders)

        elif main_choice == 4:
            promos.apply_discount(foods, current_orders)

        elif main_choice == 5:
            orders.clear()
            current_orders.clear()

        elif main_choice == 6:
            break

        else:
            continue
    print("Xizmatimizdan foydalanganiz uchun rahmat!")

main()
