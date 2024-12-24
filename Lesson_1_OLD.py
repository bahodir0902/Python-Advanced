foods = {"Osh": 25_000, "Manti": 15_000, "Lag\'mon": 20_000, "Shashlik":10_000}
menu = ["Display menu", "Take order", "Calculate total", "Apply discount", "Delete orders", "Exit"]

def main_menu() -> None:
    """This function is needed for displaying main menu"""
    for i, item in enumerate(menu, 1):
        print(f"{i}. - {item}")

def take_order(orders) -> None:
    temp = True
    while temp:
        try:
            choice = int(input("Qaysi ovqatni buyurtma qilasiz? "))
            if not (0 < choice < 5):
                raise ValueError("Son 1 dan 4 gacha bo\'lishi kerak!")
            orders.append(choice)
            while True:
                extra = input("Yana biror nima buyutrma qilasizmi? (ha/yoq) ")
                if extra.lower() == "ha":
                    break
                else:
                    temp = False
                    break
        except (ValueError, TypeError) as e:
            print(f"Xatolik! {e}")

def calculate_orders(orders, discount=False) -> None:
    try:
        if not orders:
            raise ValueError("Siz hech narsa buyurtma bermadingiz!")
    except ValueError as e:
        print(f"Xatolik! {e}")
        return
    sum = 0
    print("Sizning buyurtmalaringiz: ")
    for i in orders:
        sum += list(foods.values())[i - 1]
        print(f"- {list(foods.keys())[i - 1]} - {list(foods.values())[i - 1] if not discount else list(foods.values())[i - 1] * 0.7}")
    if not discount:
        print(f"Umumiy summa: {sum}")
    else:
        print(f"Umumiy summa: {sum * 0.7}")

def apply_discount(orders) -> None:
    try:
        if not orders:
            raise ValueError("Siz hech narsa buyutrma bermadingiz!")
    except ValueError as e:
        print(f"Xatolik! {e}")
        return
    while True:
        client_answer = input(f"30% chegirma olish uchun promokod kiriting: ")
        if client_answer == "uz24":
            print(f"30% lik chegirma qo\'llanildi.")
            calculate_orders(orders, discount=True)
            break
        else:
            a = input(f"'{client_answer}' chegirmasi mavjud emas! Iltimos boshqatdan urinib koring. (ha/yoq): ")
            if a.lower() == "ha":
                continue
            else:
                break

def display_menu() -> None:
    print("Tushlik menyusiga xush kelibsiz!")
    for i, (food, price) in enumerate(foods.items(), 1):
        print(f"{i}. {food} - {price} so\'m")

def main():
    orders = []
    while True:
        main_menu()
        while True:
            try:
                main_choice = int(input("Qaysi funksiyadan foyadalanas? "))
                if not (0 < main_choice < 7):
                    raise ValueError("Son 1 dan 5 gacha bo\'lishi kerak!")
                break
            except (ValueError, TypeError) as e:
                print(f"Xatolik! {e}")

        if main_choice == 1:
            display_menu()

        elif main_choice == 2:
            take_order(orders)

        elif main_choice == 3:
            calculate_orders(orders)

        elif main_choice == 4:
            apply_discount(orders)

        elif main_choice == 5:
            orders.clear()

        elif main_choice == 6:
            break

        else:
            continue # har extimolga qarshi
    print("Xizmatimizdan foydalanganiz uchun rahmat!")

main()
