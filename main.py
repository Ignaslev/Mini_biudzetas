from funkcijos import ivesti_pajams, ivesti_islaidas, ziureti_pajamas, ziureti_islaidas, statistika


def main():
    print('Sveiki atvyke!')
    while True:
        print(' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n'
              '| 1. Ivesti pajamas             |\n'
              '| 2. Istrinti pajamas           |\n'
              '| 3. Ivesti islaidas            |\n'
              '| 3. Istrinti islaidas          |\n'
              '| 4. Ziureti pajamas            |\n'
              '| 5. Ziureti islaidas           |\n'
              '| 6. Statistika                 |\n'
              '| q - iseiti                    |\n'
              '| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |\n')
        pasirinkimas = input('Pasirinkimas: ')

        if pasirinkimas == '1':  # ivesti pajamas
            ivesti_pajams()

        if pasirinkimas == '2':   # ivesti islaidas
            ivesti_islaidas()

        if pasirinkimas == '3':   # ziureti pajamas
            ziureti_pajamas()

        if pasirinkimas == '4':   # ziureti islaidas
            ziureti_islaidas()

        if pasirinkimas == '5':   # statistika
            statistika()

        if pasirinkimas == 'q':   # iseiti
            break


if __name__ == '__main__':
    main()
