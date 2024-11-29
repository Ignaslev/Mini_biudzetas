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
        pajamu_pavadinimas = input('Pajamu saltinis: ')
        pajamu_skaicius = input('Pajamos: ')
        try:
            pajamu_skaicius = int(pajamu_skaicius)
        except ValueError:
            print("Pajamos turi būti tik skaičiai. Bandykite dar kartą.")
            continue

        pajamos.append([pajamu_pavadinimas, pajamu_skaicius, formatted_date])

        testi = input('"Enter" prideti dar pajamu arba "q" grizti i menu: ')
        if testi == 'q':
            with open('pajamos.pickle', mode='wb') as file:
                # noinspection PyTypeChecker
                pickle.dump(pajamos, file)
            print("Pajamos issaugotos.")
            print()
            break
        else:
            continue


def ivesti_islaidas():
    islaidos = []

    dt_now = datetime.datetime.now()
    formatted_date = dt_now.strftime('%Y-%m-%d %H:%M')

    if os.path.exists('islaidos.pickle') and os.path.getsize('islaidos.pickle') > 0:
        with open('islaidos.pickle', mode='rb') as file:
            try:
                islaidos = pickle.load(file)
            except EOFError:
                print("Tuscias failas, pradedama su nauju")


    while True:
        islaidu_pavadinimas = input('Islaidu saltinis: ')
        islaidu_skaicius = input('Isleista: ')
        try:
            islaidu_skaicius = int(islaidu_skaicius)
        except ValueError:
            print("Pajamos turi būti tik skaičiai. Bandykite dar kartą.")
            continue

        islaidos.append([islaidu_pavadinimas, islaidu_skaicius, formatted_date])

        testi = input('"Enter" prideti dar pajamu arba "q" grizti i menu: ')
        if testi == 'q':
            with open('islaidos.pickle', mode='wb') as file:
                # noinspection PyTypeChecker
                pickle.dump(islaidos, file)
            print("islaidos issaugotos.")
            print()
            break
        else:
            continue


def ziureti_pajamas():
    if os.path.exists('pajamos.pickle') and os.path.getsize('pajamos.pickle') > 0:
        with open('pajamos.pickle', mode='rb') as file:
            pajamos = pickle.load(file)
            print(pajamos)
    else:
        print('Kolkas pajamu nera')


def ziureti_islaidas():
    if os.path.exists('islaidos.pickle') and os.path.getsize('islaidos.pickle') > 0:
        with open('islaidos.pickle', mode='rb') as file:
            islaidos = pickle.load(file)
            print(islaidos)
    else:
        print('Kolkas islaidu nera')


def statistika():
    pass
