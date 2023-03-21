from logic import Shop, Store, Request

if __name__ == '__main__':
    shop = Shop()
    shop.add("печеньки", 3)
    shop.add("вафли", 4)
    shop.add("пряники", 1)
    shop.add("сок", 3)
    store = Store()
    store.add("печеньки", 20)
    store.add("вафли", 2)
    store.add("пряники", 20)
    store.add("сок", 1)


    def move_operation():
        user_str = input('Введите запрос:\nзабрать количество наименование из склад/магазин\n'
                         'или доставить количество наименование из склад в магазин/магазин в склад')
        user_str_list = user_str.split(" ")
        # print(user_str)
        # print(user_str_list)
        r = Request(user_str)
        # print(r)

        if len(user_str_list) < 5:
            print("не верный запрос")
            move_operation()

        elif not user_str_list[1].isdigit():
            print("введите число")
            move_operation()

        elif "доставить" not in user_str_list[0].lower() and "забрать" not in user_str_list[0].lower():
            print("Введите 'доставить/забрать'")
            move_operation()

        elif "магазин" not in user_str_list[4].lower() and "склад" not in user_str_list[4].lower():
            print("введите место назначения")
            move_operation()

        if user_str_list[0].lower() == "забрать":
            if user_str_list[4].lower() == "склад":
                if r.product in store.get_item():
                    if r.amount <= store.get_item()[r.product]:
                        print("Нужное количество есть на складе")
                        print(f"Курьер забирает {r.amount} {r.product} из склад")
                        store.remove(r.product, r.amount)
                    else:
                        print("Не хватает на складе, попробуйте заказать меньше")
                        move_operation()
                else:
                    print("Такого товара нет на складе")
                    move_operation()

        if user_str_list[0].lower() == "забрать":
            if user_str_list[4].lower() == "магазин":
                if r.product in shop.get_item():
                    if r.amount <= shop.get_item()[r.product]:
                        print("Нужное количество есть в магазине")
                        print(f"Курьер забирает {r.amount} {r.product} из магазина")
                        shop.remove(r.product, r.amount)
                    else:
                        print("Не хватает в магазине, попробуйте заказать меньше")
                        move_operation()
                else:
                    print("Такого товара нет в магазине")
                    move_operation()


        if user_str_list[0].lower() == "доставить":
            if user_str_list[4].lower() == "склад":
                if r.product in store.get_item():
                    if r.amount <= store.get_item()[r.product]:
                        print("Нужное количество есть на складе")
                        print("Курьер везет со склад в магазин")
                        if sum(shop.get_item().values()) + int(r.amount) < shop.capacity:
                            print(f"Курьер доставил {r.amount} {r.product} в магазин")
                            store.remove(r.product, r.amount)
                            shop.add(r.product, r.amount)

                        else:
                            print("В магазин недостаточно места, попобуйте что-то другое")
                            move_operation()

                    else:
                        print("Не хватает на складе, попробуйте заказать меньше")
                        move_operation()
                else:
                    print("Такого товара нет на складе")
                    move_operation()

        if user_str_list[0].lower() == "доставить":
            if user_str_list[4].lower() == "магазин":
                if r.product in shop.get_item():
                    if r.amount <= shop.get_item()[r.product]:
                        print("Нужное количество есть в магазин")
                        print("Курьер везет с магазина в склад")
                        if sum(store.get_item().values()) + int(r.amount) < store.capacity:
                            print(f"Курьер доставил {r.amount} {r.product} в склад")
                            shop.remove(r.product, r.amount)
                            store.add(r.product, r.amount)

                        else:
                            print("на складе недостаточно места, попобуйте что-то другое")
                            move_operation()

                    else:
                        print("Не хватает в магазине, попробуйте заказать меньше")
                        move_operation()
                else:
                    print("Такого товара нет в магазине")
                    move_operation()


    move_operation()

    print("В магазине хранится:")
    for key, value in shop.items.items():
        print(key, value)

    print("На складе хранится:")
    for key, value in store.items.items():
        print(key, value)
