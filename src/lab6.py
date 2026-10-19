
from calculator import (
    add, subtract, multiply, divide,
    power, root, percentage
)
from colorama import Fore, init

init(autoreset=True)


def main():

    while True:
        print(Fore.CYAN + "\n=== КАЛЬКУЛЯТОР ===")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Піднесення до степеня")
        print("6. Квадратний корінь")
        print("7. Відсоток від числа")
        print("0. Вихід")

        choice = input("Оберіть операцію: ")

        if choice == "0":
            print("Завершення програми")
            break

        if choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print(Fore.RED + "Невірний вибір!")
            continue

        try:
            a = float(input("Введіть перше число: "))

            if choice != "6":
                b = float(input("Введіть друге число: "))

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            elif choice == "5":
                result = power(a, b)
            elif choice == "6":
                result = root(a)
            else:
                result = percentage(a, b)

            print(Fore.GREEN + f"Результат: {result}")

        except (ValueError, OverflowError) as error:
            print(Fore.RED + f"Помилка: {error}")


if __name__ == "__main__":
    main()
