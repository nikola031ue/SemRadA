import upiti as u


def admin_session():
    while 1:
        print("")
        print("Admin meni")
        print("1. Registruj novog Sluzbenika")
        print("2. Registruj novog Klijenta")
        print("3. Obrisi Sluzbenika")
        print("4. Obrisi Klijenta")
        print("5. Odjavi se")

        izbor = input(str("Izbor: "))
        if izbor == "1":
            print("")
            print("Registruj novog Sluzbenika")
            print("")
            ime = input(str("Ime sluzbenika: "))
            prezime = input(str("Prezime sluzbenika: "))
            password = input(str("Lozinka sluzbenika: "))
            polozaj = 1
            u.registruj(ime, prezime, password, polozaj)
        elif izbor == "2":
            print("")
            print("Registruj novog Klijenta")
            print("")
            ime = input(str("Ime klijenta: "))
            prezime = input(str("Prezime klijenta: "))
            password = input(str("Lozinka klijenta: "))
            polozaj = 2
            u.registruj(ime, prezime, password, polozaj)
        elif izbor == "3":
            print("")
            print("Obrisi Sluzbenika")
            print("")
            ime = input(str("Ime Sluzbenika: "))
            prezime = input(str("Prezime Sluzbenika: "))
            polozaj = 1
            u.brisanje(ime, prezime, polozaj)
        elif izbor == "4":
            print("")
            print("Obrisi Klijenta")
            print("")
            ime = input(str("Ime Klijenta: "))
            prezime = input(str("prezime Sluzbenika: "))
            polozaj = 2
            u.brisanje(ime, prezime, polozaj)
        elif izbor == "5":
            break
        else:
            print("Pogresan izbor")


def auth_admin():
    print("")
    print("Admin login")
    print("")

    ime = input(str("Ime: "))
    password = input(str("Lozinka: "))
    polozaj = 0
    result = u.prijava(ime, password, polozaj)
    for row in result:

        if ime == row[0]:
            if password == row[2]:
                print("Uspeh")
                admin_session()
            else:
                print("Netacna lozinka")
        else:
            print("Pogresno ime ili lozinka")