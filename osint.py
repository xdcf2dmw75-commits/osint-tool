print("1 - Поиск по нику")
print("2 - Поиск по номеру")
print("3 - Проверка ника на сайтах")

choice = input("Выбери: ")

if choice == "1":
    username = input("Ник: ")
    print("Google:", "https://www.google.com/search?>
    print("Telegram:", "https://t.me/" + username)
    print("GitHub:", "https://github.com/" + usernam>

elif choice == "2":
    number = input("Номер: ")
    print("Google:", "https://www.google.com/search?>
    print("WhatsApp:", "https://wa.me/" + number)

elif choice == "3":
    username = input("Ник: ")
    sites = ["https://github.com/", "https://t.me/",>
    for site in sites:
        print("Проверка:", site + username)

else:
    print("Ошибка")

