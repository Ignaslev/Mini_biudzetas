import datetime
import pickle
import os


def ivesti_pajams():
    pajamos = []

    dt_now = datetime.datetime.now()
    formatted_date = dt_now.strftime('%Y-%m-%d %H:%M')

    if os.path.exists('pajamos.pickle') and os.path.getsize('pajamos.pickle') > 0:
        with open('pajamos.pickle', mode='rb') as file:
            try:
                pajamos = pickle.load(file)
            except EOFError:
                print("File is empty. Starting with an empty list.")

    while True:
        pavadinimas = input('Pajamu saltinis: ')
        skaicius = input('Pajamos: ')
        try:
            skaicius = int(skaicius)
        except ValueError:
            print("Pajamos turi būti tik skaičiai. Bandykite dar kartą.")
            continue

        pajamos.append([pavadinimas, skaicius, formatted_date])

        testi = input('"Enter" prideti dar pajamu arba "q" grizti i menu: ')
        if testi == 'q':
            with open('pajamos.pickle', mode='wb', encoding='utf-8') as file:
                # noinspection PyTypeChecker
                pickle.dump(pajamos, file)
            print("Pajamos issaugotos.")
            print()
            break
        else:
            continue


def ivesti_islaidas():
    pass


def ziureti_pajamas():
    pass


def ziureti_islaidas():
    pass


def statistika():
    pass
