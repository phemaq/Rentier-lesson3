#Конвертация значений
print(
    """
 Рантье
Программа подсчитывает ваши ежемесячные расходы. Эту статистику нужнознать затем,
чтобы у вас не кончились деньги и вам не пришлось искать работу.

Введите суммы расходов по всем статьям, перечиеслеяемым ниже. Вы богаты - так не мелочитесь,
пишите суммы в долларах, без центов.
    """
)

car = input("Техническое обслуживание машины 'Тесла Родстер': ")
car = int(car)
rent = int(input("Снятие квартиры в Москве: "))
gifts = int(input("Подарки: "))
food = int(input("Еда в ресторанах: "))
staff = int(input("Прислуга: "))
teacher = int(input("Учитель: "))
donate = int(input("Донат в видеоигры: "))
total = car + rent + gifts + food + staff + teacher + donate
print("\nОбщая сумма:", total)
input("\n\nНажмите Entere, чтобы выйти из программы 'Рантье'.")
