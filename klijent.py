import upiti as u


def klijent_session(ime, prezime, password, racun):
    while 1:
        print("")
        print("Klijent meni")
        print("1. Stanje racuna")
        print("2. Podigni gotovinu")
        print("3. Istorija transakcija")
        print("4. Odjavi se")
        print("")

        izbor = input(str("Izbor: "))
        if izbor == "1":
            print("")
            print("Stanje racuna")
            print("")
            polozaj = 2

            stanje = str(u.trenutno_stanje(ime, prezime, racun, polozaj))
            print("Stanje na vasem racunu broj: " + racun + " je " + stanje + " dinara")
        elif izbor == "2":
            print("")
            print("Podizanje gotovine")
            print("")
            polozaj = 2

            trenutno_stanje = u.trenutno_stanje(ime, prezime, racun, polozaj)
            print("Na stanju imate " + str(trenutno_stanje))
            print("")
            za_podizanje = input(str("Koliko gotovine zelite da podignete? "))

            if trenutno_stanje < float(za_podizanje):
                print("Nemate dovoljno gotovine na racunu!")
                print("")
            else:
                novo_stanje = trenutno_stanje - float(za_podizanje)
                u.update_stanje(ime, prezime, racun, polozaj, novo_stanje)
                print("")
                print("Podigli ste " + za_podizanje + " dinara.")
                print("")
                u.ispisi_klijenta(ime, prezime, racun, polozaj)


def auth_klijent():
    print("")
    print("Klijent login")
    print("")

    ime = input(str("Ime: "))
    prezime = input(str("Prezime: "))
    password = input(str("Lozinka: "))
    racun = input(str("Racun: "))
    polozaj = 2
    result = u.prijava(ime, password, polozaj)
    for row in result:

        if ime == row[0]:
            if password == row[2]:
                print("Uspeh")
                klijent_session(ime, prezime, password, racun)
            else:
                print("Netacna lozinka")
        else:
            print("Pogresno ime ili lozinka")
