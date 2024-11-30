while True:
    print("\nКто хочет стать пенсионером!")
    print("\nДобрый вечер, дорогие друзья! Я — интерпретатор Python 3.7, и это шоу \"Кто хочет стать пенсионером\" "
          "в нашей студии.")
    print(
        "\nУ вас имеется две подсказки: \"50 x 50\" и \"Право на ошибку\". Была ещё помощь зала, но какой нахрен зал? "
        "Даже в реальной игре временно нет этой подсказки из-за ковида.")
    print("Остальное ты знаешь: 4 варианта ответа, верен только один. Один неверный ответ — вылет.")
    print("Будет 10 вопросов, за которые ты можешь получить:"
          "\n1. 500 очков"
          "\n2. 1 000 очков"
          "\n3. 2 000 очков"
          "\n4. 3 000 очков"
          "\n5. 5 000 очков"
          "\n6. 10 000 очков"
          "\n7. 15 000 очков"
          "\n8. 25 000 очков"
          "\n9. 50 000 очков"
          "\n10. 100 000 очков")
    satisfactory_answer_received = False
    satisfactory_answer_list = [500, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000]

    while satisfactory_answer_received is not True:
        solid_amount = int(input("\nВыберите несгораемую сумму (без пробелов): "))
        if solid_amount not in satisfactory_answer_list:
            print("\nВыберите несгораемую сумму из предложенных выше!")
        else:
            print("\nЗашибись, приступаем!")
            satisfactory_answer_received = True

    fifty_fifty = 1
    extra_chance = 1

    game_won = False
    satisfactory_answer_list_1 = ["А", "Б", "В", "Г", "50 X 50", "50X50", "50Х50", "50 Х 50", "Право на ошибку"]
    satisfactory_answer_list_1_shorted = ["А", "Б", "В", "Г"]
    solid_amount_obtained = False

    attempt_1 = 1
    print("\nВопрос номер 1.")  # Номер вопроса
    print("Кто в Far Cry 4 должен был стать новой Тарун Матарой?")  # Сам вопрос
    print("А: Амита")  # Вариант 1
    print("Б: Бхатра")  # Вариант 2
    print("В: Ишвари")  # Вариант 3
    print("Г: Лакшмана")  # Вариант 4
    satisfactory_answer_received_1 = False
    while satisfactory_answer_received_1 is False:
        answer_1 = input("\nВыберите один вариант ответа: ")
        answer_1 = str(answer_1.upper())
        if answer_1 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_1 in satisfactory_answer_list_1:
            break
    if answer_1 == "50X50" or answer_1 == "50 X 50" or answer_1 == "50Х50" or answer_1 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nА: Амита")  # Вариант 1
            print("Б: Бхатра")  # Вариант 2
            satisfactory_answer_received_1 = False
            while satisfactory_answer_received_1 is False:
                answer_1 = input("\nВыберите один вариант ответа: ")
                answer_1 = str(answer_1.upper())
                if str(answer_1) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_1 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_received_1 = False
            while satisfactory_answer_received_1 is False:
                answer_1 = input("\nВыберите один вариант ответа: ")
                answer_1 = str(answer_1.upper())
                if answer_1 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_1 in satisfactory_answer_list_1_shorted:
                    break

    if answer_1 != "Б":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 500:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_2 = 1
    print("\nВопрос номер 2.")  # Номер вопроса
    print("Как называлась лопата с улыбкой в Far Cry 5?")  # Сам вопрос
    print("А: Лопата")  # Вариант 1
    print("Б: Позитивчик")  # Вариант 2
    print("В: Позитив")  # Вариант 3
    print("Г: Хорошее настроение")  # Вариант 4
    satisfactory_answer_received_2 = False
    while satisfactory_answer_received_2 is False:
        answer_2 = input("\nВыберите один вариант ответа: ")
        answer_2 = answer_2.upper()
        if answer_2 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_2 in satisfactory_answer_list_1:
            break
    if answer_2 == "50X50" or answer_2 == "50 X 50" or answer_2 == "50Х50" or answer_2 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nА: Лопата")  # Вариант 1
            print("В: Позитив")  # Вариант 2
            satisfactory_answer_received_2 = False
            while satisfactory_answer_received_2 is False:
                answer_2 = input("\nВыберите один вариант ответа: ")
                answer_2 = str(answer_2.upper())
                if str(answer_2) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_2 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_received_2 = False
            while satisfactory_answer_received_2 is False:
                answer_2 = input("\nВыберите один вариант ответа: ")
                answer_2 = answer_2.upper()
                if answer_2 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_2 in satisfactory_answer_list_1_shorted:
                    break
    if answer_2 != "В":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 1000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_3 = 1
    print("\nВопрос номер 3.")  # Номер вопроса
    print("Как звали Старую Ветошь в серии Dishonored?")  # Сам вопрос
    print("А: Вера Морэй")  # Вариант 1
    print("Б: Гарсия Бойл")  # Вариант 2
    print("В: Джелли Морли")  # Вариант 3
    print("Г: Имя по сюжету не известно")  # Вариант 4
    satisfactory_answer_received_3 = False
    while satisfactory_answer_received_3 is False:
        answer_3 = input("\nВыберите один вариант ответа: ")
        answer_3 = answer_3.upper()
        if answer_3 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_3 in satisfactory_answer_list_1:
            break
    if answer_3 == "50X50" or answer_3 == "50 X 50" or answer_3 == "50Х50" or answer_3 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nА: Вера Морэй")  # Вариант 1
            print("В: Джелли Морли")  # Вариант 2
            satisfactory_answer_received_3 = False
            while satisfactory_answer_received_3 is False:
                answer_3 = input("\nВыберите один вариант ответа: ")
                answer_3 = str(answer_3.upper())
                if str(answer_3) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_3 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_received_3 = False
            while satisfactory_answer_received_3 is False:
                answer_3 = input("\nВыберите один вариант ответа: ")
                answer_3 = answer_3.upper()
                if answer_3 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_3 in satisfactory_answer_list_1_shorted:
                    break
    if answer_3 != "А":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 2000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_4 = 1
    print("\nВопрос номер 4.")  # Номер вопроса
    print("На каком острове располагается дворец герцога в Dishonored 2?")  # Сам вопрос
    print("А: Тивия")  # Вариант 1
    print("Б: Морли")  # Вариант 2
    print("В: Гристоль")  # Вариант 3
    print("Г: Серконос")  # Вариант 4
    satisfactory_answer_reanswer_4 = False
    while satisfactory_answer_reanswer_4 is False:
        answer_4 = input("\nВыберите один вариант ответа: ")
        answer_4 = answer_4.upper()
        if answer_4 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_4 in satisfactory_answer_list_1:
            break
    if answer_4 == "50X50" or answer_4 == "50 X 50" or answer_4 == "50Х50" or answer_4 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nА: Тивия")  # Вариант 1
            print("Г: Серконос")  # Вариант 2
            satisfactory_answer_received_4 = False
            while satisfactory_answer_received_4 is False:
                answer_4 = input("\nВыберите один вариант ответа: ")
                answer_4 = str(answer_4.upper())
                if str(answer_4) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_4 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_reanswer_4 = False
            while satisfactory_answer_reanswer_4 is False:
                answer_4 = input("\nВыберите один вариант ответа: ")
                answer_4 = answer_4.upper()
                if answer_4 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_4 in satisfactory_answer_list_1_shorted:
                    break
    if answer_4 != "Г":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 3000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_5 = 1
    print("\nВопрос номер 5.")  # Номер вопроса
    print("Какой уровень в компании Geometry Dash восьмой по счёту (от Stereo Madness)?")  # Сам вопрос
    print("А: xStep")  # Вариант 1
    print("Б: Clutterfunk")  # Вариант 2
    print("В: Time Machine")  # Вариант 3
    print("Г: Cycles")  # Вариант 4
    satisfactory_answer_reanswer_5 = False
    while satisfactory_answer_reanswer_5 is False:
        answer_5 = input("\nВыберите один вариант ответа: ")
        answer_5 = answer_5.upper()
        if answer_5 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_5 in satisfactory_answer_list_1:
            break
    if answer_5 == "50X50" or answer_5 == "50 X 50" or answer_5 == "50Х50" or answer_5 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nБ: Clutterfunk")  # Вариант 1
            print("В: Time Machine")  # Вариант 2
            satisfactory_answer_received_5 = False
            while satisfactory_answer_received_5 is False:
                answer_5 = input("\nВыберите один вариант ответа: ")
                answer_5 = str(answer_5.upper())
                if str(answer_5) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_5 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_reanswer_5 = False
            while satisfactory_answer_reanswer_5 is False:
                answer_5 = input("\nВыберите один вариант ответа: ")
                answer_5 = answer_5.upper()
                if answer_5 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_5 in satisfactory_answer_list_1_shorted:
                    break
    if answer_5 != "В":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 5000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_6 = 1
    print("\nВопрос номер 6.")  # Номер вопроса
    print("Кем для Аджая Гейла является Пейган Мин?")  # Сам вопрос
    print("А: Дядей")  # Вариант 1
    print("Б: Отцом")  # Вариант 2
    print("В: Отчимом")  # Вариант 3
    print("Г: Старшим братом")  # Вариант 4
    satisfactory_answer_reanswer_6 = False
    while satisfactory_answer_reanswer_6 is False:
        answer_6 = input("\nВыберите один вариант ответа: ")
        answer_6 = answer_6.upper()
        if answer_6 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_6 in satisfactory_answer_list_1:
            break
    if answer_6 == "50X50" or answer_6 == "50 X 50" or answer_6 == "50Х50" or answer_6 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nБ: Отцом")  # Вариант 1
            print("В: Отчимом")  # Вариант 2
            satisfactory_answer_received_6 = False
            while satisfactory_answer_received_6 is False:
                answer_6 = input("\nВыберите один вариант ответа: ")
                answer_6 = str(answer_6.upper())
                if str(answer_6) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_6 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_reanswer_6 = False
            while satisfactory_answer_reanswer_6 is False:
                answer_6 = input("\nВыберите один вариант ответа: ")
                answer_6 = answer_6.upper()
                if answer_6 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_6 in satisfactory_answer_list_1_shorted:
                    break
    if answer_6 != "В":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 10000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_7 = 1
    print("\nВопрос номер 7.")  # Номер вопроса
    print("Сколько очков навыков стоит навык \"Вуаль\" в Far Cry: New Dawn?")  # Сам вопрос
    print("А: 4 очка")  # Вариант 1
    print("Б: 5 очков")  # Вариант 2
    print("В: 6 очков")  # Вариант 3
    print("Г: 8 очков")  # Вариант 4
    satisfactory_answer_reanswer_7 = False
    while satisfactory_answer_reanswer_7 is False:
        answer_7 = input("\nВыберите один вариант ответа: ")
        answer_7 = answer_7.upper()
        if answer_7 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_7 in satisfactory_answer_list_1:
            break
    if answer_7 == "50X50" or answer_7 == "50 X 50" or answer_7 == "50Х50" or answer_7 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nА: 4 очка")  # Вариант 1
            print("Г: 8 очков")  # Вариант 2
            satisfactory_answer_received_7 = False
            while satisfactory_answer_received_7 is False:
                answer_7 = input("\nВыберите один вариант ответа: ")
                answer_7 = str(answer_7.upper())
                if str(answer_7) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_7 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_reanswer_7 = False
            while satisfactory_answer_reanswer_7 is False:
                answer_7 = input("\nВыберите один вариант ответа: ")
                answer_7 = answer_7.upper()
                if answer_7 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_7 in satisfactory_answer_list_1_shorted:
                    break
    if answer_7 != "Г":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 15000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_8 = 1
    print("\nВопрос номер 8.")  # Номер вопроса
    print("Какой уровень в Geometry Dash НЕ присутствует в Fire Gauntlet?")  # Сам вопрос
    print("А: Carnation")  # Вариант 1
    print("Б: Overture")  # Вариант 2
    print("В: Shock")  # Вариант 3
    print("Г: First Race")  # Вариант 4
    satisfactory_answer_reanswer_8 = False
    while satisfactory_answer_reanswer_8 is False:
        answer_8 = input("\nВыберите один вариант ответа: ")
        answer_8 = answer_8.upper()
        if answer_8 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_8 in satisfactory_answer_list_1:
            break
    if answer_8 == "50X50" or answer_8 == "50 X 50" or answer_8 == "50Х50" or answer_8 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nА: Carnation")  # Вариант 1
            print("Г: First Race")  # Вариант 2
            satisfactory_answer_received_8 = False
            while satisfactory_answer_received_8 is False:
                answer_8 = input("\nВыберите один вариант ответа: ")
                answer_8 = str(answer_8.upper())
                if str(answer_8) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_8 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_reanswer_8 = False
            while satisfactory_answer_reanswer_8 is False:
                answer_8 = input("\nВыберите один вариант ответа: ")
                answer_8 = answer_8.upper()
                if answer_8 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_8 in satisfactory_answer_list_1_shorted:
                    break
    if answer_8 != "А":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 25000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_9 = 1
    print("\nВопрос номер 9.")  # Номер вопроса
    print("Сколько всего прицелов на автоматическую винтовку существует в Far Cry 5?")  # Сам вопрос
    print("А: 5")  # Вариант 1
    print("Б: 6")  # Вариант 2
    print("В: 7")  # Вариант 3
    print("Г: 8")  # Вариант 4
    satisfactory_answer_reanswer_9 = False
    while satisfactory_answer_reanswer_9 is False:
        answer_9 = input("\nВыберите один вариант ответа: ")
        answer_9 = answer_9.upper()
        if answer_9 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_9 in satisfactory_answer_list_1:
            break
    if answer_9 == "50X50" or answer_9 == "50 X 50" or answer_9 == "50Х50" or answer_9 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nБ: 6")  # Вариант 1
            print("Г: 8")  # Вариант 2
            satisfactory_answer_received_9 = False
            while satisfactory_answer_received_9 is False:
                answer_9 = input("\nВыберите один вариант ответа: ")
                answer_9 = str(answer_9.upper())
                if str(answer_9) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_9 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_reanswer_9 = False
            while satisfactory_answer_reanswer_9 is False:
                answer_9 = input("\nВыберите один вариант ответа: ")
                answer_9 = answer_9.upper()
                if answer_9 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_9 in satisfactory_answer_list_1_shorted:
                    break
    if answer_9 != "Б":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 50000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    attempt_10 = 1
    print("\nВопрос номер 10.")  # Номер вопроса
    print("На каком из островов располагается город \"Дануол\" в серии Dishonored?")  # Сам вопрос
    print("А: Гристоль")  # Вариант 1
    print("Б: Тивия")  # Вариант 2
    print("В: Серконос")  # Вариант 3
    print("Г: Морли")  # Вариант 4
    satisfactory_answer_reanswer_10 = False
    while satisfactory_answer_reanswer_10 is False:
        answer_10 = input("\nВыберите один вариант ответа: ")
        answer_10 = answer_10.upper()
        if answer_10 not in satisfactory_answer_list_1:
            print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
        elif answer_10 in satisfactory_answer_list_1:
            break
    if answer_10 == "50X50" or answer_10 == "50 X 50" or answer_10 == "50Х50" or answer_10 == "50 Х 50":
        if fifty_fifty == 1:
            print("\nВы использовали подсказку \"50 x 50\". 2 неверных варианта ответа были убраны.")  # Номер вопроса
            print("\nА: Гристоль")  # Вариант 1
            print("В: Серконос")  # Вариант 2
            satisfactory_answer_received_10 = False
            while satisfactory_answer_received_10 is False:
                answer_10 = input("\nВыберите один вариант ответа: ")
                answer_10 = str(answer_10.upper())
                if str(answer_10) not in satisfactory_answer_list_1:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_10 in satisfactory_answer_list_1:
                    break
            fifty_fifty -= 1
        else:
            print("Вы уже использовали эту подсказку!")
            satisfactory_answer_reanswer_10 = False
            while satisfactory_answer_reanswer_10 is False:
                answer_10 = input("\nВыберите один вариант ответа: ")
                answer_10 = answer_10.upper()
                if answer_10 not in satisfactory_answer_list_1_shorted:
                    print("Выбери \"А\", \"Б\", \"В\" или \"Г\"!")
                elif answer_10 in satisfactory_answer_list_1_shorted:
                    break
    if answer_10 != "А":
        break
    else:
        print("Абсолютно верно! Идём дальше!")
    if solid_amount == 100000:
        print(f"\nВы дошли до несгораемой суммы в {solid_amount} очков! Поздравляем!")
        solid_amount_obtained = True

    print("\nПоздравляем! Вы ответили на все вопросы верно!")
    print("Ваш рекорд: 100 000 очков.")
    print("\nВы, безусловно, знаток игровой индустрии! Вам интересно не только играть в игру, а проникнуться ей! Для вас, "
          "игра интересна как произведение искусства, а не как средство развлечения. Безусловно, вы — хороший игрок!")
    game_won = True

    break

if game_won is not True:
    print("\nК сожалению, ответ неверен. Вы проиграли.")
    if solid_amount_obtained is True:
        print("Зато, вы дошли до несгораемой суммы!")
        print(f"Ваш рекорд: {solid_amount} очков.")
        if solid_amount >= 500 and solid_amount < 5000:
            print("\nВы плохо разбираетесь в играх. Вас совершенно не интересуют детали, история, повествование... "
                  "\nВам нравятся простые игры, где не нужно думать и во что-то вникать. Сомневаюсь, что вы — хороший игрок. "
                  "\nНо, возможно, вы просто поставили низкую несгораемую сумму и ответили на "
                  "большое количество вопросов, так что не буду наговаривать.")
        elif solid_amount >= 5000 and solid_amount < 25000:
            print("\nВы — рядовой игрок. Вы уделяете играм не слишком много времени, но любите это дело! Игра — ваше хобби, "
                  "но не смысл жизни. Вас сложно назвать задротом, но, думаю, вы — неплохой игрок! Так держать!")
        elif solid_amount >= 25000:
            print("\nВы — продвинутый игрок. Ваш уровень выше среднего. Вы много играете в компьютерные игры. "
                  "Это ваш большой и, возможно, единственный интерес в жизни. \nВас считают задротом и избегают, или "
                  "с радостью играют вместе с вами из-за ваших навыков. Вас с уверенностью можно назвать хорошим игроком!")
    else:
        print("\nК сожалению, вы не дошли до несгораемой суммы! Можете попробовать пройти игру ещё раз.")
print("\nС вами был интерпретатор Python 3.7, скоро увидимся!")
